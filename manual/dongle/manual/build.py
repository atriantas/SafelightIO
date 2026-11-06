#!/usr/bin/env python3
"""Build the SafelightIO manual from its Markdown sources.

Outputs (all next to the manual):
  examples/eez_ui/MANUAL.md                     canonical Markdown
  examples/eez_ui/MANUAL.html                   self-contained learning edition
  examples/eez_ui/SafelightIO Dongle — User Manual.pdf  print edition

Only the standard library and PyMuPDF are required for the PDF.  Run:

    python examples/eez_ui/manual/build.py
    python examples/eez_ui/manual/build.py --check
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import os
import re
import shutil
import struct
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
EEZ = HERE.parent
REPO = EEZ.parents[1]
SRC = HERE / "src"
FIG = HERE / "figures"
SOURCES = ["01-start.md", "02-tools.md", "03-control.md", "04-reference.md"]
MD_OUT = EEZ / "MANUAL.md"
HTML_OUT = EEZ / "MANUAL.html"
PDF_OUT = EEZ / "SafelightIO Dongle — User Manual.pdf"
INVENTORY = HERE / "dongle_inventory.json"

PAPER = "#FBF8F2"
INK = "#211E1B"
MUTED = "#6D635B"
LINE = "#D9CEBF"
ORANGE = "#E8730C"

BANNED = []

COVER_LOGO = HERE / "assets" / "wordmark.png"
BLACK_LOGO = HERE / "assets" / "wordmark-black.png"
DEVICE_PHOTO = HERE / "figures" / "hero-app.png"

FONT_CANDIDATES = {
    "body": ["C:/Windows/Fonts/segoeui.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
             "/System/Library/Fonts/Supplemental/Arial.ttf"],
    "bodyb": ["C:/Windows/Fonts/segoeuib.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/System/Library/Fonts/Supplemental/Arial Bold.ttf"],
    "bodyi": ["C:/Windows/Fonts/segoeuii.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
              "/System/Library/Fonts/Supplemental/Arial Italic.ttf"],
    "display": ["C:/Windows/Fonts/georgia.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
                "/System/Library/Fonts/Supplemental/Georgia.ttf"],
    "displayb": ["C:/Windows/Fonts/georgiab.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
                 "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"],
    "mono": ["C:/Windows/Fonts/consola.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
             "/System/Library/Fonts/Supplemental/Courier New.ttf"],
}


def slug(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "section"


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def inline(text: str) -> str:
    """Render the small inline subset used by the manual."""
    text = esc(text)
    stash: list[str] = []

    def code(match: re.Match[str]) -> str:
        stash.append(f"<code>{match.group(1)}</code>")
        return f"\x00{len(stash) - 1}\x00"

    text = re.sub(r"`([^`]+)`", code, text)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        text,
    )
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    for index, value in enumerate(stash):
        text = text.replace(f"\x00{index}\x00", value)
    return text


@dataclass
class Block:
    kind: str
    text: str = ""
    level: int = 0
    items: list[str] = field(default_factory=list)
    rows: list[list[str]] = field(default_factory=list)
    caption: str = ""
    src: str = ""
    callout: str = ""
    anchor: str = ""


def _is_separator(line: str) -> bool:
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{2,}:?", c or "") for c in cells)


def _image_caption(lines: list[str], index: int) -> tuple[str, int]:
    if index + 1 >= len(lines):
        return "", index + 1
    nxt = lines[index + 1].strip()
    if not (nxt.startswith("*") and not nxt.startswith("**") and nxt.endswith("*")):
        return "", index + 1
    collected = [nxt]
    cursor = index + 2
    while not collected[-1].rstrip().endswith("*") and cursor < len(lines) and lines[cursor].strip():
        collected.append(lines[cursor].strip())
        cursor += 1
    caption = " ".join(collected).strip()
    caption = caption[1:-1].strip() if caption.startswith("*") and caption.endswith("*") else caption
    return caption, cursor


def _collect_list(lines: list[str], index: int, ordered: bool) -> tuple[list[str], int]:
    pattern = r"^\s*\d+\.\s+" if ordered else r"^\s*[-*]\s+"
    items: list[str] = []
    current: str | None = None
    while index < len(lines):
        raw = lines[index]
        stripped = raw.strip()
        if not stripped:
            probe = index + 1
            while probe < len(lines) and not lines[probe].strip():
                probe += 1
            if probe < len(lines) and re.match(pattern, lines[probe]):
                index = probe
                continue
            break
        if re.match(pattern, raw):
            if current is not None:
                items.append(current)
            current = re.sub(pattern, "", raw).strip()
            index += 1
            continue
        if re.match(r"^\s*[-*]\s+", raw) or re.match(r"^\s*\d+\.\s+", raw):
            break
        if "|" in raw and index + 1 < len(lines) and _is_separator(lines[index + 1]):
            break
        if stripped.startswith(("#", ">", "```", "![")):
            break
        if current is not None:
            current = f"{current} {stripped}"
            index += 1
            continue
        break
    if current is not None:
        items.append(current)
    return items, index


def parse_markdown(path: Path) -> list[Block]:
    lines = path.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
    blocks: list[Block] = []
    index = 0
    while index < len(lines):
        raw = lines[index]
        line = raw.rstrip()
        if not line.strip():
            index += 1
            continue
        if line.startswith("```"):
            cursor = index + 1
            code: list[str] = []
            while cursor < len(lines) and not lines[cursor].startswith("```"):
                code.append(lines[cursor])
                cursor += 1
            blocks.append(Block("code", text="\n".join(code)))
            index = cursor + 1
            continue
        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            blocks.append(Block("h" + str(len(heading.group(1))), text=heading.group(2).strip(),
                                level=len(heading.group(1))))
            index += 1
            continue
        if re.fullmatch(r"-{3,}", line.strip()):
            blocks.append(Block("hr"))
            index += 1
            continue
        image = re.fullmatch(r"!\[([^\]]*)\]\(([^)]+)\)", line.strip())
        if image:
            caption, cursor = _image_caption(lines, index)
            blocks.append(Block("image", text=image.group(1), src=image.group(2), caption=caption))
            index = cursor
            continue
        if line.lstrip().startswith(">"):
            quote_lines: list[str] = []
            while index < len(lines) and lines[index].lstrip().startswith(">"):
                content = lines[index].lstrip()[1:]
                if content.startswith(" "):
                    content = content[1:]
                quote_lines.append(content.rstrip())
                index += 1
            callout = ""
            first = next((q for q in quote_lines if q.strip()), "")
            found = re.match(r"^\[!([A-Za-z]+)\]", first.strip())
            if found:
                callout = found.group(1).upper()
            blocks.append(Block("quote", text="\n".join(quote_lines), callout=callout))
            continue
        if "|" in line and index + 1 < len(lines) and _is_separator(lines[index + 1]):
            rows = []
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(header)
            index += 2
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                rows.append([c.strip() for c in lines[index].strip().strip("|").split("|")])
                index += 1
            blocks.append(Block("table", rows=rows))
            continue
        if re.match(r"^\s*[-*]\s+", line):
            items, index = _collect_list(lines, index, ordered=False)
            blocks.append(Block("ul", items=items))
            continue
        if re.match(r"^\s*\d+\.\s+", line):
            items, index = _collect_list(lines, index, ordered=True)
            blocks.append(Block("ol", items=items))
            continue
        paragraph = [line.strip()]
        index += 1
        while index < len(lines) and lines[index].strip():
            nxt = lines[index].strip()
            if re.match(r"^(#{1,6})\s+", nxt) or nxt.startswith(">") or nxt.startswith("```"):
                break
            if re.fullmatch(r"-{3,}", nxt):
                break
            if re.match(r"^\s*[-*]\s+", nxt) or re.match(r"^\s*\d+\.\s+", nxt):
                break
            if nxt.startswith("!["):
                break
            paragraph.append(nxt)
            index += 1
        blocks.append(Block("p", text=" ".join(paragraph)))
    # stable, unique heading anchors
    seen: dict[str, int] = {}
    for block in blocks:
        if block.kind.startswith("h"):
            base = slug(block.text)
            count = seen.get(base, 0)
            seen[base] = count + 1
            block.anchor = base if count == 0 else f"{base}-{count + 1}"
    return blocks


def assemble_markdown() -> str:
    parts = []
    for name in SOURCES:
        text = (SRC / name).read_text(encoding="utf-8").replace("\r\n", "\n").strip()
        parts.append(text)
    markdown = "\n\n".join(parts).strip() + "\n"
    return markdown


def asset_path(src: str) -> Path:
    if src.startswith("manual/figures/"):
        return HERE / "figures" / Path(src).name
    if src.startswith("figures/"):
        return HERE / "figures" / Path(src).name
    return EEZ / src


def data_uri(path: Path) -> str:
    mime = "image/svg+xml" if path.suffix.lower() == ".svg" else "image/png"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def svg_size(path: Path) -> tuple[int, int]:
    match = re.search(r'viewBox="0 0 (\d+) (\d+)"', path.read_text(encoding="utf-8"))
    if match:
        return int(match.group(1)), int(match.group(2))
    return 940, 500


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        width, height = struct.unpack(">II", data[16:24])
        return width, height
    return 940, 500


def image_size(path: Path) -> tuple[int, int]:
    if path.suffix.lower() == ".svg":
        return svg_size(path)
    return png_size(path)


def figure_width(path: Path) -> int:
    width, height = image_size(path)
    ratio = height / width if width else 0.5
    if ratio > 1.2:
        return 190
    if ratio > 0.62:
        return 460
    return 470


def render_callout(block: Block, mode: str) -> str:
    lines = block.text.split("\n")
    if lines and re.match(r"^\[![A-Za-z]+\]", lines[0].strip()):
        lines = lines[1:]
    while lines and not lines[0].strip():
        lines.pop(0)
    groups: list[str] = []
    current: list[str] = []
    for line in lines:
        if not line.strip():
            if current:
                groups.append(" ".join(current))
                current = []
        elif line.lstrip().startswith("- "):
            if current:
                groups.append(" ".join(current))
                current = []
            groups.append(line.lstrip())
        else:
            current.append(line.strip())
    if current:
        groups.append(" ".join(current))
    title = block.callout.title() if block.callout else "Note"
    out = [f'<div class="callout {block.callout.lower()}">']
    out.append(f'<p class="callout-title">{esc(title)}</p>')
    for group in groups:
        if group.startswith("- "):
            out.append("<ul>")
            for item in [g for g in groups if g.startswith("- ")]:
                out.append(f"<li>{inline(item[2:])}</li>")
            out.append("</ul>")
            groups = [g for g in groups if not g.startswith("- ")]
            break
    for group in groups:
        if group.startswith("- "):
            continue
        out.append(f"<p>{inline(group)}</p>")
    out.append("</div>")
    return "\n".join(out)


def render_table(rows: list[list[str]], mode: str) -> str:
    if not rows:
        return ""
    out = ['<div class="table-wrap"><table>']
    out.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in rows[0]) + "</tr></thead>")
    out.append("<tbody>")
    for row in rows[1:]:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def render_blocks(blocks: list[Block], mode: str, promote_first_h2: bool = False) -> str:
    out: list[str] = []
    promoted = False
    for block in blocks:
        kind = block.kind
        if kind == "h1":
            out.append(f'<h1 id="{block.anchor}">{inline(block.text)}</h1>')
        elif kind == "h2":
            if promote_first_h2 and not promoted:
                out.append(f'<h1 id="{block.anchor}">{inline(block.text)}</h1>')
                promoted = True
            else:
                out.append(f'<h2 id="{block.anchor}">{inline(block.text)}</h2>')
        elif kind == "h3":
            out.append(f'<h3 id="{block.anchor}">{inline(block.text)}</h3>')
        elif kind == "h4":
            out.append(f'<h4 id="{block.anchor}">{inline(block.text)}</h4>')
        elif kind == "p":
            out.append(f"<p>{inline(block.text)}</p>")
        elif kind == "ul":
            out.append("<ul>")
            for item in block.items:
                check = re.match(r"^\[ \]\s+(.*)$", item)
                if check:
                    mark = "☐" if mode == "html" else "[ ]"
                    out.append(f'<li class="task"><span class="checkbox">{mark}</span> {inline(check.group(1))}</li>')
                else:
                    out.append(f"<li>{inline(item)}</li>")
            out.append("</ul>")
        elif kind == "ol":
            out.append("<ol>")
            for item in block.items:
                out.append(f"<li>{inline(item)}</li>")
            out.append("</ol>")
        elif kind == "table":
            out.append(render_table(block.rows, mode))
        elif kind == "quote":
            out.append(render_callout(block, mode))
        elif kind == "hr":
            out.append("<hr>")
        elif kind == "code":
            out.append(f"<pre><code>{esc(block.text)}</code></pre>")
        elif kind == "image":
            path = asset_path(block.src)
            caption = f'<p class="caption">{inline(block.caption)}</p>' if block.caption else ""
            if mode == "html":
                out.append(
                    f'<figure><img src="{data_uri(path)}" alt="{esc(block.text)}" loading="lazy">'
                    f"{caption}</figure>"
                )
            else:
                width = figure_width(path)
                src = path.name
                out.append(
                    f'<div class="figure"><img src="{src}" width="{width}">' f"{caption}</div>"
                )
    return "\n".join(out)


def split_document(blocks: list[Block]) -> tuple[list[Block], list[Block]]:
    start = next((i for i, b in enumerate(blocks) if b.kind == "h1" and b.text.startswith("1.")), len(blocks))
    return blocks[:start], blocks[start:]


def howto_blocks(front: list[Block]) -> list[Block]:
    start = next((i for i, b in enumerate(front) if b.kind == "h2" and "How to use" in b.text), None)
    if start is None:
        return []
    end = next((i for i, b in enumerate(front) if i > start and b.kind == "h2" and b.text.startswith("Contents")), len(front))
    return front[start:end]


def chapters(blocks: list[Block]) -> list[dict]:
    result: list[dict] = []
    current = None
    for block in blocks:
        if block.kind == "h1":
            current = {"title": block.text, "anchor": block.anchor, "sections": [], "blocks": []}
            result.append(current)
        if current is not None:
            current["blocks"].append(block)
            if block.kind == "h2":
                current["sections"].append(block)
    return result


def toc_data(body: list[Block]) -> list[dict]:
    result: list[dict] = []
    current = None
    for block in body:
        if block.kind == "h1":
            current = {"title": block.text, "anchor": block.anchor, "sections": []}
            result.append(current)
        elif block.kind == "h2" and current is not None:
            current["sections"].append({"title": block.text, "anchor": block.anchor})
    return result


def search_data(body: list[Block]) -> list[dict]:
    """Flatten headings, prose, lists and tables into a small search index."""
    result: list[dict] = []
    current = None

    def clean(text: str) -> str:
        return re.sub(r"[*`#>\[\]]", "", text or "").strip()

    def add(text: str) -> None:
        nonlocal current
        if current is None:
            return
        text = clean(text)
        if text and len(current["text"]) < 1600:
            current["text"] = (current["text"] + " " + text).strip()

    for block in body:
        if block.kind in ("h1", "h2"):
            current = {"title": block.text, "anchor": block.anchor, "text": ""}
            result.append(current)
        elif current is not None:
            if block.kind in ("p", "quote", "code"):
                add(block.text)
            if block.kind in ("ul", "ol"):
                for item in block.items:
                    add(item)
            if block.kind == "table":
                for row in block.rows:
                    for cell in row:
                        add(cell)
            if block.kind == "image":
                add(block.caption)
    return result


CSS = """
:root{
  --paper:#FBF8F2; --ink:#211E1B; --muted:#6D635B; --line:#D9CEBF;
  --accent:#E8730C; --accent2:#F2A33A; --panel:#FFFFFF; --code:#F2ECE2;
  --shadow:0 10px 30px rgba(40,30,20,.08); --max:1180px;
}
html[data-theme="darkroom"]{
  --paper:#0D0908; --ink:#F4E8D6; --muted:#C9A79A; --line:#3A2620;
  --accent:#FF4B3E; --accent2:#F2A33A; --panel:#171110; --code:#241A17;
  --shadow:0 10px 30px rgba(0,0,0,.35);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);
  font:16px/1.6 "Segoe UI",system-ui,-apple-system,Helvetica,Arial,sans-serif;}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
