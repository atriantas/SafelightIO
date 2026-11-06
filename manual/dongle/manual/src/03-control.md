# 7. Setup

## 7.1 The index

Tap **Setup**. The index groups the pages by what they belong to:

| Group | Row | What it opens |
|---|---|---|
| **Device** | **Meter** | Connection, firmware, serial and board |
| **Device** | **Paper & filter** | The same sheet as the selection bar |
| **Calibration** | **Calibration** | The paper's known lux and known time |
| **Calibration** | **Sensor** | Gain, integration time, averaging and Sensor Calibration |
| **Work** | **Tools & data** | Paper editor, estimate and files |
| **Work** | **Help & messages** | What a refusal means and where to fix it |
| **Work** | **About** | Version and the data rule |

## 7.2 Meter

The **Meter** page reports what the dongle said when it connected: the firmware
version, the protocol, the board and the serial number. The **SafelightIO ID**
is shown as `SN: ...`, the chip's uppercase unique board ID, just as the
7-inch device shows it. Use it to tell two dongles apart. **Reconnect** asks the app
to open the port and send `HELLO` again.

Use it when the top bar is stuck on **No meter** or **Linking**, or after a
firmware update. If the dongle is not attached, the page says so; it cannot
invent a connection.

## 7.3 Calibration

The **Calibration** page is the paper's two numbers:

- **Known lux**: the light measured on the test strip;
- **Known time (s)**: the exposure that produced the chosen midtone.

The page shows the paper the dongle has in force, whether it has a calibration,
the meter's constant and the phone's copy when one exists. Enter the pair and
send it; the dongle stores it for that paper.

For a fixed-grade paper, the page still takes the pair; there is no grade
ladder to choose. Use the same midtone procedure.

## 7.4 Sensor

The **Sensor** page has three controls:

- **Gain** — a snap rail: **Auto**, **Low**, **Med**, **High**, **Max**.
- **Integration time (ms)** — a snap rail from 100 to 600 ms.
- **Averaging samples** — a number field, 1–16.

The page also shows:

- **Effective gain** — the rung the meter resolved, or the manual gain it is
  using;
- **A read may take** — the time budget for one reading;
- the provenance line — whether the settings came from the meter or the phone;
- the phone's backup copy, when one exists.

Auto is the normal choice; a manual rung is for a difficult subject or for checking the sensor's behaviour.

### Sensor Calibration

At the bottom of the Sensor page is the **Sensor Calibration** card. It holds
**Calibrate Dark** and **Calibrate Enlarger Light**, plus **Clear Dark** and
**Clear Light**. Do the dark calibration with the sensor covered and the light
calibration with the enlarger on. This is the one-time job that makes the lux
numbers trustworthy.

> [!IMPORTANT] Do not skip the sensor calibration
> A paper calibration on top of an uncalibrated sensor gives a time, but the lux
> numbers under it are not trustworthy. The sensor calibration is the foundation
> for the paper calibration, not an optional extra.

---

# 8. Tools & data

Open **Setup → Work → Tools & data**. It has three cards.

## 8.1 Paper & Filter Editor

The editor changes the paper's coefficients on the dongle. Choose the filter
and the paper; the editor shows the **Lengthening Factor**, the **ISO R Range**
and the **Base ISO P**. For a fixed-grade paper, the factor and ISO R fields are
inert and the fixed grade is shown instead; the Base ISO P is editable.

The editor is an advanced tool. If you only need to choose a paper that is
already in the catalogue, use **Paper & filter** instead.

## 8.2 Estimate Calibration

The estimate card gives a starting calibration when you do not have a test
strip. It uses the paper's ISO P and the reference paper to estimate the pair.
Treat the result as a starting point and confirm it with a real strip.

## 8.3 Data Manager

The Data Manager saves and loads two kinds of file on the phone:

- **Settings**: the dongle's persistent settings, including the paper
  catalogue and calibrations;
- **Session**: the current tool's readings, trims and selections.

A load always shows a preview and asks for confirmation before it writes
anything to the dongle. **Save** writes a text file to the phone; **Load** opens
one after the preview. The app never silently restores a file at launch.

---

# 9. Saving, loading and storage

## 9.1 What is saved automatically

The dongle persists the paper, the filter brand and grade, the paper
calibrations, the sensor settings, the trims and the burn. The app reads them
on every connection. You do not need to press Save to keep the ordinary
working state.

The app's own view is not a file. Switching tools, rotating the phone or
reopening the app does not lose the dongle's settings because they are on the
dongle.

## 9.2 Settings files

A **Settings** file is a backup of the dongle's persistent state. Use it when
you want a copy on the phone, or when you are moving to another dongle. The
file is a text document; the Data Manager preview shows what it contains before
you load it.

## 9.3 Session files

A **Session** file stores the current tool's readings, trims and selections. It
is useful when you want to come back to a print after a break, or when you want
to keep the two readings from a Contrast or Split session.

Loading a session restores the readings and the trims; it does not change the
paper calibration or the paper catalogue unless the file contains those groups.
The preview always says what will be written.

## 9.4 What is kept, and what is not

| Data | Lives on |
|---|---|
| Paper catalogue | Dongle |
| Paper calibration | Dongle (and in a Settings file when saved) |
| Filter brand and grade | Dongle |
| Sensor gain, integration, averaging | Dongle |
| Trims and burn | Dongle, per paper and per tool |
| Current readings | App session; not on the dongle after a power cycle |
| Settings and Session files | Phone documents, only when you save them |
| App version and code | Phone |

The dongle does not persist the current readings. If you unplug it, the readings
leave with the app's session; save a Session file if you need them later.

---

# 10. Calibrating a paper

## 10.1 Before you start

You need:

