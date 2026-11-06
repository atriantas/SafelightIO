# 7. Control Panel

**Use this tab to edit filter data, estimate calibrations, save/load, and calibrate
the sensor.**

The tab is labelled **Control Panel**. Its main heading is **PAPER & FILTER
EDITOR**. The Help Center calls the same area **Paper Editor**. The tab has four
sections in two columns:

![The Control Panel tab on the device](manual/figures/screen-control.png)

- **PAPER & FILTER EDITOR** — left column, top. Override the built-in factors and
  ISO values.
- **ESTIMATE CALIBRATION** — left column, bottom. Copy a calibration to other
  papers by speed.
- **DATA MANAGER** — right column, top. Save and load settings and sessions.
- **SENSOR CALIBRATION** — right column, bottom. Dark and light calibration.

## 7.1 Paper & Filter Editor

This section changes the numbers the meter uses for a **paper + filter grade**
combination. It is for advanced users; the built-in data is good enough for most
printing. Edits survive a power cycle: they are written to `SETTINGS.TXT` when a
card is inserted, and to internal flash when there is no card.

| Element | What it is | What to do |
|---|---|---|
| **Select Filter** | Chooses the grade to edit | Pick the grade whose data you want to change |
| **Lengthening Factor** | The filter's exposure multiplier | Raise it if prints through that filter are too light; lower it if too dark |
| **ISO R Range** | The contrast range this grade produces | Higher = softer contrast; lower = harder |
| **Base ISO P** | The paper's unfiltered speed | Higher = shorter times; lower = longer times. This is per paper, not per grade |
| **FILTER VALUES** | The read-only value block | — |
| **Factor value** | The **effective** factor used by every tab | Shows your override, or the built-in value |
| **Default factor value** | The built-in factory factor | Reference only |
| **ISO R value** | The **effective** ISO R | Shows your override, or the built-in value |
| **Default ISO R value** | The built-in ISO R | Reference only |
| **ISO P value** | The **effective** ISO P for the paper | Shows your override, or the built-in value |
| **Default ISO P value** | The built-in ISO P | Reference only |
| **Reset** | Clears all overrides for the **current paper** | Other papers keep their overrides |

- A factor of **1.00** means “no exposure change”.
- A readout shows `--` when there is no value to display yet, for example before a
  grade is selected.
- If the selected paper has no filter data for the selected filter brand, the
  **Factor** and **ISO R** fields show `--` and are locked. That is a normal state
  (for example a variable-contrast paper under a brand with no compatibility
  table), not a fault. **Base ISO P** still works because it is a per-paper value.
- Two decimal places are enough for the factor; ISO R and ISO P are whole numbers
  between 1 and 999. A `PAPERS.CSV` row outside that range is rejected rather than
  loaded with a value the fields cannot show.
- The device stores at most **64 filter overrides** and at most **23 ISO P
  overrides**. If an ISO P override cannot be stored, the status line says so and
  the value is not changed — reset a paper you no longer use.
- On a fixed-grade paper, Factor and ISO R are disabled; only ISO P can be changed.
- Changing a value commits that field. Selecting another grade commits a pending
  edit first.

> [!NOTE] What ISO R and ISO P mean
> **ISO R** is the paper's contrast range: a higher number is a softer paper.
> **ISO P** is its speed: a higher number means a faster paper and a shorter time.
> You do not need the standards to use the meter; you only need to know which way
> the numbers move.

## 7.2 Estimate Calibration

This section copies a calibration from one paper to another. It is a shortcut for
papers you have not calibrated yet; the result is an estimate, not a measurement.

