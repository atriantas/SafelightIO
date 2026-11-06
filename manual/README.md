# SafelightIO manuals

Two illustrated manuals in the same voice and layout, plus one selector page.

| Path | What it is |
|---|---|
| `MANUAL.html` | The device selector. Open this first. |
| `7-inch/MANUAL.html` | The 7-inch touchscreen edition (self-contained HTML). |
| `7-inch/MANUAL.md` | The 7-inch canonical Markdown. |
| `7-inch/SafelightIO — User Manual.pdf` | The 7-inch print edition. |
| `dongle/MANUAL.html` | The dongle + Android app edition (self-contained HTML). |
| `dongle/MANUAL.md` | The dongle canonical Markdown. |
| `dongle/SafelightIO Dongle — User Manual.pdf` | The dongle print edition. |
| `dongle/manual/src/` | The dongle's four Markdown source chapters. |
| `dongle/manual/figures/` | The dongle's screenshots and procedural SVG figures. |
| `dongle/manual/figures.py` | Generates the procedural dongle figures. |
| `dongle/manual/build.py` | Assembles the dongle Markdown, HTML and PDF. |
| `7-inch/manual/src/` | A copy of the 7-inch source chapters. |
| `7-inch/manual/figures/` | A copy of the 7-inch figures, so the Markdown images resolve. |

## Where the site points

The main site's **Manual** menu offers the two editions directly and links to
`MANUAL.html` for the full list (HTML, PDF and Markdown). The mobile menu has the
same three entries, and the footer links all three pages. `MANUAL.html` links back
to the site with **← Main site**.

## Build the dongle edition

The builder needs Python 3 and PyMuPDF for the PDF. The HTML and Markdown are
written even if PyMuPDF is absent; only the PDF step stops.

```sh
python3 -m venv .venv
.venv/bin/pip install pymupdf
cd dongle/manual
python3 figures.py
python3 build.py --check
```

Outputs:

- `dongle/MANUAL.md`
- `dongle/MANUAL.html`
- `dongle/SafelightIO Dongle — User Manual.pdf`

The build uses the same cream/ink/orange CSS, callouts, TOC, search, darkroom
toggle and print layout as the 7-inch edition. The selector page is static and
does not need a build step.

## Editing rules

- Edit `dongle/manual/src/*.md`, then rebuild; do not edit `dongle/MANUAL.md` by
  hand.
- Re-run `figures.py` only when a procedural figure changes. Screenshots are
  copied from `android/screenshots/redesign/`.
- The dongle has no display, no battery and no BOOTSEL button; the manual
  describes the Android app as its screen and the 1200-baud/UF2 update path.
- The 7-inch files are a copy of the existing edition. Its source remains
  available in the 7-inch project; do not edit the copy.

## Adding the hardware photo

The dongle edition intentionally uses app screenshots and diagrams until a photo
of the enclosed dongle exists. When it arrives:

1. Put it in `dongle/manual/figures/` (for example `dongle-hardware.png`).
2. Replace the hero image in `dongle/manual/build.py` if you want it on the
   cover, and add it to the hardware section of `src/01-start.md`.
3. Rebuild the dongle edition.

## File policy

The HTML editions embed their images as data URIs. They can be opened directly
from disk without a web server. The Markdown editions keep relative links under
each device's `manual/figures/` folder.