- a calibrated sensor (chapter 7.4);
- the paper and the filter brand you will print with;
- a test strip and the reference print you are matching;
- a way to measure the light on the strip.

The paper calibration is one-time per paper and filter. Redo it when you change
developer, toner, or the paper's response.

![Paper calibration: one strip, choose the midtone, enter two numbers](manual/figures/fig-calibration.svg)

## 10.2 Procedure

1. Make a test strip with a series of exposures, usually in half or third
   stops.
2. Develop it exactly as you will develop the print.
3. Choose the patch that matches the reference midtone. This is the **known
   time**: the exposure that produced that patch.
4. Measure the light on that patch with the meter. This is the **known lux**.
5. Open **Setup → Calibration** (or **Tools & data → Estimate Calibration**).
6. Enter **Known lux** and **Known time (s)**; send the pair.
7. The dongle multiplies the known lux by the known time to get the paper's
constant. The app confirms
   the constant it read back.
8. Make a print at the meter's suggested time. The print should match the
   reference midtone; if it does not, check the sensor calibration before
   repeating the strip.

## 10.3 What "correct midtone" means

The correct patch is the one that matches the tone you want middle grey to be,
not the one that looks "nice" in isolation. Use the same reference print and
the same viewing light each time. A darkroom's safelight can make a print look
darker than it is; judge under the enlarger's white light or a consistent
viewing light.

## 10.4 Redoing a calibration

Redo the paper calibration when:

- you change developer or dilution;
- you change the paper's grade or the paper itself;
- the prints are consistently off in the same direction;
- you have replaced the sensor or the dongle.

You do not need to redo it for every print, every session, or every filter
change. The filter factor is part of the dongle's table, not the paper
calibration.

## 10.5 Fixed-grade papers

A fixed-grade paper has no variable-contrast ladder. The calibration pair is
still lux and time; the grade is fixed by the paper. The editor and the
calibration page show the fixed grade and make the factor/ISO R fields inert.

## 10.6 A calibration checklist

- Sensor dark calibration done.
- Sensor light calibration done with the enlarger at the working height.
- Paper and filter brand selected.
- Test strip developed exactly like the print.
- Midtone chosen under consistent light.
- Known lux and known time entered for the right paper.
- The dongle answered with a constant; the app shows it.
- A confirm print matches the reference.

## 10.7 Worked examples

### Example 1 — the first calibration

You expose a strip in one-stop steps and the 8-second patch matches your
reference midtone. You measure 1.20 lux on that patch. Enter **1.20** lux and
**8** seconds. The dongle stores the product; the Exposure answer for a 0.30 lux
reading is then about 32 seconds.

### Example 2 — a developer change

You change from a paper developer to a warmer, slower developer. The prints are
consistently light. Make a new strip with the new developer, choose the new
midtone patch, and enter the new pair. Do not compensate with the burn; the
burn is for a print that is consistently off for a different reason.

### Example 3 — a fixed-grade paper

The fixed-grade paper's calibration page still asks for known lux and known
time. Choose the patch that matches the reference; the fixed grade is already
part of the paper's response.

### Example 4 — no strip looks right

If no patch matches, check the sensor calibration first, then the developer
temperature and the paper's age. A paper calibration cannot repair a sensor
that is reading the wrong lux.

### Example 5 — a second paper from a reference

If you have a calibrated paper and want a starting point for another, use
**Estimate Calibration**, then make a strip to confirm. An estimate is a
starting point, not a calibration.

---

# 11. The paper and filter database

## 11.1 Where the catalogue lives

The paper catalogue is on the dongle. The app does not ship a copy. On every
connection the app reads the dongle's `PAPERS` block: the paper brands, the
paper types and the filter brands. That is why the sheet says **Connect the
meter to list papers** when no dongle is attached.

The catalogue includes the paper's filter system, its kind (variable or fixed
grade) and its filter table. The app uses those fields to decide which grades
are offered and whether the Midtones pair is available.

## 11.2 Filter brands

The **Filter brand** rail lists the brands the dongle knows. A brand is half of
the selection: `FILTER brand= grade=`. The brand is shown in the selection bar;
the grade is chosen on Exposure.

## 11.3 Adding your own paper

Open **Setup → Tools & data → Paper & Filter Editor**. Choose the paper and the
filter, then edit the coefficients:

- **Lengthening Factor**: the paper's speed factor;
- **ISO R Range**: the contrast range;
- **Base ISO P**: the paper's ISO speed.

For a fixed-grade paper, the factor and ISO R fields are inert; the Base ISO P
is editable. **Reset** restores the paper's defaults after a confirmation.

> [!NOTE] The dongle is the source of truth
> The editor writes to the dongle. Another phone will see the edited paper only
> after it reads the dongle's catalogue again. There is no cloud copy and no
> bundled fallback.

---

# 12. Filter factors

## 12.1 What a filter factor is

A filter factor is a multiplier on the exposure: a factor of 2 means one stop
more light. Variable-contrast filters have different factors at different
grades, which is why the grade and the time are linked in the dongle's table.

## 12.2 Measuring your own factor, simply

1. Meter a plain, even grey target without the filter and note the time.
2. Meter the same target with the filter and note the time.
3. Divide the filtered time by the unfiltered time. The result is the factor.

Do this at the grade you actually use. The filter's factor is not a constant
across all grades.

## 12.3 Re-measuring

Re-measure the factor when you change the filter brand, the paper, or the light
source. The dongle's table is the starting point; your own measurement is the
confirmation.

## 12.4 Long exposures

Very long exposures can lose contrast through reciprocity. The meter does not
invent a reciprocity correction; if your paper's data sheet gives one, apply it
as a deliberate exposure adjustment and note it in the session, not as a paper
calibration.
