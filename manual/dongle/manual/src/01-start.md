# SafelightIO Dongle — User Manual

**USB darkroom exposure meter · Android app · Firmware 0.11 and later · First edition, November 2026**

> [!IDEA] The one idea
> The meter measures the light on your easel and turns it into a printing time:
> **light × your paper's constant = seconds**. Every tool is built on that one
> number. Once your paper is calibrated, any new reading becomes a time
> immediately.

![The Exposure screen in the SafelightIO Android app](manual/figures/hero-app.png)

*The phone is the dongle's screen. The screenshots in this manual show the app
at its darkroom brightness; the labels match the current app and firmware 0.11.*

## How to use this manual

There are three ways in:

| If you want to… | Start at |
|---|---|
| Connect the dongle and make a first print | **1. Start here** |
| Look up one control you can see on screen | **15. Reference → Index of controls** |
| Fix a problem | **13. Messages and troubleshooting** |

The manual follows the product: first the dongle and the app shell, then the five
tools, then Setup and the jobs that need several steps (paper calibration,
files, firmware updates).

**Words in this manual.** A **control** is something you tap, drag or type into.
A **readout** is a number or message the app shows you. Names printed in
**bold** match the labels on screen. The dongle has no display: every screen in
this manual is on the Android phone.

> [!TIP] Reading in the darkroom
> The HTML edition (open `MANUAL.html` in a browser) has a **Darkroom** button
> that switches to red-on-black. Use it on a phone or tablet beside the
> enlarger.

> [!NOTE] The dongle owns the data
> The paper catalogue, the calibration, the filter brand and grade, the trims
> and the session settings live on the dongle. The app reads them on every
> connection. There is no bundled paper list in the app, and no file is loaded
> at launch. If the app says **Connect the meter to list papers**, the paper
> list is simply not available until the dongle answers.

## Contents

1. **Start here** — what the dongle does, the first session, the five tools
2. **The app at a glance** — top bar, selection bar, sheet, Setup, connection
3. **Exposure** — zone, measure, time, grade and burn
4. **Contrast** — two readings, one time and a suggested grade
5. **Split Grade** — a soft leg and a hard leg, added together
6. **Virtual Proof** — preview the print and check the enlarger's evenness
7. **Setup** — Meter, Paper & filter, Calibration, Sensor, Help and About
8. **Tools & data** — paper editor, estimate and backups
9. **Saving, loading and storage** — settings, sessions, phone files and dongle memory
10. **Calibrating a paper** — the one-time job that makes the times accurate
11. **The paper and filter database** — what the dongle holds and how to add a paper
12. **Filter factors** — why a filter costs time, and how to measure yours
13. **Messages and troubleshooting** — what the app is telling you
14. **Firmware updates** — 1200-baud touch, UF2, and what to do if it fails
15. **Reference** — ranges, defaults, glossary, index and cheat sheet

---

# 1. Start here

## 1.1 What the dongle does

The SafelightIO dongle is a small USB-C light meter. One end plugs into the
phone; the other end carries the light sensor. It measures the light on the
easel and works out how long to expose the paper.

It is the same metering engine as the 7-inch SafelightIO, without the screen.
The dongle has:

- the TSL2591 light sensor and its dark/light calibration;
- the RP2350 processor running the same exposure, contrast and split-grade
  arithmetic;
- the paper catalogue, the filter brands and grades, and the paper constants;
- the per-paper trims and burn records;
- USB-C, which carries both power and the text protocol.

It has **no display, no battery and no BOOTSEL button**. The phone supplies the
screen, the keyboard and the touch input. The dongle supplies the measurement.
A computer is not needed to use the meter; a computer is needed only for a
firmware update.

![The dongle is the meter; the phone is the screen](manual/figures/fig-device-map.svg)

## 1.2 The one thing that makes it accurate

A light reading on its own is not a printing time. The meter needs to know what
your paper and developer do with that light. The **paper calibration** is the
bridge: one test strip gives the dongle two numbers, and it multiplies them
to get the paper's constant.

After that, the answer is just multiplication. The dongle does it; the app shows
it. The phone never does the metering arithmetic and never needs a network
connection.

## 1.3 What you need