| Element | What it is | What to do |
|---|---|---|
| **ESTIMATE CALIBRATION** | The section heading | — |
| **Reference Paper** | Snapshots the current paper's calibration (lux, time, ISO P) | Calibrate one paper well, select it, then press **Reference Paper** |
| **Reference status** | Tells you whether a reference is stored | If it says **No reference**, set one first |
| **Estimate Calibration** | Estimates the current paper from the reference, scaled by ISO P | Use it for a paper you have not calibrated |
| **Auto-Est. All Papers** | Estimates every uncalibrated paper from the reference | Asks for confirmation first |
| **Clear All Calibrations** | Wipes every paper calibration and the reference | Asks for confirmation first; this cannot be undone |

The estimate assumes that, at the same light level, a paper with twice the ISO P
needs half the time. It is a starting point: make a test strip and adjust.

The calibration time field holds **99.99 s** at most. An estimate that would need
a longer time is refused with a message instead of being stored, because the field
could not show it and the next touch of a calibration spinbox would overwrite the
real value with the displayed one. **Auto-Est. All Papers** skips such papers and
reports how many it skipped.

**A sensible workflow:**

1. Calibrate your most-used paper properly (chapter 10).
2. Select it and press **Reference Paper**.
3. Select an uncalibrated paper and press **Estimate Calibration**.
4. Print a test strip; if the time is off, calibrate that paper properly or adjust
   its factor.
5. Use **Auto-Est. All Papers** only when you want rough starting points for the
   whole collection.

## 7.3 Data Manager

| Element | What it is | What to do |
|---|---|---|
| **DATA MANAGER** | The section heading | — |
| **Save and Load Setting** | The settings group | — |
| **Save Settings** | Writes the internal flash snapshot, plus `BACKUP.TXT` when a card is in | Do it before a firmware update |
| **Load settings** | Restores the flash snapshot; reboots. Works with or without a card | Asks for confirmation first |
| **Save and Load Session** | The session group | — |
| **Session slot picker** | Lists slots 1-8 with what each one holds (paper, filter, exposure) or **empty** | Tap it and choose the slot the two buttons below act on |
| **Save Session** | Writes the current readings and results to the selected slot | Use it to resume later or share a setup |
| **Load Session** | Restores the selected slot | Asks for confirmation if measurements exist |
| **Calibration switch (session load)** | Include or exclude the stored calibration when loading | On if you want the session's calibration restored; off to keep the current one |
| **Data manager message** | The result line: saved, loaded, **Nothing to export**, **Session 3 is empty** | Read it if a button seems to do nothing |

A **session** contains the current paper and filter, the last Contrast and Split
readings and results, and the Virtual Proof grid (including its mode). It does not
contain your whole settings file; use **Save Settings** for that. The four
Contrast/Split trim sliders are per-paper settings, not session data: **Load
Session** leaves the selected paper's trims unchanged.

## 7.4 Sensor Calibration

| Element | What it is | What to do |
|---|---|---|
| **SENSOR CALIBRATION** | The section heading | — |
| **Calibrate Environment Noise** | The dark-calibration group | Do it in total darkness |
| **Calibrate Dark** | Measures the sensor's electrical noise floor | Press once in darkness; it sweeps several settings automatically |
| **Clear** (dark) | Erases the dark calibration | Asks for confirmation |
| **Sensor calibration status** | Progress and result, for example `dark calib... 12/24` or `dark offsets set (24)` | Wait for it to finish |
| **Calibrate Enlarger Light** | The light-calibration group | Do it with the enlarger on and steady |
| **Calibrate Light** | Measures the gain stages against a known light level | Follow the two-phase prompt |
| **Clear** (light) | Erases the light calibration | Asks for confirmation |

### Calibrate Dark

1. Put the sensor in **total darkness** — cap it, or close the enlarger and turn off
   all light.
2. Press **Calibrate Dark**.
3. The device sweeps 24 combinations of gain and integration time. It shows
   `dark calib... n/24` while it works; at the slowest settings this takes a few
   minutes.
4. Wait for `dark offsets set (24)`. If it says `dark calib failed`, light reached
   the sensor; repeat in darkness.

### Calibrate Light

