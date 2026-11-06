# SafelightIO — User Manual

**Digital darkroom exposure meter · Firmware 1.0 · Second edition, October 2026**

> [!IDEA] The one idea
> The meter measures the light on your easel and turns it into a printing time:
> **light × your paper's constant = seconds**. Every tool in the device is built on
> that one number. Once your paper is calibrated, any new light reading becomes a
> time immediately.

![The SafelightIO on its easel](ManualImage.png)

*Prototype hardware. The screen in this photo shows an early build; the labels in
this manual are the ones you will see on firmware 1.0.*

## How to use this manual

There are three ways in:

| If you want to… | Start at |
|---|---|
| Set the meter up and make a first print | **1. Start here** |
| Look up one control you can see on screen | **15. Reference → Index of controls** |
| Fix a problem | **13. Messages, Help Center and troubleshooting** |

The manual follows the device: first the screen, then the five tabs, then the
sidebar, then the jobs that need several steps (calibration, saving, updates).

**Words in this manual.** A **control** is something you tap, drag or type into.
A **readout** is a number or message the device shows you. Names printed in
**bold** match the labels on screen. The device is a small screen in a darkroom,
so labels are often abbreviated; the full name is given the first time.

> [!NOTE] The Help Center is on the device
> The **Help** button at the bottom of the sidebar opens the **Help Center**: seven
> short tabs (Start, Settings, Exposure, Contrast, Split Grade, Virtual Proof and
> Paper Editor), a QR code to the project page, and the support address shown on the
> Start tab (**support@cyanowood.com**). Use it when
> you are standing at the enlarger and need a reminder.
>
> The Help Center is a quick reminder. This manual is the complete, current
> reference. If a Help page and this manual disagree, trust this manual.

> [!TIP] Reading in the darkroom
> The HTML edition (open `MANUAL.html` in a browser) has a **Darkroom** button that
> switches to red-on-black. Use it on a phone or tablet beside the enlarger.

## Contents

1. **Start here** — what the meter does, the first session, the five tools
2. **The screen at a glance** — tabs, content area, sidebar, splash, confirmations
3. **Exposure** — measure the easel and get a time
4. **Contrast** — read the negative and choose a grade
5. **Split Grade** — two filters, two exposures, one print
6. **Virtual Proof** — preview the print, and check the enlarger's evenness
7. **Control Panel** — filter data, estimates, saving, sensor calibration
8. **Settings sidebar** — paper, sensor, brightness and battery
9. **Saving, loading and storage** — SD card, flash, backups, sessions
10. **Calibrating a paper** — the fifteen minutes that make the meter accurate
11. **The paper and filter database** — what is built in, and how to add your own
12. **Filter factors** — why a filter costs time, and how to measure yours
13. **Messages, Help Center and troubleshooting** — what the device is telling you
14. **Firmware updates** — updating safely, and what is kept
15. **Reference** — ranges, defaults, glossary, index, one-page cheat sheet

---

# 1. Start here

## 1.1 What the meter does

SafelightIO is a light meter for black-and-white enlarger printing. You put its
sensor where the print will be, press **Measure LUX**, and it tells you how many
seconds to expose the paper. It can also:

- recommend a **contrast filter grade** from two readings of the negative;
- work out a **split-grade** soft + hard exposure;
- paint a **preview grid** of the print from a series of readings;
- check that the enlarger's light is **even** across the easel.

It is not a densitometer and not a colour analyser. It measures the light that
actually falls on the easel, which is what the paper responds to.

## 1.2 The one thing that makes it accurate

The meter needs one number from you: how sensitive **your** paper is under **your**
enlarger. You find it once, with one test strip, and type the result into the
device. That is **paper calibration** (chapter 10). After that, every reading
becomes a time.

A meter that has not been calibrated for the selected paper cannot give a time. It
will show **`calibrate`** instead. This is normal, not an error.

## 1.3 What you need

- The meter, charged or plugged in.
- Your enlarger, focused at the height and aperture you will print at.
- A sheet of the paper you intend to use, for the calibration test strip.
- A darkroom (or a very dark room) for the sensor's dark calibration.
- Optional: a microSD card. It keeps settings, papers and sessions on removable
  storage and makes backups easy.

## 1.4 Your first session

![First session: five steps](manual/figures/fig-first-session.svg)

| Step | What you do | Where | Time |
|---|---|---|---|
| 1 | Charge, power on, wait for the main screen | USB-C / power | 2 min |
| 2 | Choose **Paper Brand**, **Paper Type** and **Filter Brand** | Sidebar | 1 min |
| 3 | Calibrate the sensor: **Calibrate Dark**, then **Calibrate Light** | **Control Panel** tab | 10 min |
| 4 | Calibrate the paper with one test strip | Chapter 10 | 15 min |
| 5 | Measure the easel and print | **Exposure** tab | 1 min |