- An Android phone with USB-C and USB host (OTG) support.
- The SafelightIO Android app installed on the phone.
- The SafelightIO dongle.
- A USB-C cable or a USB-C OTG adapter that passes data, not just power.
- Your paper, your filter brand and a test strip for the paper calibration.
- Optional: a computer and a USB cable for firmware updates.

> [!IMPORTANT] The cable matters
> Use a data cable. A charge-only cable can power the dongle but the app will
> never see it. If the phone offers a USB permission dialog, choose **Allow**.

## 1.4 Your first session

![First session: six steps](manual/figures/fig-first-session.svg)

| Step | What you do | Where |
|---|---|---|
| 1 | Plug the dongle into the phone | USB-C |
| 2 | Allow the USB permission | Android dialog |
| 3 | Choose the filter brand and the paper | **Paper & filter** sheet |
| 4 | Calibrate the sensor: dark, then enlarger light | **Setup → Sensor → Sensor Calibration** |
| 5 | Calibrate the paper with one test strip | **Setup → Calibration** or **Tools & data → Estimate Calibration** |
| 6 | Measure the easel and print | **Exposure** |

Steps 4 and 5 are one-time jobs per device and paper. Step 3 is repeated when
you change paper. Step 6 is the everyday job.

### Step 1 — Connect the dongle

Plug the dongle into the phone. Android asks whether to allow the app to access
the USB device; choose **Allow**. The app's top bar moves from **No meter** to
**Linking**, then to **Ready · fw 0.11** (your firmware version may be newer).

If the app says **No meter** and no dialog appears, unplug the dongle, check that
the cable is a data cable, and plug it in again. On some phones the USB mode
must be set to **File transfer / MTP** or **USB controlled by this device**; the
app will show the permission dialog either way.

### Step 2 — Choose the paper and filter

Tap the selection bar under the top bar: it reads **No paper | No filter** until
something is chosen. The **Paper & filter** sheet opens.

1. Choose the **Filter brand** in the rail at the top.
2. Open the paper brand's row and choose the paper.

The sheet does not ask for a filter grade. The grade is chosen on **Exposure**
because it belongs to the exposure, not to the paper selection.

With no meter connected, the sheet says **Connect the meter to list papers**.
That is not an error: the list is on the dongle.

### Step 3 — Choose the zone

On **Exposure**, the zone rail is already at **Zone V**, the usual starting
point. Swipe the rail or tap a neighbouring zone to change it. The selected
value settles in the centre; the app shows **zone V** in the line under the
answer.

### Step 4 — Calibrate the sensor

Open **Setup → Sensor → Sensor Calibration**. Do **Calibrate Dark** with
the sensor covered, then **Calibrate Enlarger Light** with the enlarger on and
the sensor in the light. This is the sensor's zero and its reference; it is one
of the two calibrations that make the lux numbers trustworthy.

### Step 5 — Calibrate the paper

Open **Setup → Calibration** and enter the **Known lux** and **Known time**
from a test strip, or use **Setup → Tools & data → Estimate Calibration** to
estimate the pair. Follow the steps in chapter 10. The dongle stores the paper's
constant; the app reads it back on every connection.

### Step 6 — Measure and print

Return to **Exposure**. Put the sensor on the easel, tap **Measure**, and read
the time. Set the enlarger to that time, with the suggested filter grade, and
make the print.

> [!TIP] The first print is a starting point
> The meter predicts; the strip confirms. If the print is consistently too light
> or too dark, check the paper calibration before changing the meter's answer.

## 1.5 The five tools at a glance

| Tool | What it answers | What you do |
|---|---|---|
| **Exposure** | One printing time for the easel reading | Choose a zone, Measure, use the time and grade |
| **Contrast** | A time and a suggested grade from a highlight and a shadow | Measure the dim spot, then the bright spot |
| **Split** | A soft time and a hard time for a two-filter print | Measure the same two spots; use the pair |
| **Proof** | A grid of the print, and optionally the enlarger's evenness | Scan the grid, tap cells, read the verdict |
| **Setup** | Device, calibration, sensor, files and help | Open the page you need |

Every tool starts with its answer at the top of the screen. If there is no
answer yet, the answer area says so and tells you which measurement is missing.

---

# 2. The app at a glance

## 2.1 The shell

Every tool uses the same shell:

- **Top bar:** the SafelightIO wordmark on the left and the meter state on the
  right. The state is **No meter**, **Linking**, **Ready · fw …** or a short
  error. Tap it to open **Setup → Meter**.
