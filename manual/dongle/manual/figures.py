#!/usr/bin/env python3
"""Generate the procedural SVG figures for the dongle manual."""
from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent / "figures"
PAPER = "#FBF8F2"
INK = "#211E1B"
MUTED = "#6D635B"
LINE = "#D9CEBF"
ORANGE = "#E8730C"
SOFT = "#F2A33A"
WHITE = "#FFFFFF"
BODY = "Segoe UI, Helvetica, Arial, sans-serif"
DISPLAY = "Georgia, Times New Roman, serif"


def svg(width: int, height: int, title: str, desc: str, body: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(desc)}">
  <title>{escape(title)}</title>
  <desc>{escape(desc)}</desc>
  {body}
</svg>
'''


def text(x, y, value, size=13, color=INK, weight="normal", anchor="start", font=BODY):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{escape(value)}</text>')


def box(x, y, w, h, fill=WHITE, stroke=LINE, rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'


def arrow(x1, y1, x2, y2):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ORANGE}" stroke-width="2.5"/>'
            f'<polygon points="{x2},{y2} {x2-10},{y2-5} {x2-10},{y2+5}" fill="{ORANGE}"/>')


def header(title, sub, width=940):
    return (f'<rect width="{width}" height="252" fill="{PAPER}"/>'
            + text(24, 40, title, 26, INK, "bold", font=DISPLAY)
            + text(24, 66, sub, 15, MUTED))


def first_session():
    steps = [
        ("1", "Connect", "Plug the dongle into", "the phone with USB-C."),
        ("2", "Allow USB", "Accept the Android", "USB permission."),
        ("3", "Choose paper", "Filter brand first,", "then the paper."),
        ("4", "Calibrate sensor", "Dark, then enlarger", "light. One-time."),
        ("5", "Calibrate paper", "One test strip sets", "the constant."),
        ("6", "Measure & print", "Zone V, Measure,", "use the time."),
    ]
    w = 1180
    out = text(24, 40, "Your first session", 26, INK, "bold", font=DISPLAY)
    out += text(24, 66, "Connect the dongle once, then make a print", 15, MUTED)
    x = 24
    for i, (num, title, l1, l2) in enumerate(steps):
        out += box(x, 92, 168, 132)
        out += f'<circle cx="{x+24}" cy="118" r="16" fill="{ORANGE}"/>'
        out += text(x + 24, 123, num, 14, WHITE, "bold", "middle")
        out += text(x + 48, 124, title, 15, INK, "bold")
        out += text(x + 16, 154, l1, 12.5, MUTED)
        out += text(x + 16, 170, l2, 12.5, MUTED)
        out += text(x + 16, 210, "one-time" if i in (3, 4) else "each session", 11, ORANGE, "bold")
        if i < len(steps) - 1:
            out += arrow(x + 170, 158, x + 183, 158)
        x += 185
    out += text(24, 244, "Steps 1–5 are setup. After that, day-to-day work is only step 6.", 13, MUTED)
    return svg(w, 252, "Your first session", "Six steps: connect, allow USB, choose paper, calibrate sensor, calibrate paper, measure", out)


def device_map():
    w, h = 940, 280
    out = f'<rect width="{w}" height="{h}" fill="{PAPER}"/>'
    out += text(24, 40, "The dongle is the meter; the phone is its screen", 24, INK, "bold", font=DISPLAY)
    out += text(24, 66, "There is no display, keypad or battery in the dongle.", 14, MUTED)
    out += box(28, 96, 250, 130)
    out += text(48, 126, "RP2350 dongle", 16, INK, "bold")
    out += text(48, 152, "sensor, USB-C,", 13, MUTED)
    out += text(48, 170, "paper catalogue,", 13, MUTED)
    out += text(48, 188, "calibration and records", 13, MUTED)
    out += text(48, 212, "no screen · no button", 11, ORANGE, "bold")
    out += arrow(286, 160, 355, 160)
    out += box(365, 96, 210, 130, "#171110", "#3A2620")
    out += text(385, 126, "USB-C + OTG", 16, "#F4E8D6", "bold")
    out += text(385, 152, "The phone is the host.", 13, "#C9A79A")
    out += text(385, 170, "Allow the USB", 13, "#C9A79A")
    out += text(385, 188, "permission once.", 13, "#C9A79A")
    out += arrow(585, 160, 654, 160)
    out += box(664, 96, 248, 130)
    out += text(684, 126, "SafelightIO app", 16, INK, "bold")
    out += text(684, 152, "Exposure · Contrast", 13, MUTED)
    out += text(684, 170, "Split · Proof · Setup", 13, MUTED)
    out += text(684, 188, "The five tools", 13, MUTED)
    out += text(684, 212, "phone screen + touch", 11, ORANGE, "bold")
    out += text(24, 260, "Unplug the dongle and the app says No meter. Your settings and the paper list stay on the dongle.", 12, MUTED)
    return svg(w, h, "Dongle and phone", "The dongle is the meter and the phone is the screen", out)


def app_map():
    w, h = 940, 360
    out = f'<rect width="{w}" height="{h}" fill="{PAPER}"/>'
    out += text(24, 40, "One screen, four places to look", 24, INK, "bold", font=DISPLAY)
    out += text(24, 66, "The same shell on every tool", 14, MUTED)
    out += box(28, 96, 250, 210)
    out += text(48, 126, "Top bar", 16, INK, "bold")
    out += text(48, 150, "SafelightIO wordmark", 13, MUTED)
    out += text(48, 168, "Meter state: No meter,", 13, MUTED)
    out += text(48, 186, "Linking, Ready fw …", 13, MUTED)
    out += text(48, 216, "Tap the state for Setup > Meter", 11, ORANGE, "bold")
    out += box(298, 96, 250, 210)
    out += text(318, 126, "Selection bar", 16, INK, "bold")
    out += text(318, 150, "Paper name", 13, MUTED)
    out += text(318, 168, "Filter brand", 13, MUTED)
    out += text(318, 196, "Opens Paper & filter", 13, MUTED)
    out += text(318, 216, "No grade here", 11, ORANGE, "bold")
    out += box(568, 96, 164, 210)
    out += text(588, 126, "Content", 16, INK, "bold")
    out += text(588, 150, "The tool", 13, MUTED)
    out += text(588, 168, "and its answer", 13, MUTED)
    out += box(748, 96, 164, 210)
    out += text(768, 126, "Bottom nav", 16, INK, "bold")
    out += text(768, 150, "Exposure", 13, MUTED)
    out += text(768, 168, "Contrast", 13, MUTED)
    out += text(768, 186, "Split", 13, MUTED)
    out += text(768, 204, "Proof", 13, MUTED)
    out += text(768, 222, "Setup", 13, MUTED)
    out += text(24, 342, "Setup is the index: Device, Calibration and Work. The five tool tabs stay at the bottom.", 12, MUTED)
    return svg(w, h, "The app shell", "Top bar, selection bar, content and bottom navigation", out)


def paper_filter():
    w, h = 940, 330
    out = f'<rect width="{w}" height="{h}" fill="{PAPER}"/>'
    out += text(24, 40, "Paper & filter: brand first, then paper", 24, INK, "bold", font=DISPLAY)
    out += text(24, 66, "The sheet no longer asks for a filter grade", 14, MUTED)
    out += box(28, 94, 500, 198)
    out += text(48, 120, "Paper & filter", 18, INK, "bold", font=DISPLAY)
    out += f'<rect x="48" y="136" width="456" height="44" rx="12" fill="#240000"/>'
    out += text(70, 164, "Ilford", 13, "#FF0000", "bold")
    out += f'<rect x="196" y="136" width="82" height="44" rx="12" fill="#FF0000"/>'
    out += text(237, 164, "Ilford", 13, "#000000", "bold", "middle")
    out += text(292, 164, "Foma", 13, "#FF0000")
    out += text(370, 164, "Kodak", 13, "#FF0000")
    out += text(48, 204, "Paper", 12, "#FF0000", "bold")
    for y, name, count in [(214, "Ilford", "3 papers"), (250, "Foma", "1 paper")]:
        out += f'<rect x="48" y="{y}" width="456" height="32" rx="8" fill="#FFFFFF" stroke="{LINE}"/>'
        out += text(64, y + 21, name, 13, INK, "bold")
        out += text(446, y + 21, count, 11, MUTED)
    out += box(552, 94, 360, 198)
    out += text(572, 120, "Where the grade lives", 18, INK, "bold", font=DISPLAY)
    out += text(572, 148, "Filter grade is set on Exposure,", 13, MUTED)
    out += text(572, 166, "not in this sheet.", 13, MUTED)
    out += f'<rect x="572" y="184" width="320" height="44" rx="12" fill="{PAPER}" stroke="{LINE}"/>'
    out += text(590, 212, "Filter Grade Transform", 13, INK, "bold")
    out += text(572, 252, "The bar shows the paper and the", 13, MUTED)
    out += text(572, 270, "brand, never the grade.", 13, MUTED)
    out += text(24, 314, "The dongle owns the catalogue. With no meter connected the sheet shows its empty state.", 12, MUTED)
    return svg(w, h, "Paper and filter sheet", "Filter brand rail above collapsible paper brands", out)


def exposure_flow():
    w, h = 940, 220
    out = f'<rect width="{w}" height="{h}" fill="{PAPER}"/>'
    out += text(24, 40, "Exposure: one zone, one reading, one time", 24, INK, "bold", font=DISPLAY)
    out += text(24, 66, "Swipe the zone rail, then measure the easel", 14, MUTED)
    labels = [("1", "Choose the zone", "Swipe or tap the rail.", "Zone V is the usual start."),
              ("2", "Measure the easel", "Tap Measure.", "The dongle reads the spot."),
              ("3", "Read the time", "The answer is seconds.", "Use the suggested grade.")]
    x = 24
    for num, title, l1, l2 in labels:
        out += box(x, 94, 270, 102)
        out += f'<circle cx="{x+24}" cy="120" r="16" fill="{ORANGE}"/>'
        out += text(x + 24, 125, num, 14, WHITE, "bold", "middle")
        out += text(x + 48, 126, title, 16, INK, "bold")
        out += text(x + 16, 154, l1, 13, MUTED)
        out += text(x + 16, 172, l2, 13, MUTED)
        if x < 600:
            out += arrow(x + 286, 145, x + 310, 145)
        x += 316
    out += text(24, 214, "The answer never wraps: a long time shrinks just enough to stay on one line, and the panel keeps its height.", 12, MUTED)
    return svg(w, h, "Exposure flow", "Choose a zone, measure, read the time", out)


def contrast_flow():
    w, h = 940, 220
    out = f'<rect width="{w}" height="{h}" fill="{PAPER}"/>'
    out += text(24, 40, "Contrast: two spots, one time and one grade", 24, INK, "bold", font=DISPLAY)
    out += text(24, 66, "Measure the dim highlight and the bright shadow", 14, MUTED)
    labels = [("1", "Highlights", "Dim spot at easel.", "Tap Measure."),
              ("2", "Shadows", "Bright spot at easel.", "Tap Measure."),
              ("3", "Answer", "Time and suggested", "grade, side by side.")]
    x = 24
    for num, title, l1, l2 in labels:
        out += box(x, 94, 270, 102)
        out += f'<circle cx="{x+24}" cy="120" r="16" fill="{ORANGE}"/>'
        out += text(x + 24, 125, num, 14, WHITE, "bold", "middle")
        out += text(x + 48, 126, title, 16, INK, "bold")
        out += text(x + 16, 154, l1, 13, MUTED)
        out += text(x + 16, 172, l2, 13, MUTED)
        if x < 600:
            out += arrow(x + 286, 145, x + 310, 145)
        x += 316
    out += text(24, 214, "Fine tune holds the trims and the burn. Reset puts every trim and the burn back to neutral.", 12, MUTED)
    return svg(w, h, "Contrast flow", "Two readings produce a time and a suggested grade", out)


def proof_grid():
    w, h = 940, 300
    out = f'<rect width="{w}" height="{h}" fill="{PAPER}"/>'
    out += text(24, 40, "Virtual Proof: a grid of the print", 24, INK, "bold", font=DISPLAY)
    out += text(24, 66, "Each cell is one meter reading; tap a cell to see its values", 14, MUTED)
    x0, y0, cw, ch = 60, 96, 110, 54
    for r in range(4):
        for c in range(5):
            idx = r * 5 + c
            fill = {4: "#C8C8C8", 6: "#8E8E8E", 7: "#595959", 8: "#D8D8D8"}.get(idx, "#ECECEC")
            out += f'<rect x="{x0+c*cw}" y="{y0+r*ch}" width="{cw-3}" height="{ch-3}" fill="{fill}" stroke="#B9AD9F"/>'
            if idx == 4:
                out += f'<rect x="{x0+c*cw}" y="{y0+r*ch}" width="{cw-3}" height="{ch-3}" fill="none" stroke="#FF0000" stroke-width="4"/>'
            if idx == 12:
                out += f'<rect x="{x0+c*cw}" y="{y0+r*ch}" width="{cw-3}" height="{ch-3}" fill="none" stroke="{ORANGE}" stroke-width="4"/>'
            out += text(x0 + c * cw + 8, y0 + r * ch + 18, str(idx), 10, "#211E1B")
    out += box(650, 96, 266, 164)
    out += text(670, 124, "The frames", 16, INK, "bold")
    out += text(670, 150, "Red: selected cell", 13, MUTED)
    out += text(670, 170, "Orange: next cell", 13, MUTED)
    out += text(670, 190, "Dark red: Zone V", 13, MUTED)
    out += text(670, 210, "Bright/dim edge: clipping", 13, MUTED)
    out += text(24, 272, "Start scan fills the grid; Set V Zone anchors it; Clear Grid starts again.", 12, MUTED)
    return svg(w, h, "Virtual proof grid", "A five-column proof grid with selected, next and reference cells", out)


def calibration():
    w, h = 940, 300
    out = f'<rect width="{w}" height="{h}" fill="{PAPER}"/>'
    out += text(24, 40, "Paper calibration in one test strip", 24, INK, "bold", font=DISPLAY)
    out += text(24, 66, "Find the patch that matches the reference midtone", 14, MUTED)
    labels = ["too light", "light", "correct", "dark", "too dark"]
    fill = ["#F4F1EA", "#D8D2C7", "#8D8880", "#4C4945", "#1D1C1B"]
    for i, (lab, col) in enumerate(zip(labels, fill)):
        x = 50 + i * 110
        out += f'<rect x="{x}" y="104" width="96" height="88" fill="{col}" stroke="#B9AD9F"/>'
        out += text(x + 48, 214, lab, 12, INK if lab == "correct" else MUTED, "bold" if lab == "correct" else "normal", "middle")
    out += f'<rect x="270" y="98" width="112" height="100" fill="none" stroke="{ORANGE}" stroke-width="4"/>'
    out += text(326, 92, "choose this", 12, ORANGE, "bold", "middle")
    out += box(620, 96, 290, 170)
    out += text(640, 124, "Enter two numbers", 16, INK, "bold")
    out += text(640, 152, "Known lux: the light on", 13, MUTED)
    out += text(640, 170, "the strip during the test.", 13, MUTED)
    out += text(640, 198, "Known time: the exposure", 13, MUTED)
    out += text(640, 216, "that produced the midtone.", 13, MUTED)
    out += text(640, 246, "The dongle does the division.", 12, ORANGE, "bold")
    out += text(24, 282, "Calibrate the sensor first: dark, then enlarger light. The paper calibration is one-time per paper and filter.", 12, MUTED)
    return svg(w, h, "Paper calibration", "A five-patch test strip and the two numbers to enter", out)


def update_flow():
    w, h = 940, 250
    out = f'<rect width="{w}" height="{h}" fill="{PAPER}"/>'
    out += text(24, 40, "Firmware update: no BOOTSEL button needed", 24, INK, "bold", font=DISPLAY)
    out += text(24, 66, "The 1200-baud touch asks the running firmware to enter the ROM bootloader", 14, MUTED)
    labels = [("1", "Open the port", "1200 baud from any", "serial terminal."),
              ("2", "RP2350 appears", "The dongle re-enumerates", "as a USB drive."),
              ("3", "Copy the UF2", "Drop the new firmware", "onto the drive."),
              ("4", "Wait", "The drive disappears", "and the app reconnects.")]
    x = 24
    for num, title, l1, l2 in labels:
        out += box(x, 94, 210, 104)
        out += f'<circle cx="{x+24}" cy="120" r="16" fill="{ORANGE}"/>'
        out += text(x + 24, 125, num, 14, WHITE, "bold", "middle")
        out += text(x + 48, 126, title, 15, INK, "bold")
        out += text(x + 16, 156, l1, 12.5, MUTED)
        out += text(x + 16, 174, l2, 12.5, MUTED)
        if x < 730:
            out += arrow(x + 218, 146, x + 238, 146)
        x += 232
    out += text(24, 234, "No SDK, Picotool or button. A failed update can leave the app unbootable; keep the cable connected until the drive disappears.", 12, MUTED)
    return svg(w, h, "Firmware update flow", "1200-baud touch, RP2350 drive, copy UF2, wait", out)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    figures = {
        "fig-first-session.svg": first_session(),
        "fig-device-map.svg": device_map(),
        "fig-app-map.svg": app_map(),
        "fig-paper-filter.svg": paper_filter(),
        "fig-exposure-flow.svg": exposure_flow(),
        "fig-contrast-flow.svg": contrast_flow(),
        "fig-proof-grid.svg": proof_grid(),
        "fig-calibration.svg": calibration(),
        "fig-firmware-update.svg": update_flow(),
    }
    for name, payload in figures.items():
        (OUT / name).write_text(payload, encoding="utf-8")
        print(f"wrote {OUT / name}")


if __name__ == "__main__":
    main()