Steps 3 and 4 are one-time jobs per device/paper. You do not repeat them for every
print.

> [!IMPORTANT] Do the steps in this order
> The sensor calibration makes the lux numbers trustworthy. The paper calibration
> turns lux into seconds. Skipping the sensor step still gives a time, but it may be
> consistently too long or too short; skipping the paper step gives no time at all.

### Step 1 — Power on

Connect USB-C to charge if the battery is low. Press the power button; the splash
screen appears with a photography quote, a darkroom tip, the firmware banner
(**SafelightIO Darkroom Meter v.1.0**, **Prototype - Not for Sale**) and the serial
number. After a few seconds the main screen opens.

The backlight is deliberately dim while the device boots, then returns to your
saved brightness. If the screen looks almost black, see **Brightness** in chapter 8
before assuming the meter is broken.

### Step 2 — Choose the paper and filter

In the sidebar, set:

- **Filter Brand** — the brand of contrast filters in your enlarger (for example
  Ilford or FOMA). It changes the grade names and the built-in filter factors.
- **Paper Brand** and **Paper Type** — the paper in the easel.

Changing the paper reloads that paper's calibration and trims, and resets the
dodge/burn slider. Choose the paper before you measure, not after.

### Step 3 — Calibrate the sensor

Open the **Control Panel** tab and find **SENSOR CALIBRATION**:

1. **Calibrate Environment Noise** → **Calibrate Dark**, in total darkness.
2. **Calibrate Enlarger Light** → **Calibrate Light**, with the enlarger on and the
   sensor in steady light.

The full procedure, including the two-phase light calibration, is in section 7.4.
Do this once per device; repeat it if readings disagree between gain settings or
after a firmware update that changes the sensor settings.

### Step 4 — Calibrate the paper

Follow chapter 10. You will make one test strip, choose the correctly exposed
midtone, and enter its lux reading and time. The device computes the paper's
constant. From then on, the **Exposure** tab gives times for that paper.

### Step 5 — Measure and print

Open **Exposure**, choose the zone you measured (usually **V**), press **Measure
LUX**, and read the time. Chapter 3 explains every control on that tab.

## 1.5 The five tools at a glance

| Tab | Answers the question | Use it when |
|---|---|---|
| **Exposure** | “How long do I expose this print?” | You have a normal negative and want a time |
| **Contrast** | “Which grade does this negative need?” | The negative looks flat or contrasty |
| **Split Grade** | “What soft and hard exposures make this print?” | You want to control highlights and shadows separately |
| **Virtual Proof** | “What will the print look like across the easel?” | The negative is uneven, or you want to see before committing paper |
| **Control Panel** | “How is the meter set up?” | Filter data, paper estimates, saving, sensor calibration |

The **Enlarger mode** switch lives inside Virtual Proof; it turns the same grid into
a light-evenness test (section 6.5).

---

# 2. The screen at a glance

![The real Exposure screen, annotated: five tabs, content area, sidebar, battery and brightness, Help and firmware version](manual/figures/screen-map-annotated.png)

The annotated screen above names the three parts. Each tool chapter opens with its
own screenshot, so you can match the labels to the device.

The main screen has three parts:

- **Five tabs** across the top: Exposure, Contrast, Split Grade, Virtual Proof,
  Control Panel. The selected tab is highlighted.
- **The content area** in the middle: the controls and readouts for that tab.
- **The sidebar** on the right: paper, filter, sensor, calibration values,
  brightness, battery and the **Help** button. The sidebar is visible on every tab.

At the bottom of the sidebar the device shows **SafelightIO v.1.0**. This is the
firmware version; it is also on the splash screen and in the Help Center.

> [!NOTE] The screenshots are dim by design
> The device uses a dim red-on-black screen to protect your night vision. The
> screenshots in this manual reproduce that look; they can seem darker on paper than
> the screen does in a darkroom. They were taken before a reading, so values that have
> no measurement yet show `--`.

## 2.1 The tabs

| Tab | What it holds | Chapter |
|---|---|---|
| **Exposure** | Zone, lux, calibration constant, exposure time, filter grade and dodge/burn | 3 |
| **Contrast** | Highlight and shadow readings, contrast range, grade, trims | 4 |
| **Split Grade** | Soft and hard exposures, filter pair, trims | 5 |
| **Virtual Proof** | Grid, histogram, selected sample, stability, enlarger mode | 6 |
| **Control Panel** | **PAPER & FILTER EDITOR**, **ESTIMATE CALIBRATION**, **DATA MANAGER**, **SENSOR CALIBRATION** | 7 |