- **Selection bar:** the paper on the left and the filter brand on the right.
  Tap it to open **Paper & filter**. This is the only place the paper and brand
  are chosen.
- **Content:** the current tool. The answer, the controls and the reference cards
  live here.
- **Bottom navigation:** **Exposure**, **Contrast**, **Split**, **Proof** and
  **Setup**. The active item has a tonal capsule.

![The app shell: top bar, selection bar, content and bottom navigation](manual/figures/fig-app-map.svg)

The app hides the Android status bar while it is in front. The page background
runs to the top of the screen, so there is no black strip above the interface.

## 2.2 The Paper & filter sheet

The sheet has two sections:

1. **Filter brand** at the top, as a horizontal rail. Choose the brand before
   the paper: the brand determines which paper rows and which grades are valid.
2. **Paper** below it, one collapsible row per manufacturer. The row shows the
   paper count; open it and choose the paper. The paper in force is marked
   **In use**.

![Paper & filter: brand first, then the paper](manual/figures/fig-paper-filter.svg)

There is **no filter grade in this sheet**. The grade is a property of the
exposure and is chosen in **Filter Grade Transform** on the Exposure screen.
This is deliberate: a grade chosen while picking paper would be a second,
competing authority for the same number.

> [!NOTE] What the selection bar shows
> The bar shows the paper and the filter brand — for example
> **Ilford MGT Cooltone | Ilford**. It never shows a grade. If no brand is in
> force it reads **No filter**.

## 2.3 Setup is the index

Tap **Setup** in the bottom navigation. The index has three groups:

| Group | Pages |
|---|---|
| **Device** | **Meter**, **Paper & filter** |
| **Calibration** | **Calibration**, **Sensor** |
| **Work** | **Tools & data**, **Help & messages**, **About** |

The index is not a settings dump. Each row opens a page with one job. The
**Meter** page reports the connection and firmware; **Paper & filter** opens
the same sheet as the selection bar; **Calibration** is the paper's two
numbers; **Sensor** is gain, integration time, averaging and the Sensor Calibration card.

## 2.4 Connecting, reconnecting and the USB permission

The dongle is a USB device. The first connection raises Android's permission
dialog. After that, the app can reopen the port when the dongle is plugged in
again.

| Top bar says | Meaning |
|---|---|
| **No meter** | No dongle is attached, or Android has not granted access |
| **Linking** | The app is opening the port and waiting for `HELLO` |
| **Ready · fw 0.11** | The dongle answered; the app is reading its catalogue and settings |
| A short error | The port opened but the dongle did not answer, or the firmware refused |

If the state stays on **No meter**, open **Setup → Meter** and use **Reconnect**.
If that fails, unplug and replug the dongle. If the phone has a USB mode switch,
set it to allow the connected device.

> [!IMPORTANT] One app, one dongle
> Close any other app that is holding the USB port. Android gives the port to
> one app at a time. The SafelightIO app will show **No meter** if another app
> owns it.

## 2.5 What the dongle keeps and what the phone keeps

The dongle keeps the things that belong to the meter:

- the paper and filter catalogue;
- the paper calibrations;
- the filter brand and grade in force;
- the sensor gain, integration time and averaging;
- the per-paper trims and burn;
- the trims and burn the app writes back while you work.

The phone keeps:

- the app itself;
- the saved settings and session files in the Data Manager;
- the screen and the reader's current view.

The app is not a copy of the dongle. If you connect the same dongle to another
phone, the catalogue and calibrations are still there; the files on the old
phone are not.

---

# 3. Exposure

## 3.1 The screen

![Exposure: the answer, the zone rule and the controls](manual/figures/screen-exposure.png)

From top to bottom:

1. **No reading** (or the time) in the answer well. Under it, one line of
   conditions: **burn**, **grade**, **zone**.
2. A **zone rule** with a dot at the selected zone. It is a picture of where the
   reading sits on the 0–X scale, not a second control.
3. **Measure** — the one action. It is disabled when the dongle is not ready.
4. **Exposure Calculator** — the zone rail, the **Lux reading** and the
   **Calibration constant**.
5. **Filter Grade Transform** — the grade rail, or the reason there is no
   grade.
6. **Dodge & Burn** — the burn slider.