code{font-family:Consolas,"SFMono-Regular",monospace;background:var(--code);
  padding:.1em .3em;border-radius:4px;font-size:.92em}
hr{border:0;border-top:1px solid var(--line);margin:28px 0}
.skip{position:absolute;left:-9999px;top:0;background:var(--ink);color:var(--paper);padding:10px 14px;z-index:100}
.skip:focus{left:10px;top:10px}
.topbar{position:sticky;top:0;z-index:40;background:rgba(18,15,14,.96);
  color:#F4E8D6;border-bottom:1px solid rgba(244,232,214,.14);backdrop-filter:blur(8px)}
.topbar-inner{max-width:var(--max);margin:0 auto;padding:10px 24px;display:flex;align-items:center;gap:14px}
.brand{display:flex;align-items:center;gap:10px;color:#F4E8D6;font-weight:600;letter-spacing:.01em}
.brand img{height:26px;width:auto}
.brand small{color:#C9A79A;font-weight:400;font-size:12px}
.topbar .spacer{flex:1}
.tool{border:1px solid rgba(244,232,214,.28);background:transparent;color:#F4E8D6;
  border-radius:8px;padding:7px 11px;font:inherit;font-size:13px;cursor:pointer}
.tool:hover{border-color:#F2A33A;color:#F2A33A}
.tool.primary{background:#E8730C;border-color:#E8730C;color:#fff}
.hero{background:linear-gradient(145deg,#151110 0%,#211A16 58%,#2B2018 100%);color:#F4E8D6}
.hero-inner{max-width:var(--max);margin:auto;padding:52px 24px 44px;
  display:grid;grid-template-columns:1.15fr .85fr;gap:38px;align-items:center}
.hero .eyebrow{color:#F2A33A;text-transform:uppercase;letter-spacing:.14em;font-size:12px;font-weight:700}
.hero h1{font-family:Georgia,"Times New Roman",serif;font-size:clamp(38px,5vw,62px);
  line-height:1.03;margin:14px 0 10px;font-weight:700}
.hero h1 span{color:#E8730C}
.hero .sub{font-size:18px;color:#D8C8BB;max-width:46ch;margin:0 0 20px}
.hero .meta{display:flex;flex-wrap:wrap;gap:8px}
.chip{border:1px solid rgba(244,232,214,.25);border-radius:999px;padding:5px 11px;
  font-size:12.5px;color:#E8D8C9}
.hero .photo{position:relative;text-align:center}
.hero .photo img{max-width:100%;border-radius:18px;box-shadow:0 22px 50px rgba(0,0,0,.45);
  border:1px solid rgba(244,232,214,.2)}
.hero .photo figcaption{font-size:11.5px;color:#B9A99A;margin-top:10px}
.layout{max-width:var(--max);margin:0 auto;padding:34px 24px 70px;
  display:grid;grid-template-columns:270px minmax(0,1fr);gap:36px;align-items:start}
.sidebar{position:sticky;top:78px;max-height:calc(100vh - 100px);overflow:auto;
  border-right:1px solid var(--line);padding-right:18px}
.sidebar .label{font-size:11px;letter-spacing:.13em;text-transform:uppercase;
  color:var(--muted);margin:0 0 10px;font-weight:700}
.sidebar a{display:block;padding:4px 0 4px 10px;border-left:2px solid transparent;
  color:var(--muted);font-size:13.5px;line-height:1.35}
.sidebar a:hover{color:var(--ink);text-decoration:none;border-left-color:var(--accent2)}
.sidebar a.active{color:var(--accent);border-left-color:var(--accent);font-weight:600}
.sidebar a.chapter{color:var(--ink);font-weight:600;margin-top:11px}
.sidebar a.section{padding-left:22px;font-size:12.5px}
main{min-width:0;max-width:840px}
main h1{font-family:Georgia,"Times New Roman",serif;font-size:clamp(28px,3.4vw,40px);
  line-height:1.12;margin:54px 0 14px;padding-bottom:10px;border-bottom:2px solid var(--accent)}
main h1:first-child{margin-top:0}
main h2{font-size:23px;line-height:1.25;margin:34px 0 8px;letter-spacing:-.01em}
main h3{font-size:17px;margin:24px 0 6px}
main h4{font-size:15px;margin:18px 0 4px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
main p{margin:0 0 12px}
main ul,main ol{margin:0 0 14px 22px;padding:0}
main li{margin:0 0 6px}
main li.task{list-style:none;margin-left:-22px}
.checkbox{color:var(--accent);font-size:17px;margin-right:6px}
.table-wrap{overflow-x:auto;margin:14px 0 20px;border:1px solid var(--line);border-radius:8px}
table{width:100%;border-collapse:collapse;font-size:14.5px;background:var(--panel)}
th,td{padding:8px 10px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
th{background:var(--code);font-size:12.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
tr:last-child td{border-bottom:0}
figure{margin:22px 0;text-align:center}
figure img{max-width:100%;height:auto;border-radius:10px;border:1px solid var(--line);
  background:#FBF8F2}
.caption{font-size:12.5px;color:var(--muted);font-style:italic;margin:7px 0 0}
.callout{border-left:4px solid var(--accent);background:var(--code);padding:14px 18px;
  margin:20px 0;border-radius:0 8px 8px 0}
.callout p:last-child{margin-bottom:0}
.callout .callout-title{font-size:11px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--accent);font-weight:700;margin:0 0 4px}
.callout.note{border-left-color:#3D6E9E}
.callout.tip{border-left-color:#2A7F7F}
.callout.warning{border-left-color:#B3261E}
.howto{border-top:1px solid var(--line);padding-top:8px}
.footer{max-width:var(--max);margin:0 auto;padding:26px 24px 60px;border-top:1px solid var(--line);
  color:var(--muted);font-size:13px;display:flex;flex-wrap:wrap;gap:14px;justify-content:space-between}
.footer a{color:var(--accent)}
.backtop{position:fixed;right:22px;bottom:22px;z-index:30;border:0;border-radius:50%;
  width:44px;height:44px;background:var(--accent);color:#fff;font-size:18px;cursor:pointer;
  display:none;box-shadow:var(--shadow)}
.search-overlay{position:fixed;inset:0;background:rgba(15,12,10,.72);z-index:60;
  display:none;padding:8vh 18px}
.search-overlay.open{display:block}
.search-box{max-width:720px;margin:auto;background:var(--paper);border:1px solid var(--line);
  border-radius:14px;box-shadow:var(--shadow);overflow:hidden}
.search-box input{width:100%;border:0;border-bottom:1px solid var(--line);padding:16px 18px;
  font:inherit;font-size:17px;background:transparent;color:var(--ink);outline:none}
.search-results{max-height:58vh;overflow:auto;padding:8px}
.search-results a{display:block;padding:10px 12px;border-radius:8px;color:var(--ink)}
.search-results a:hover{background:var(--code);text-decoration:none}
.search-results small{display:block;color:var(--muted);font-size:12px;margin-top:2px}
.search-empty{padding:18px;color:var(--muted);font-size:14px}
@media (max-width:920px){
  .layout{grid-template-columns:1fr;padding-top:22px}
  .sidebar{position:static;max-height:none;border-right:0;border-bottom:1px solid var(--line);
    padding:0 0 16px;margin-bottom:8px}
  .hero-inner{grid-template-columns:1fr;padding-top:36px}
  .hero .photo{max-width:340px;margin:auto}
  .brand small{display:none}
}
@media print{
  .topbar,.sidebar,.search-overlay,.backtop,.hero .photo,.hero .meta{display:none!important}
  body{background:#fff;color:#111;font-size:10.5pt}
  .hero{background:#fff;color:#111}
  .hero-inner{display:block;padding:0 0 12pt}
  .hero h1{color:#111;font-size:30pt}
  .hero h1 span{color:#B3540A}
  .hero .sub{color:#333}
  .layout{display:block;padding:0}
  main{max-width:none}
  main h1{page-break-before:always;break-before:page;border-bottom:1pt solid #B3540A}
  main h1:first-of-type{page-break-before:auto;break-before:auto}
  figure,table,.callout{page-break-inside:avoid;break-inside:avoid}
  .table-wrap{border:0}
  a{color:#111;text-decoration:none}
  .footer{display:none}
}
"""

HTML_JS = """
(function(){
  const root=document.documentElement;
  const key='safelight-manual-theme';
  try{const saved=localStorage.getItem(key); if(saved) root.dataset.theme=saved;}catch(e){}
  const toggle=document.getElementById('theme');
  function sync(){toggle.textContent=root.dataset.theme==='darkroom'?'Paper':'Darkroom';}
  sync();
  toggle.addEventListener('click',()=>{
    root.dataset.theme=root.dataset.theme==='darkroom'?'':'darkroom';
    try{localStorage.setItem(key,root.dataset.theme);}catch(e){}
    sync();
  });
  const links=[...document.querySelectorAll('.sidebar a')];
  const heads=[...document.querySelectorAll('main h1[id],main h2[id]')];
  const byId=new Map(links.map(a=>[a.getAttribute('href').slice(1),a]));
  if('IntersectionObserver' in window){
    const obs=new IntersectionObserver(entries=>{
      for(const e of entries){ if(e.isIntersecting){ links.forEach(a=>a.classList.remove('active'));
        const a=byId.get(e.target.id); if(a) a.classList.add('active'); } }
    },{rootMargin:'-15% 0px -75% 0px',threshold:[0,1]});
    heads.forEach(h=>obs.observe(h));
  }
  const top=document.getElementById('backtop');
  window.addEventListener('scroll',()=>{top.style.display=window.scrollY>700?'block':'none';},{passive:true});
  top.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
  const overlay=document.getElementById('search');
  const input=document.getElementById('search-input');
  const results=document.getElementById('search-results');
  const data=window.SEARCH_DATA||[];
  function openSearch(){overlay.classList.add('open');input.value='';render('');input.focus();}
  function closeSearch(){overlay.classList.remove('open');}
  function render(q){
    const term=q.trim().toLowerCase();
    const hits=term?data.filter(d=>(d.title+' '+d.text).toLowerCase().includes(term)).slice(0,30):data.slice(0,14);
    results.innerHTML=hits.length?hits.map(d=>`<a href="#${d.anchor}"><strong>${d.title}</strong><small>${d.text.slice(0,140)}</small></a>`).join(''):'<div class="search-empty">No matching section.</div>';
  }
  document.getElementById('search-open').addEventListener('click',openSearch);
  document.getElementById('search-close').addEventListener('click',closeSearch);
  overlay.addEventListener('click',e=>{if(e.target===overlay)closeSearch();});
  input.addEventListener('input',()=>render(input.value));
  document.addEventListener('keydown',e=>{
    if(e.key==='/'&&document.activeElement!==input){e.preventDefault();openSearch();}
    if(e.key==='Escape')closeSearch();
  });
})();
"""


def build_html(front: list[Block], body: list[Block], toc: list[dict], search: list[dict]) -> str:
    howto = howto_blocks(front)
    idea = next((b for b in front if b.kind == "quote" and b.callout == "IDEA"), None)
    intro = ""
    if idea:
        intro += render_callout(idea, "html")
    intro += render_blocks(howto, "html", promote_first_h2=True)

    nav = ['<p class="label">Contents</p>']
    nav.append('<a class="chapter" href="#how-to-use-this-manual">How to use this manual</a>')
    for chapter in toc:
        nav.append(f'<a class="chapter" href="#{chapter["anchor"]}">{inline(chapter["title"])}</a>')
        for section in chapter["sections"]:
            nav.append(f'<a class="section" href="#{section["anchor"]}">{inline(section["title"])}</a>')

    content = intro + "\n" + render_blocks(body, "html")
    search_json = json.dumps(search, ensure_ascii=False).replace("</", "<\\/")
    logo = data_uri(COVER_LOGO)
    photo = data_uri(DEVICE_PHOTO)
    pdf_href = quote(PDF_OUT.name)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SafelightIO Dongle — User Manual</title>
<meta name="description" content="Illustrated user manual for the SafelightIO USB dongle and Android app, firmware 0.11 and later.">
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">Skip to the manual</a>
<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="#top"><img src="{logo}" alt="SafelightIO"><small>Dongle manual · firmware 0.11+</small></a>
    <span class="spacer"></span>
    <button class="tool" id="search-open" type="button" aria-label="Search the manual">Search</button>
    <button class="tool" id="theme" type="button">Darkroom</button>
    <button class="tool primary" type="button" onclick="window.print()">Print</button>
    <a class="tool" href="{pdf_href}">PDF</a>
  </div>
</header>
<section class="hero" id="top">
  <div class="hero-inner">
    <div>
      <div class="eyebrow">Firmware 0.11+ · First edition</div>
      <h1>Safelight<span>IO</span><br><em style="font-size:.55em;color:#E8D8C9">The dongle, explained</em></h1>
      <p class="sub">From the first USB connection to a finished print: the dongle, the Android app, every control and every setting, in plain language.</p>
      <div class="meta"><span class="chip">USB dongle + Android app</span><span class="chip">Five tools</span><span class="chip">Every control explained</span></div>
    </div>
    <figure class="photo">
      <img src="{photo}" alt="The SafelightIO Exposure screen in the Android app">
      <figcaption>The phone is the dongle’s screen. The app is shown at darkroom brightness; the labels match firmware 0.11 and later.</figcaption>
    </figure>
  </div>
</section>
<div class="layout">
  <aside class="sidebar" aria-label="Contents">{''.join(nav)}</aside>
  <main id="main">
    {content}
  </main>
</div>
<footer class="footer">
  <span>SafelightIO Dongle · Firmware 0.11+ · First edition, November 2026</span>
  <span><a href="{pdf_href}">Download the print edition (PDF)</a> · <a href="#top">Back to top</a></span>
</footer>
<button class="backtop" id="backtop" type="button" aria-label="Back to top">↑</button>
<div class="search-overlay" id="search" role="dialog" aria-modal="true" aria-label="Search">
  <div class="search-box">
    <input id="search-input" type="search" placeholder="Search controls, messages, tasks…" autocomplete="off">
    <div class="search-results" id="search-results"></div>
  </div>
</div>
<div id="search-close" hidden></div>
<script>window.SEARCH_DATA={search_json};</script>
<script>{HTML_JS}</script>
</body>
</html>
"""


PDF_CSS = """
@font-face { font-family: Body; src: url(segoeui.ttf); }
@font-face { font-family: BodyB; src: url(segoeuib.ttf); }
@font-face { font-family: BodyI; src: url(segoeuii.ttf); }
@font-face { font-family: Display; src: url(georgia.ttf); }
@font-face { font-family: DisplayB; src: url(georgiab.ttf); }
@font-face { font-family: Mono; src: url(consola.ttf); }
body { font-family: Body; font-size: 9.3pt; line-height: 1.42; color: #26221F; }
h1 { font-family: DisplayB; font-size: 22pt; color: #211E1B; margin: 0 0 10pt 0;
     padding-bottom: 4pt; border-bottom: 1.5pt solid #E8730C; }
h2 { font-family: BodyB; font-size: 13pt; color: #211E1B; margin: 13pt 0 4pt 0; }
h3 { font-family: BodyB; font-size: 10.5pt; color: #211E1B; margin: 10pt 0 2pt 0; }
h4 { font-family: BodyB; font-size: 9.5pt; color: #6D635B; margin: 8pt 0 2pt 0; }
p { margin: 0 0 5.5pt 0; }
ul, ol { margin: 0 0 6pt 16pt; }
li { margin: 0 0 2.5pt 0; }
table { width: 100%; border-collapse: collapse; font-size: 7.9pt; margin: 5pt 0 8pt 0; }
th { background: transparent; text-align: left; padding: 3pt; border: 0.5pt solid #D9CEBF;
     border-bottom: 1pt solid #B3540A; }
td { padding: 3pt; border: 0.5pt solid #D9CEBF; vertical-align: top; }
.callout { background: #FDF3E7; border-left: 3pt solid #E8730C; padding: 6pt 8pt; margin: 7pt 0; }
.callout.note { background: #EEF3F7; border-left-color: #3D6E9E; }
.callout.tip { background: #EDF5F2; border-left-color: #2A7F7F; }
.callout.warning { background: #F8E9E6; border-left-color: #B3261E; }
.callout-title { font-family: BodyB; font-size: 7.5pt; color: #B3540A; margin: 0 0 2pt 0; }
.figure { text-align: center; margin: 6pt 0 0 0; }
.caption { font-family: BodyI; font-size: 7.8pt; color: #6D635B; text-align: center;
           margin: 2pt 0 8pt 0; }
code { font-family: Mono; font-size: 8pt; background: #F2ECE2; }
hr { border-top: 0.5pt solid #D9CEBF; margin: 8pt 0; }
a { color: #B3540A; }
strong { font-family: BodyB; }
"""


def _font_files() -> dict[str, Path]:
    result = {}
    for name, candidates in FONT_CANDIDATES.items():
        for candidate in candidates:
            path = Path(candidate)
            if path.exists():
                result[name] = path
                break
    return result


def story_doc(html_text: str, archive, out: Path, page_rect=(0, 0, 595, 842),
              content_rect=(54, 56, 541, 792)) -> object:
    import pymupdf

    story = pymupdf.Story(html=html_text, user_css=PDF_CSS, archive=archive)
    writer = pymupdf.DocumentWriter(str(out))
    box = pymupdf.Rect(*page_rect)
    content = pymupdf.Rect(*content_rect)
    matrix = pymupdf.Matrix(1, 0, 0, 1, 0, 0)

    def rectfn(_number, _filled):
        return box, content, matrix

    story.write(writer, rectfn)
    writer.close()
    doc = pymupdf.open(str(out))
    return doc


def _chapter_html(chapter: dict) -> str:
    return "<html><body>" + render_blocks(chapter["blocks"], "pdf") + "</body></html>"


def _page_footer(page, chapter_title: str, number: int, fonts: dict, pdf):
    page.draw_line((54, 806), (541, 806), color=(0.85, 0.81, 0.76), width=0.5)
    page.insert_text((54, 820), chapter_title, fontsize=7, fontname="helv",
                     color=(0.42, 0.38, 0.34))
    page.insert_text((541 - 24, 820), str(number), fontsize=7, fontname="helv",
                     color=(0.42, 0.38, 0.34))


def _register_fonts(page, fonts: dict):
    import pymupdf

    names = {}
    for key, label in [("body", "body"), ("bodyb", "bodyb"), ("display", "display"),
                       ("displayb", "displayb"), ("mono", "mono")]:
        if key in fonts:
            try:
                page.insert_font(fontname=label, fontfile=str(fonts[key]))
                names[key] = label
            except Exception:
                pass
    return names


def _draw_cover(page, fonts: dict, logo: Path):
    import pymupdf

    page.draw_rect(page.rect, color=None, fill=(0.984, 0.973, 0.949))
    page.draw_rect(pymupdf.Rect(0, 0, 595, 430), color=None, fill=(0.082, 0.071, 0.063))
    names = _register_fonts(page, fonts)
    if logo.exists():
        page.insert_image(pymupdf.Rect(54, 52, 294, 97), filename=str(logo))
    page.insert_text((54, 146), "DONGLE MANUAL  ·  FIRMWARE 0.11+", fontsize=8.5,
                     fontname=names.get("bodyb", "helv"), color=(0.95, 0.64, 0.23))
    page.insert_text((54, 218), "The dongle", fontsize=35,
                     fontname=names.get("displayb", "times-bold"), color=(0.957, 0.91, 0.84))
    page.insert_text((54, 258), "explained", fontsize=35,
                     fontname=names.get("displayb", "times-bold"), color=(0.91, 0.45, 0.05))
    page.insert_text((54, 300), "From the first USB connection to a finished print.", fontsize=11.5,
                     fontname=names.get("body", "helv"), color=(0.86, 0.78, 0.70))
    page.draw_line((54, 325), (134, 325), color=(0.91, 0.45, 0.05), width=2)

    strip_y = 470
    page.insert_text((54, 454), "THE TONE SCALE", fontsize=7.5,
                     fontname=names.get("bodyb", "helv"), color=(0.42, 0.38, 0.34))
    count = 11
    width = 487 / count
    for index in range(count):
        value = index / (count - 1)
        shade = 0.06 + value * 0.88
        page.draw_rect(pymupdf.Rect(54 + index * width, strip_y, 54 + (index + 1) * width, strip_y + 24),
                       color=(0.85, 0.81, 0.76), fill=(shade, shade, shade), width=0.4)
        page.insert_text((54 + index * width + width / 2 - 2, strip_y + 36), str(index),
                         fontsize=6.5, fontname=names.get("body", "helv"),
                         color=(0.42, 0.38, 0.34))
    page.insert_text((54, 550), "Inside", fontsize=16,
                     fontname=names.get("displayb", "times-bold"), color=(0.13, 0.12, 0.11))
    lines = [
        "Five tools: Exposure, Contrast, Split Grade, Virtual Proof, Setup.",
        "Every control and readout, with screen maps and step diagrams.",
        "Paper and sensor calibration, files, troubleshooting and firmware updates.",
    ]
    for index, line in enumerate(lines):
        page.insert_text((54, 578 + index * 19), line, fontsize=9.2,
                         fontname=names.get("body", "helv"), color=(0.22, 0.20, 0.18))
    page.draw_line((54, 780), (541, 780), color=(0.85, 0.81, 0.76), width=0.6)
    page.insert_text((54, 800), "First edition  ·  November 2026  ·  Firmware 0.11+", fontsize=8,
                     fontname=names.get("body", "helv"), color=(0.42, 0.38, 0.34))
    if BLACK_LOGO.exists():
        page.insert_image(pymupdf.Rect(541 - 84, 788, 541, 804), filename=str(BLACK_LOGO))
    else:
        page.insert_text((541 - 84, 800), "SafelightIO", fontsize=8,
                         fontname=names.get("bodyb", "helv"), color=(0.91, 0.45, 0.05))


def _draw_toc(page, chapters: list[dict], page_numbers: list[int], fonts: dict):
    import pymupdf

    names = _register_fonts(page, fonts)
    page.draw_rect(page.rect, color=None, fill=(0.984, 0.973, 0.949))
    page.insert_text((54, 86), "Contents", fontsize=28,
                     fontname=names.get("displayb", "times-bold"), color=(0.13, 0.12, 0.11))
    page.draw_line((54, 104), (541, 104), color=(0.91, 0.45, 0.05), width=1.5)
    page.insert_text((54, 130), "Fifteen chapters, in the order you will use them.", fontsize=9,
                     fontname=names.get("body", "helv"), color=(0.42, 0.38, 0.34))
    y = 168
    for chapter, number in zip(chapters, page_numbers):
        title = chapter["title"]
        page.insert_text((54, y), title, fontsize=10.2,
                         fontname=names.get("body", "helv"), color=(0.13, 0.12, 0.11))
        width = pymupdf.get_text_length(title, fontname="helv", fontsize=10.2)
        x1 = 54 + width + 6
        x2 = 541 - 20
        for x in range(int(x1), int(x2), 5):
            page.draw_circle((x, y - 2), 0.35, color=(0.55, 0.50, 0.45), fill=(0.55, 0.50, 0.45), width=0)
        page.insert_text((541 - 14, y), str(number), fontsize=10,
                         fontname=names.get("bodyb", "helv"), color=(0.91, 0.45, 0.05))
        y += 27
    page.insert_text((54, 790), "Page numbers match the printed footer.", fontsize=7.5,
                     fontname=names.get("bodyi", "helv"), color=(0.42, 0.38, 0.34))


def build_pdf(front: list[Block], body: list[Block]) -> None:
    import pymupdf

    fonts = _font_files()
    if "body" not in fonts:
        raise SystemExit("No usable body font found; add a font path in FONT_CANDIDATES.")
    temp_path = HERE / ".build"
    if temp_path.exists():
        shutil.rmtree(temp_path)
    temp_path.mkdir(parents=True)
    font_dir = temp_path / "assets"
    font_dir.mkdir()
    # The PDF CSS uses these fixed names; copy whichever system fonts were
    # found under them so MuPDF can resolve the @font-face rules.
    pdf_font_names = {
        "body": "segoeui.ttf", "bodyb": "segoeuib.ttf", "bodyi": "segoeuii.ttf",
        "display": "georgia.ttf", "displayb": "georgiab.ttf", "mono": "consola.ttf",
    }
    for key, path in fonts.items():
        shutil.copy(path, font_dir / pdf_font_names.get(key, path.name))
    for figure in list(FIG.glob("*.svg")) + list(FIG.glob("*.png")):
        shutil.copy(figure, font_dir / figure.name)
    manual_photo = EEZ / "ManualImage.png"
    if manual_photo.exists():
        shutil.copy(manual_photo, font_dir / manual_photo.name)
    archive = pymupdf.Archive(str(font_dir))

    chapter_list = chapters(body)
    chapter_docs = []
    old_cwd = os.getcwd()
    os.chdir(FIG)
    try:
        for index, chapter in enumerate(chapter_list, start=1):
            out = temp_path / f"chapter-{index:02d}.pdf"
            doc = story_doc(_chapter_html(chapter), archive, out)
            chapter_docs.append((chapter, doc))
            print(f"  rendered chapter {index:02d}: {len(doc)} page(s)")

        body_doc = pymupdf.open()
        starts = []
        for chapter, doc in chapter_docs:
            starts.append(len(body_doc))
            body_doc.insert_pdf(doc)
        print(f"  body: {len(body_doc)} page(s)")

        howto = howto_blocks(front)
        idea = next((b for b in front if b.kind == "quote" and b.callout == "IDEA"), None)
        front_html = "<html><body>"
        if idea:
            front_html += render_callout(idea, "pdf")
        front_html += render_blocks(howto, "pdf", promote_first_h2=True)
        front_html += "</body></html>"
        howto_doc = story_doc(front_html, archive, temp_path / "front.pdf")
        print(f"  front matter: {len(howto_doc)} page(s)")
    finally:
        os.chdir(old_cwd)

    front_count = len(howto_doc) + 1  # how-to pages + contents page
    body_start = front_count + 2      # cover + front matter
    toc_page = front_count + 1
    page_numbers = [body_start + start for start in starts]

    toc_doc = pymupdf.open()
    toc_page_obj = toc_doc.new_page(width=595, height=842)
    _draw_toc(toc_page_obj, chapter_list, page_numbers, fonts)

    final = pymupdf.open()
    cover = final.new_page(width=595, height=842)
    _draw_cover(cover, fonts, COVER_LOGO)
    final.insert_pdf(howto_doc)
    final.insert_pdf(toc_doc)
    final.insert_pdf(body_doc)

    body_index = 1 + len(howto_doc) + len(toc_doc)
    for offset, (chapter, doc) in enumerate(chapter_docs):
        for page_index in range(starts[offset], starts[offset] + len(doc)):
            page = final[body_index + page_index]
            number = body_index + page_index + 1
            _page_footer(page, chapter["title"], number, fonts, None)

    toc = [[1, "Cover", 1], [1, "Contents", toc_page]]
    for chapter, number in zip(chapter_list, page_numbers):
        toc.append([1, chapter["title"], number])
    final.set_toc(toc)
    final.set_metadata({
        "title": "SafelightIO Dongle - User Manual",
        "author": "SafelightIO",
        "subject": "Darkroom exposure meter dongle, firmware 0.11 and later",
        "keywords": "darkroom, enlarger, exposure, contrast, split grade, virtual proof",
        "creator": "SafelightIO manual build",
        "producer": "PyMuPDF",
    })
    try:
        final.subset_fonts()
    except Exception as exc:
        print(f"  font subsetting skipped: {exc}")
    final.save(str(PDF_OUT), garbage=4, deflate=True)
    final.close()
    print(f"  wrote {PDF_OUT.relative_to(REPO)} ({PDF_OUT.stat().st_size} bytes, {PDF_OUT})")


def lint(markdown: str) -> list[str]:
    problems: list[str] = []
    lower = markdown.lower()
    for term in BANNED:
        if term.lower() in lower:
            problems.append(f"stale term still present: {term!r}")
    for token in ["$$", "TODO", "user_papers"]:
        if token.lower() in lower:
            problems.append(f"forbidden token: {token!r}")
    headings = re.findall(r"^#{1,2} (.*)$", markdown, re.M)
    if not any(h.startswith("15. Reference") for h in headings):
        problems.append("reference chapter is missing")
    refs = re.findall(r"[Cc]hapter (\d+)(?:\.(\d+))?", markdown)
    chapter_numbers = {h.split(".")[0] for h in headings if re.match(r"^\d+\.", h)}
    for major, minor in refs:
        if major not in chapter_numbers:
            problems.append(f"cross-reference to missing chapter {major}")
    figure_refs = re.findall(r"\]\((manual/figures/[^)]+)\)", markdown)
    for ref in figure_refs:
        if not (HERE / "figures" / Path(ref).name).exists():
            problems.append(f"missing figure: {ref}")
    if INVENTORY.exists():
        try:
            inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
        except Exception as exc:
            problems.append(f"cannot read inventory: {exc}")
        else:
            skip = {"yes", "no", "back", "low", "med", "high", "max", "auto",
                    "ilford", "foma", "agfa", "kodak", "durst", "meopta", "beseler",
                    "omega/chromega", "de vere",
                    "safelightio darkroom meter v.1.0 prototype - not for sale"}
            for entry in inventory:
                label = str(entry.get("label", "")).strip()
                cleaned = re.sub(r"\s*:\s*--\s*$", "", label).strip()
                base = re.sub(r"\s*\([^)]*\)$", "", cleaned).strip()
                base = re.sub(r"\s+(slider|button|readout)$", "", base, flags=re.IGNORECASE).strip()
                if len(base) < 4 or base.lower() in skip:
                    continue
                if base.lower() not in lower:
                    problems.append(f"UI label not covered: {cleaned!r} ({entry.get('tab')})")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the SafelightIO manual.")
    parser.add_argument("--check", action="store_true", help="run the coverage/lint checks")
    parser.add_argument("--html-only", action="store_true")
    parser.add_argument("--pdf-only", action="store_true")
    args = parser.parse_args()

    markdown = assemble_markdown()
    MD_OUT.write_text(markdown, encoding="utf-8", newline="\n")
    print(f"wrote {MD_OUT.relative_to(REPO)} ({len(markdown.splitlines())} lines)")

    blocks = parse_markdown(MD_OUT)
    front, body = split_document(blocks)
    toc = toc_data(body)
    search = search_data(body)

    if not args.pdf_only:
        html_text = build_html(front, body, toc, search)
        HTML_OUT.write_text(html_text, encoding="utf-8", newline="\n")
        print(f"wrote {HTML_OUT.relative_to(REPO)} ({HTML_OUT.stat().st_size} bytes)")

    if not args.html_only:
        try:
            build_pdf(front, body)
        except ModuleNotFoundError:
            print("PyMuPDF is not installed; PDF skipped", file=sys.stderr)
            return 1

    if args.check:
        problems = lint(markdown)
        if problems:
            print("\ncheck failed:")
            for problem in problems:
                print(f"  - {problem}")
            return 1
        print("check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