The fifth tab is labelled **Control Panel**. Its main heading is **PAPER & FILTER
EDITOR**. The Help Center calls the same area **Paper Editor**. They are the same
place; this manual uses **Control Panel** for the tab and **Paper & Filter Editor**
for the editing section.

## 2.2 The sidebar

The sidebar is the meter's setup panel. It stays put while you change tabs. The
full reference is chapter 8; in short:

- **Battery** and **Brightness** at the top.
- **Filter Brand**, **Paper Brand**, **Paper Type**.
- **Calibration Lux Value**, **Calibration Time Value**.
- **Sensor Averaging Samples**, **Sensor Gain**, **Intergration Time**.
- **SafelightIO v.1.0** and the **Help** button at the bottom.

> [!NOTE] The device spells one label “Intergration Time”
> The correct spelling is *Integration Time*. The manual uses the correct spelling
> in prose and quotes **Intergration Time** when it refers to the on-screen label,
> so you can find it on the device.

## 2.3 Common actions

| Action | What it does | Where |
|---|---|---|
| **Measure LUX** | Takes a light reading at the sensor | Exposure |
| **Measure Highlight** / **Measure Shadow** | Takes the two readings used for contrast | Contrast, Split Grade |
| **Measure** / **Start scan (n/total)** | Reads one proof cell and advances the grid cursor; with Stability Detection on it starts a hands-free scan | Virtual Proof |
| **Set V Zone** / **Set Reference** | Uses the selected cell as the middle-gray anchor | Virtual Proof |
| **Clear Grid** | Erases the proof grid and its reference | Virtual Proof |
| **Reset** | Returns the current tab's trims to neutral (current paper only) | Contrast, Split Grade, Control Panel |
| **Help** | Opens the Help Center | Sidebar |

## 2.4 Confirmation screens

Some actions cannot be undone, so the device asks first. The screen asks
**Are you sure?** with **Yes** and **No**. It is used by:

- **Clear All Calibrations** (wipes every paper calibration and the reference);
- **Auto-Est. All Papers** (overwrites estimates for uncalibrated papers);
- **Load settings** and **Load Session** (replace current data);
- **Clear** under the sensor calibration headings;
- the second phase of **Calibrate Light**.

Read the question, then choose. **No** returns without changing anything.

## 2.5 The splash screen

At power-on, before the main screen:

- the banner **SafelightIO Darkroom Meter v.1.0**;
- **Prototype - Not for Sale**;
- an **Inspirational quote** and a practical darkroom tip (they change at random);
  for example **Tip: Pre-flash your paper for highlight detail**;
- a closing line such as **Have a happy developing sessions!**;
- the serial number and a QR code to the project page.

Nothing on the splash is a control. Wait for the main screen.

---

# 3. Exposure

**Use this tab when you have a negative and want a printing time.**

![Exposure flow: choose the zone, measure, read the time](manual/figures/fig-exposure-flow.svg)

## 3.1 The screen

The left column is the measurement: zone, lux reading, calibration constant and the
**Measure LUX** button. The right column is the **FILTER & DODGE/BURN** panel:
filter grade transform, dodge/burn slider, additional time and total time.

The large number at the top is the **exposure time**. Before you measure it may show
a message instead of a number: **`calibrate`** or **`measure lux`**. A reading of
0.00 lux is below the sensor's usable range and shows **`below sensor range`**. The
sensor's own messages — **`no sensor`** and **`error`** — appear on the
**LUX READING** line. Chapter 13 explains each one.

![The Exposure tab on the device, with the sidebar on the right](manual/figures/screen-exposure.png)

## 3.2 Every control and readout

| Element | What it is | What to do |
|---|---|---|
| **EXPOSURE CALCULATOR** | The tab heading | — |
| **Exposure time readout** | The suggested printing time in seconds | Read it; it updates after Measure and after filter/dodge changes. A second line says `incl. +x.xx s reciprocity` when long-exposure correction was applied |
| **SELECT ZONE OF MEASUREMENT** | Opens the zone list | Choose the zone the measured tone should print on; **V** is the normal midtone |
| **Zone of measurement** | The list: 0, I, II, III, IV, V, VI, VII, VIII, IX, X | See the zone table below |
| **LUX READING** | The last measured light level in lux | Shows the raw measurement |
| **CALIBRATION CONSTANT** | The paper's lux × seconds constant | Set by paper calibration; read-only here |
| **Measure LUX** | Takes a reading and calculates the time | Press once per measurement; the backlight dims while it reads |
| **FILTER & DODGE/BURN** | Heading for the right-hand panel | — |
| **FILTER GRADE TRANSFORM** | Opens the filter grade list | Choose the filter you will actually use. The grade's factor lengthens the time |
| **DODGE & BURN** | Heading for the slider and the two times | — |
| **Dodge and burn slider** | Adds or removes exposure in ¼-stop steps | Drag right to print darker, left to print lighter |
| **ADDITIONAL TIME** | The seconds added by the slider | Read-only; negative values mean less time |
| **TOTAL TIME** | Base time + additional time | This is the time to use at the enlarger |
| **F-Stop** | The slider's position expressed in f-stops | Read-only; useful when writing notes |