1. Put the sensor in **steady enlarger light** — no negative, lens open, lamp warmed
   up. Use a mid-range light level, not the brightest the enlarger can produce.
2. Press **Calibrate Light**. The device starts phase 1 and shows
   `gain calib... phase 1/2`.
3. When it asks, dim the light by about **four stops** (close the aperture or use a
   neutral density filter) and choose **Yes**.
4. Wait for `gain cal set`. If it says `gain cal failed - adjust light`, the level
   was too high or too low; adjust and repeat.
5. The result is stored. If the light moved during the calibration, it reports
   `- moved`; if there was not enough infrared, `- no IR`; if a stage saturated,
   `- MAX sat` or `HIGH zero`.

Run the light calibration once per device. Repeat it if readings disagree when you
switch gain, or after a firmware update that changes the sensor settings.

> [!IMPORTANT] Darkness and steady light matter
> A safelight, a phone screen or a gap in the enlarger can spoil the dark
> calibration. A flickering lamp or a moving hand can spoil the light calibration.
> Both are worth doing carefully once.

---

# 8. Settings sidebar

The sidebar is always visible. It holds the choices that affect every tab. From
top to bottom the panels hold:

- battery and **Brightness**;
- **Filter Brand**, **Paper Brand** and **Paper Type**;
- **Calibration Lux Value** and **Calibration Time Value**;
- **Sensor Averaging Samples**, **Sensor Gain** and **Intergration Time**;
- the battery status line, the version and **Help**.

![The real Settings sidebar](manual/figures/screen-sidebar.png)

| Element | What it is | Range / default | What to do |
|---|---|---|---|
| **Battery** + bar | Charge state | 0–100% | See 8.4 |
| **Brightness** + slider | Screen backlight | 1–100 | Set the dimmest level you can read; saves battery and stray light |
| **Filter Brand** | The filter system in your enlarger | 9 brands | Choose the brand printed on your filters |
| **Paper Brand** | The paper manufacturer | Built-in list | Choose before measuring |
| **Paper Type** | The paper surface/emulsion | Built-in list | Choose before measuring |
| **Calibration Lux Value** | The lux reading from your calibration test strip | 0.00–99.99 | Enter it during paper calibration |
| **Calibration Time Value** | The exposure time that produced the good test strip | 0.00–99.99 | Enter it during paper calibration |
| **Sensor Averaging Samples** | How many readings are averaged per measurement | 1–16, default 5 | Raise for dim or flickering light; lower for speed |
| **Sensor Gain** | Sensitivity stage | Auto, LOW, MED, HIGH, MAX; default Auto | Leave on Auto unless you need a fixed stage |
| **Intergration Time** | How long each sensor reading lasts | 100–600 ms, default 200 | Longer is quieter and slower; shorter is faster |
| **SafelightIO v.1.0** | Firmware version | — | Use it when checking an update |
| **Help** | Opens the Help Center | — | Quick reference on the device |

## 8.1 Choosing paper and filter

**Paper Brand** and **Paper Type** are linked: choose the brand first, then the
paper. Selecting a paper loads its calibration, its trims and its filter data. If
you change paper, measure again; the previous readings belonged to the previous
paper.

**Filter Brand** changes the grade names and the built-in factors. It does not
change the paper. Choose the brand of the filters you actually own. If the brand
has no data for the selected paper, the paper stays selectable; the Exposure tab
offers only **No filter**, the Contrast tab says `No filter data for this paper`
and the Split Grade tab says `No split-grade data for this paper`. Choose another
brand in that case.

## 8.2 Sensor gain, integration time and samples

These three controls trade speed against noise:

- **Sensor Gain**: Auto starts at the most sensitive stage and steps down when the
  light is bright enough. A fixed stage is useful when you want repeatable readings
  and you know the light level; if a fixed stage saturates, the reading shows
  `error`.
- **Intergration Time**: the length of one reading. Longer readings collect more
  light and are less noisy; shorter readings make a proof scan faster.