The answer well keeps the same height even when a long time shrinks to fit, or
when the conditions line wraps to two lines. The controls below do not jump.

## 3.2 Every control and readout

### Zone rail

**Zone of measurement** is a horizontal snap rail from **0** to **X**. The
selected zone sits in the centre; the neighbouring zones peek in at the edges.
Swipe the rail or tap a neighbour. The rail snaps to a whole zone, the dongle
saves it, and the app recomputes the answer from the stored reading.

### Lux reading

The illuminance the dongle measured, in lux. It is the number the time is
computed from. When no reading has been taken, it shows **—**.

### Calibration constant

The paper's constant, as the dongle holds it. It is the "known lux × known
time" product of the paper calibration, not a value you type here.

### Measure

One tap starts a `SENSOR` read, stores it as the exposure reading, and asks the
dongle to compute. While the dongle is working, the last answer stays on screen
and the button is disabled.

### Filter Grade Transform

The grade rail shows the grade tokens the dongle's table holds for the selected
paper and filter brand. A grade is a request, not a local choice: the app sends
`FILTER brand= grade=` and the meter answers. The line below the rail explains
the current state:

- **No filter grade — the time is the unfiltered one**;
- **No filtration — the time is the unfiltered one**;
- **Grade 2xM1 — the factor is the meter's**.

If there is no table for the paper and brand, the card says
**No grade table for this paper and filter brand** instead of drawing an empty
rail.

### Dodge & Burn

A symmetric slider: the lit span runs from the centre to the thumb, and the
default middle position has no fill. The value is in quarter stops. This is the
one trim on Exposure; the four trims live on Contrast and Split.

## 3.3 Step by step

![Exposure: choose a zone, measure, read the time](manual/figures/fig-exposure-flow.svg)

1. Confirm the top bar says **Ready**.
2. Choose the paper and filter brand from the selection bar.
3. Swipe the zone rail to the zone you are metering; **V** is the usual start.
4. Put the sensor on the easel and tap **Measure**.
5. Read the time. Set the enlarger and the filter grade; the grade is the
   suggested one in the answer line.
6. If the print needs a little more or less, use **Dodge & Burn** and measure
   again, or adjust the trim on Contrast.

## 3.4 The zone list

The rail runs 0 to X because those are the meter's own numbers.

| Zone | What it represents |
|---|---|
| **0** | The black end: deep shadow with texture |
| **I–III** | The low values |
| **IV** | A darker midtone |
| **V** | Middle grey: the standard metering target |
| **VI** | A lighter midtone |
| **VII–IX** | The high values |
| **X** | The white end: a specular or paper-base highlight |

Meter the tone you want to print as middle grey. If you meter a highlight, the
time will make that highlight middle grey, which is usually not what you want.

## 3.5 What the filter grade does

A variable-contrast filter changes the paper's speed as well as its contrast.
The dongle knows the factor for each grade in its table, so the time already
includes the filter. You do not multiply by a filter factor yourself.

The grade is independent of the zone. The zone chooses which tone becomes
middle grey; the grade chooses the contrast. Changing one does not silently
change the other.

## 3.6 Dodge and burn

The burn slider is a **bias**: it shifts the whole exposure, not a local dodge.
It is measured in quarter stops and is symmetric around zero. Use it when the
print is consistently a little light or dark but the contrast is right.

The four trims on Contrast and Split are the per-print adjustments: exposure,
contrast, highlights and shadows. They are saved per paper and per tool.

## 3.7 A worked example

Suppose the meter says **12.40 s**, **grade 2xM1**, **zone V**. Set the enlarger
to 12.4 seconds and the filter to the 2xM1 grade. Make the print.

If the print is slightly light across the whole image, open **Dodge & Burn** and
move one step toward **+** (a quarter stop). If the contrast is right but the
highlights are blocked, use the **Highlights** trim on Contrast instead. The
trim is the more surgical control; the burn is the global one.

## 3.8 Common questions

**The time is blank.** The dongle has not answered a compute yet. Measure, or
check that the paper has a calibration.

**The time says calibrate.** The paper has no calibration constant. Calibrate
the paper (chapter 10).

**The grade rail is missing.** The paper and brand have no grade table; the
card says so. Try another brand, or edit the paper in the Paper & Filter Editor.

**The app says No meter.** Check the cable and the Android USB permission; open
**Setup → Meter → Reconnect**.

---