## 3.3 Step by step

1. **Select the paper.** In the sidebar choose **Paper Brand** and **Paper Type**.
2. **Select the filter.** Choose the grade you will put in the enlarger under
   **FILTER GRADE TRANSFORM**. “No filter” keeps the time unchanged.
3. **Place the sensor.** Put it where the midtone will fall on the easel. Keep your
   body and the safelight out of the light path.
4. **Choose the zone.** **V** for a midtone; **III** for a shadow you want to place;
   **VII** for a highlight.
5. **Press Measure LUX.** Wait for the backlight to return.
6. **Read the time.** Use **TOTAL TIME** if you moved the dodge/burn slider;
   otherwise use the large exposure time.

## 3.4 The zone list

The zone tells the meter which tone you measured, counted on the print's scale:
**Zone V** is the reference, **Zone VIII** is three stops lighter and **Zone III** is
two stops darker. Naming the zone lets the meter place that tone on that zone, so the
reading can come from any part of the image.

| Zone | Tone you are measuring | How the printed time changes |
|---|---|---|
| **0** | Deep black, almost no detail | +5 stops (×32) |
| **I** | Black with a hint of detail | +4 stops (×16) |
| **II** | Dark shadow with texture | +3 stops (×8) |
| **III** | Shadow with good detail | +2 stops (×4) |
| **IV** | Dark midtone | +1 stop (×2) |
| **V** | Middle gray — the reference | no change (×1) |
| **VI** | Light midtone | −1 stop (÷2) |
| **VII** | Highlight with texture | −2 stops (÷4) |
| **VIII** | Bright highlight, little texture | −3 stops (÷8) |
| **IX** | Near white | −4 stops (÷16) |
| **X** | Paper white | −5 stops (÷32) |

The sensor sits at the easel, where the tones are inverted: the part that prints
lighter is the part that receives the least light. The meter accounts for that, so
naming a lighter zone shortens the time rather than lengthening it.

> [!TIP] Which zone should I use?
> Measure **V** when the sensor sits on the midtone. Measure **III** when you want
> to place a shadow, or **VII** for a highlight. The meter converts either reading
> to the same exposure scale, so you do not have to move the sensor to a midtone.

## 3.5 What the filter grade does

A contrast filter absorbs light, so it needs a longer exposure. The meter knows the
built-in factor for each grade and brand, and multiplies the base time by that
factor. The filter grade also changes the contrast of the print; the meter does not
try to compensate for that, because that is the point of the filter.

If you have measured your own filter factor (chapter 12), the device uses your value
instead of the built-in one.

## 3.6 Dodge and burn

The slider is a trim, not a second exposure. It adds or removes time from the whole
print in ¼-stop steps, up to ±2.25 stops. Use it when the print is consistently a
little light or dark, or when you want to try a variation without recalibrating.

- **ADDITIONAL TIME** shows the seconds the slider adds (or subtracts).
- **TOTAL TIME** is what you actually expose.
- The slider resets when you change paper.

For local dodging and burning under the enlarger, use the same total time as your
starting point and cover/uncover areas as usual.

## 3.7 A worked example

A portrait negative, Ilford FP4, printed on Ilford Multigrade Classic Cooltone.
The sensor is on the face at **Zone VI**.

1. The filter is grade **3**, factor about 2.5.
2. The sensor reads **2.84 lux** at Zone VI.
3. The meter converts Zone VI to the Zone V equivalent: 2.84 × 2 = **5.68 lux**.
4. The paper's constant — 12.50 lux·s — gives 12.50 ÷ 5.68 ≈ **2.20 s**.
5. The grade 3 factor makes it 2.20 × 2.5 = **5.50 s**.
6. The dodge/burn slider at +2 quarter-stops adds about 2.3 s → **~7.8 s** total.

You do not have to do this arithmetic. The point is that every step has a visible
readout, and the **TOTAL TIME** already includes all of them.

## 3.8 Common questions

**Why does the time change when I change the filter?** The filter absorbs light; the
factor compensates. The print contrast changes too, which is why you chose the
filter.

**Why does the time change when I change paper?** Each paper has its own calibration
and its own trims.

**Can I use the meter without calibrating the paper?** You can read lux, but you
will not get a time. The tab shows `calibrate` until the paper is calibrated.

**The time looks wrong by exactly 2×.** Check that you measured the zone you think
you did, and that the enlarger height and aperture match the calibration. If they
do, run **Calibrate Light** again.