- **Sensor Averaging Samples**: how many readings are averaged. More samples make a
  steadier number; fewer make the device feel quicker.

For a Virtual Proof scan, lower the integration time and sample count. For a single
critical reading, raise them.

## 8.3 The calibration values

**Calibration Lux Value** and **Calibration Time Value** are the two numbers from
your paper calibration test strip. The device divides one by the other to get the
paper's constant. You only touch them during calibration (chapter 10).

## 8.4 Battery, charging and power

The battery bar is red and updates every five seconds. The device has no charger
status pin, so it infers charging from the battery voltage:

| Display | Meaning |
|---|---|
| **Discharging** + percentage | Running on the battery |
| **Charging...** (bar hidden) | USB-C connected; the device is charging |
| **Fully charged** | The cell has reached the charger's top voltage |
| **Battery absent** (grey, empty) | No battery detected; USB-C power only |
| **Battery low** | About 10% or less; charge now |

Notes:

- **Battery low** replaces the bar when the charge reaches about 10%. The device has
  no sleep mode, so the warning stays visible until you charge it.
- **Charging...** can stay on after the battery is effectively full, because some
  chargers stop just below the top voltage the device looks for. This is normal.
- The bar is voltage-based. Under a heavy load it can sag; a bar that looks empty
  while the device still runs is not necessarily a dead battery.
- Charge with USB-C. The battery is protected; unplug when you are done printing.
- **Brightness** at 1 is intentionally very dim, not off. Drag right if the screen
  looks dead.

---

# 9. Saving, loading and storage

The meter can keep its data in two places:

- **Internal flash** — always present. Settings, calibrations and trims live here.
- **microSD card** — optional. It holds copies and files you can move between
  devices or edit on a computer.

| File | Where | What it is |
|---|---|---|
| `SETTINGS.TXT` | SD card | The settings file |
| `SETTINGS.BAK` | SD card | The previous settings file |
| `PAPERS.CSV` | SD card | Custom paper definitions |
| `BACKUP.TXT` | SD card | A readable backup of the settings |
| `SESSION1.CSV` … `SESSION8.CSV` | SD card | One saved session per slot |

## 9.1 Settings and backups

- **Save Settings** writes the internal flash snapshot, and `BACKUP.TXT` as well
  when a card is inserted. Do this before a firmware update.
- **Load settings** restores the flash snapshot and reboots. It asks for
  confirmation, and it works with or without a card: the snapshot lives in the
  device, not on the card.
- Settings changes are flushed about half a second after the last edit. If you cut
  power immediately after a change, the last change may be lost.
- With a card inserted, the device also keeps `SETTINGS.TXT` on the card. On first
  boot with a card it copies the current settings to the card. If the card is
  removed, the device falls back to flash.
- A card inserted **while the device is running** is not used until the next
  reboot, because the device cannot tell whether the card or the current session
  holds the newer settings. The status line says `SD card found - reboot to
  load it`. A blank card is adopted immediately.
- Removing the card is not detected instantly; the sidebar can still say
  `SD: settings.txt` until the next save fails. If a save fails, reinsert the card
  and try again.

## 9.2 Sessions

A session is a snapshot of **the current work**, not the whole meter:

- the selected paper and filter;
- the last Contrast and Split readings and results;
- the Virtual Proof grid, its reference and its mode (negative or enlarger);
- optionally the paper calibration.

The filter is the Virtual Proof grade. **Load Session** reselects it when the
current filter brand still offers that grade; otherwise the preview falls back to
**No filter**.

Loading **replaces** the session state rather than merging into it. A session saved
with an empty proof grid loads as an empty grid; a session with no Contrast or Split
readings clears them. Anything the file does not contain is gone afterwards, which is
what the confirmation means by *current measurements will be replaced*. The paper
selection, the four per-paper trims and — unless its toggle is on — the paper
calibration are not session data and are left alone.

After a restore the amber cursor sits on the first cell with no reading, so the next
**Measure** fills a gap instead of overwriting the first loaded cell.

The per-paper tunables — the four Contrast and Split sliders — are not part of a
session. **Load Session** leaves them at the selected paper's saved values.

**Save Session** writes the slot chosen in the picker. **Load Session** restores it,
re-derives the results and asks before overwriting current measurements. The
**Calibration** switch decides whether the session's calibration is restored too.
If the card cannot be read to the end, the load is aborted and the current state is
left unchanged; a truncated session is never partly applied.

Eight slots are available; each one is a complete, independent session:

| Slot | File on the card |
|---|---|
| 1 | `SESSION1.CSV` |
| 2-8 | `SESSION2.CSV` … `SESSION8.CSV` |

The picker reads each file's header and shows what the slot holds, for example
`2: FOMA FOMASPEED / 2xY / 8.20 sec`. Slots that have never been saved read
`empty`. Nothing is typed — the description comes from the session itself.

- Pick a slot, then **Save Session** writes it. Saving over an occupied slot asks
  first.
- Pick a slot, then **Load Session** restores it. An empty slot reports
  `Session 3 is empty`.
- Each slot keeps a `.BAK` copy while it is being written, so a failed save leaves
  the previous session in that slot intact.
- The picker starts on slot 1 after every power-on; the slot choice is not saved.
- Older firmware wrote a single `SESSION.CSV`. That file is no longer read or
  written; delete it from the card if you want the space back.

Sessions are useful when you stop halfway through a print, when you want to compare
two negatives, or when you want to send a setup to another meter.

## 9.3 What is kept, and what is not

- Settings, paper calibrations, filter overrides and trims live in internal flash.
- Custom paper **definitions** live in `PAPERS.CSV` on the card. Their calibrations
  are stored on the card too; without the card they are not available after a
  reboot.
- `BACKUP.TXT` is a readable copy, not a second live database.
- A firmware update preserves the settings record only while the settings format is
  unchanged. A format change resets the stored settings; the release notes will say
  so. Recalibrate the sensor and your papers after such an update.

---

# 10. Calibrating a paper

**Do this once per paper.** It is the step that turns lux into seconds.

![Paper calibration: test strip, choose the midtone, enter lux and time](manual/figures/fig-paper-calibration.svg)

## 10.1 Before you start

- The enlarger is at the height, aperture and lens you will use for real prints.
- The paper is the one you will print on.
- The sensor is calibrated (section 7.4).
- You have a test strip and your usual developer.

## 10.2 Procedure

1. **Choose the paper** in the sidebar.
2. **Set up a normal print.** Use a negative with a good midtone and no contrast
   filter. Focus at the working height.
3. **Place the sensor** on the easel where the midtone will fall. Do not let the
   meter or your hand shadow the point.
4. **Press Measure LUX** and write down the lux reading.
5. **Make a test strip** at a few seconds, then in steps, through the same lens and
   aperture. Develop it normally.
6. **Choose the strip with the correct midtone.** Note its exposure time.
7. In the sidebar, enter the lux reading in **Calibration Lux Value** and the time
   in **Calibration Time Value**.
8. The device computes the constant. Open **Exposure** and check that it now shows a
   time instead of `calibrate`.
9. Make a full print to confirm. If it is consistently off by a small amount, use
   the **Exposure** trim rather than recalibrating.

## 10.3 What “correct midtone” means

The test strip should show the tone you want for a middle gray — not the lightest
strip that still has detail, and not the darkest. The meter uses that point as Zone
V. If you choose a different tone, the constant will be biased.

## 10.4 Redoing a calibration

Repeat the procedure and enter the new lux and time. The new values overwrite the
old ones for that paper. You do not need to clear anything first.

Calibrate again if:

- you change the enlarger, lens or aperture you print at;
- you change the paper's developer or dilution significantly;
- the prints are consistently off by a fixed factor and a trim no longer covers it;
- you replace the sensor.

## 10.5 Fixed-grade papers

Fixed-grade papers have one contrast grade. The calibration procedure is the same;
just use the paper's grade (no variable-contrast filter). The Contrast tab will show
**Fixed grade** and Split Grade is not applicable.

## 10.6 A calibration checklist

- [ ] Sensor dark calibration done.
- [ ] Sensor light calibration done.
- [ ] Paper selected in the sidebar.
- [ ] Same lens, aperture and height as real prints.
- [ ] Sensor on the midtone, not shadowed.
- [ ] Lux reading written down.
- [ ] Test strip developed normally.
- [ ] Correct midtone chosen.
- [ ] Lux and time entered.
- [ ] Exposure tab shows a time.

## 10.7 Worked examples

These examples follow the original guide's test-strip method. The first uses its
numbers; the others show common variations.

### Example 1 — the first calibration

You are printing on **Ilford Multigrade RC Deluxe** at f/8, with the head at your
usual height and no contrast filter.

1. You measure **2.50 lux** on the midtone.
2. You make a test strip in 4-second steps: **4, 8, 12, 16, 20 s**.
3. The **12-second** strip has the middle gray you want.
4. Enter **2.50** in **Calibration Lux Value** and **12.0** in **Calibration Time
   Value**. The device stores **30.0** lux-seconds (2.50 × 12.0).
5. With the same negative and no changes, press **Measure LUX** again. It should
   read about **2.50 lux**, and the Exposure tab should show **12.0 s**. That is the
   check that the calibration is good.

### Example 2 — recalibrating after a developer change

You mix a new developer and the same paper now prints darker at the same time.

1. The light reading is still **2.50 lux**.
2. The test strip says the correct midtone is now **9.0 s**, not 12.0 s.
3. Enter **2.50** and **9.0**. The constant becomes **22.5 lux-seconds**.
4. The paper is now calibrated for this developer. The old value is overwritten;
   there is nothing to clear first.

The constant changed because the paper/developer combination changed. That is
expected. If only the enlarger height or aperture changed, the light reading changes
instead, and the constant should stay close to the old value.

### Example 3 — a fixed-grade paper

You are printing on **FOMA FOMASPEED Normal**, which has one contrast grade.

1. Select the paper. Use no contrast filter.
2. Measure **2.50 lux** on the midtone.
3. The test strip gives **12.0 s**. Enter **2.50** and **12.0**.
4. The Exposure tab gives a time. The Contrast tab shows **Fixed grade**, and Split
   Grade is not applicable.

The procedure is the same as for a variable-contrast paper. The only difference is
that there is no grade to choose.

### Example 4 — a second paper from a reference

You have already calibrated **Ilford MG FB Classic** at **1.42 lux** and **8.8 s**.
You want a starting point for **FOMA FOMABROM Variant**.

1. On the calibrated paper, press **Reference Paper**.
2. Switch to **FOMA FOMABROM Variant**.
3. Press **Estimate Calibration**.
4. The meter scales the reference by the paper speed (ISO P 500 → 130), about
   **×3.85**, and suggests **33.9 seconds**.

This is a starting point, not a measurement. Make a real test strip before you trust
it for critical work.

### Example 5 — no strip looks right

The 12-second strip is too dark and the 8-second strip is too light.

- Make a new strip through the same setup at **9.5, 10.0, 10.5 and 11.0 s**.
- If even the whole strip is too dark or too light, move the range by a full stop and
  repeat. Do not guess the constant.
- When one strip is clearly right, enter its time. The constant is what you measured,
  not what you hoped for.

---

# 11. The paper and filter database

## 11.1 Papers

The built-in database has **22 papers** across Ilford and FOMA. Most are
variable-contrast; **eight are fixed-grade**. The Paper Type dropdown is the source
of truth for the exact list on your firmware.

Fixed-grade papers:

- FOMA FOMASPEED Normal
- FOMA FOMASPEED Hard
- FOMA FOMABROM Normal
- FOMA FOMABROM Hard
- FOMA FOMABROM N chamois, glossy
- FOMA FOMABROM N chamois, matt
- FOMA RETROBROM Special, glossy
- FOMA RETROBROM Special, semi-matt

The variable-contrast papers include the Ilford Multigrade RC and FB families
(Deluxe, Portfolio, Warmtone, Cooltone, Classic, ART 300) and the FOMA Variant,
Fomabrom Variant, Fomapastel and Fomatone families. Some entries are marked **~** in
the database documentation because their values are derived from similar papers
rather than measured. They are reasonable starting points; calibrate the paper for
critical work.

## 11.2 Filter brands

The **Filter Brand** list has **nine** entries:

| Brand | Grade names you may see |
|---|---|
| **Ilford** | 00, 0, 1, 2, 3, 4, 5 |
| **FOMA** | Y, M, and Special variants |
| **AGFA** | 00–5 |
| **KODAK** | 00–5 |
| **DURST** | 00–5 |
| **MEOPTA** | 00–5 |
| **BESELER** | 00–5 |
| **OMEGA/CHROMEGA** | 00–5 |
| **DE VERE** | 00–5 |

The exact grades offered depend on the paper and the brand. If a grade is not
available for the selected paper, it does not appear in the list.

## 11.3 Adding your own papers

Custom papers are read from `PAPERS.CSV` on the microSD card at boot. You do not
need to rebuild the firmware.

The file has a header line and two kinds of rows:

- a **P** row defines a paper (id, manufacturer, type, contrast type, family,
  Dmin, Dmax, fibre base, ISO P);
- one or more **F** rows define that paper's filter grades (grade, factor, ISO R).

Rules:

- Commas or semicolons separate fields.
- A **P** row needs at least 10 fields; an **F** row needs at least 8.
- Up to 8 filter rows per paper.
- A paper whose id matches a built-in replaces it; other ids are added at the end.
- The file is a template on first boot with a card. Edit a copy, keep the header,
  and reboot with the card inserted.
- Calibrations for custom papers live on the card; without the card they are not
  available after a reboot.

The exact column order is documented in the header comment that the device writes
into the template. Keep a backup of the file; it is not part of `BACKUP.TXT`.

---

# 12. Filter factors

## 12.1 What a filter factor is

A contrast filter absorbs light. The **factor** is how many times longer the
exposure must be to compensate. A factor of 2.0 doubles the time; 1.50 adds half.

The meter has built-in factors for each paper and grade. They are manufacturer
averages; your enlarger, lamp and filters can differ by 10–30%. If your prints
through a filter are consistently light or dark, adjust the factor in the Control
Panel (chapter 7.1).

## 12.2 Measuring your own factor, simply

1. Without a filter, make a test strip of a midtone and find the correct time.
2. With the filter you want to measure, make another strip of the same subject at
   the same aperture and height.
3. Divide the filtered time by the unfiltered time. That is the factor.
4. Enter it in **Lengthening Factor** for that grade.

Example: 12.0 s unfiltered and 26.4 s filtered → 26.4 ÷ 12.0 = **2.20**.

You do not need a densitometer. A consistent test strip is enough.

## 12.3 Re-measuring

Re-measure after changing the lamp, reflector, lens or filter set; when prints
through one grade are consistently off; or once a year if you print often.

## 12.4 Long exposures

At very long exposures, paper loses some sensitivity (reciprocity failure). The
meter applies a correction automatically when the time is long enough, and tells you
when it has done so: the **Exposure** tab appends `incl. +x.xx s reciprocity` under
the time, and the Contrast tab says it in the **Exposure Note**. You do not need to
calculate it. If you override a filter factor, use the measured value; an incorrect
factor compounds with the long-exposure correction.
