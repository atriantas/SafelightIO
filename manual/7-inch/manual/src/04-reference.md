# 13. Messages, Help Center and troubleshooting

## 13.1 What the messages mean

The device uses short messages because the screen is small. Here is the full list.

| Message | Where | Meaning | What to do |
|---|---|---|---|
| `select paper` | Exposure / Contrast / Split time | The paper selection did not resolve to a database entry | Choose the paper brand and type in the sidebar |
| `calibrate` | Exposure / Contrast / Split time | The selected paper has no calibration | Calibrate the paper (chapter 10) |
| `measure lux` | Exposure time | The paper is calibrated, but there is no live reading | Press **Measure LUX** |
| `below sensor range` | Exposure time | The live reading is 0.00 lux — below the sensor's usable range | Increase the light, gain or integration; measure again |
| `highlight below range` / `shadow below range` / `readings below range` | Contrast / Split time | A reading is 0.00 lux — below the sensor's usable range | Increase the light, gain or integration; measure again |
| `no sensor` | Lux readout | The sensor is not responding | Check the sensor cable; reboot |
| `error` | Lux readout | A reading failed, usually saturation at a fixed gain | Choose **Auto** gain, or a lower fixed gain |
| `read error` | Lux readout | The sensor reading failed | Reboot; if it persists, check the cable |
| `No stable reading` | Virtual Proof Measure button | The scan stopped because a cell did not settle within **Max Wait**; the cell keeps no reading | Keep the light steady, raise **Max Wait**, or turn off **Stability Detection**, then start the scan again |
| `Fixed grade` | Contrast tab | The selected paper has one contrast grade | Use Exposure; Split Grade is not applicable |
| `Fixed grade paper` / `Split-grade printing is not available...` | Split Grade | The selected paper has one contrast grade | Use Exposure; the Split controls are disabled |
| `No split-grade data for this paper` | Split Grade | The filter brand has no grade table for this paper | Choose another Filter Brand |
| `saved split pair unavailable for this brand; using defaults` | Split Grade analysis | The saved Midtones pair was chosen under another filter brand | Pick a pair again, or switch the Filter Brand back |
| `--` | Contrast / Split | One of the two readings is missing | Read the note; measure the missing point |
| `dark calib... n/24` | Sensor status | Dark calibration in progress | Wait |
| `dark offsets set (24)` | Sensor status | Dark calibration complete | — |
| `dark calib failed` | Sensor status | Light reached the sensor during calibration | Repeat in total darkness |
| `gain calib... phase 1/2` | Sensor status | Light calibration, first phase | Wait for the prompt |
| `gain cal set` | Sensor status | Light calibration complete | — |
| `gain cal failed - adjust light` | Sensor status | The light level was outside the usable range | Adjust the enlarger and repeat |
| `- moved` | Sensor status | The light changed during calibration | Keep the light steady and repeat |
| `- no IR` | Sensor status | Not enough infrared for the calibration | Use a tungsten/halogen enlarger light, or accept the limitation |
| `- MAX sat` / `HIGH zero` | Sensor status | One gain stage could not be calibrated | The other stages are still usable; repeat if needed |
| `No reference` | Estimate calibration | No reference paper has been set | Calibrate a paper, select it, press **Reference Paper** |
| `Nothing to export` | Data manager | There is no session data to save | Take a reading first |
| `Session 3 is empty` | Data manager | That slot holds no saved session | Pick another slot or save one first |
| `Session load failed` | Data manager | The file is not a session export, its paper is no longer available, or the card could not be read to the end | The load was aborted and the current state is unchanged; reinsert the card, or re-save the slot |
| `Settings not saved` | Control Panel status line | A settings write failed after three retries | Check the SD card and free space; change a setting to retry |
| `SD: none (flash)` | Control Panel status line | No card; settings are in internal flash | Insert a card if you want file storage |
| `Battery low` | Battery area | About 10% charge or less | Charge with USB-C |
| `Charging...` | Battery area | USB-C connected, charging | — |
| `Fully charged` | Battery area | The cell reached the top voltage | Unplug when convenient |
| `Battery absent` | Battery area | No battery detected | Use USB-C power, or fit the battery |

> [!NOTE] The device uses ASCII punctuation
> The on-screen strings use `...` and `-`, not typographic ellipses or dashes. This
> manual quotes the exact string so you can match it.

## 13.2 The Help Center

Press **Help** at the bottom of the sidebar. The Help Center opens with a **Back**
button, the version, and seven tabs:

| Help tab | Covers |
|---|---|
| **Start** | First-time setup, the one idea, what you need, a QR code to the project page |
| **Settings** | The sidebar: paper, filter, sensor, brightness, battery |
| **Exposure** | The Exposure tab |
| **Contrast** | The Contrast tab |
| **Split Grade** | The Split Grade tab |
| **Virtual Proof** | The proof grid, stability and Enlarger mode |
| **Paper Editor** | The Control Panel's paper/filter editor |

Each tab has a short explanation and a picture of the screen. The Help Center is a
reminder for when you are at the enlarger; this manual is the full reference. The
pictures in the Help Center may show an earlier firmware build; the text in this
manual matches firmware 1.0.

The **Start** tab also shows a QR code for the project page. The address is
`https://atriantas.github.io/SafelightIO/`.

## 13.3 Troubleshooting

### The meter gives no time

| Symptom | Likely cause | Fix |
|---|---|---|
| Exposure time shows `select paper` | Paper selection did not resolve | Choose the paper brand and type in the sidebar |
| Exposure time shows `calibrate` | Paper not calibrated | Chapter 10 |
| Exposure time shows `measure lux` | No reading yet | Press **Measure LUX** |
| Exposure time shows `below sensor range` | The reading is 0.00 lux, below the sensor's usable range | Increase the light, gain or integration |
| Lux shows `no sensor` | Sensor not responding | Check the cable; reboot |
| Lux shows `error` | Saturation at a fixed gain | Set **Sensor Gain** to **Auto**, or lower the fixed gain |

### The time is consistently wrong

| Symptom | Likely cause | Fix |
|---|---|---|
| Every print is 2× too light or too dark | Enlarger height or aperture differs from calibration | Recalibrate the paper at the height/aperture you print at |
| Every print is 2× too light or too dark, at the same setup | Gain stages uncalibrated | Run **Calibrate Light** |
| Readings disagree when you change gain | Gain stages uncalibrated | Run **Calibrate Light** |
| One paper is off, others are fine | That paper's calibration | Recalibrate that paper |
| Long exposures are off | Reciprocity correction or a stale filter factor | Check the **Exposure Note**; remeasure the filter factor |

### Contrast and Split Grade

| Symptom | Likely cause | Fix |
|---|---|---|
| `--` everywhere | A reading is missing | Measure both points |
| Grade and range shown, but the time says `calibrate` | The paper has no calibration | Calibrate the paper (chapter 10); the grade already applies |
| Grade looks too hard/soft | Match Quality is **Approximate** or a trim is active | Check the trims; press **Reset** |
| Fixed grade shown | Fixed-grade paper selected | Use Exposure; Split Grade is not applicable |
| Highlights burn every time | Negative range exceeds the paper | Choose a softer grade, or use Split Grade |
| Contrast grade does not change | Filter Brand or paper limits the available grades | Check the selected brand; not every brand offers every grade |

### Virtual Proof

| Symptom | Likely cause | Fix |
|---|---|---|
| Grid is empty after changing size | Changing Grid Size clears the grid | Rescan |
| Every highlight is clipped | The negative is too contrasty for the paper/grade | Choose a softer grade, or use Split Grade |
| A cell will not settle | Light is flickering or the sensor is moving | The scan stops and keeps no reading for that cell. Keep the light steady, raise **Max Wait**, or turn off **Stability Detection** |
| Set V Zone seems to change everything | It changes the reference for the whole grid | Use it deliberately; Clear Grid resets it |
| Enlarger verdict is UNEVEN | Light falls off or is misaligned | See section 6.5 |

### Control Panel and data

| Symptom | Likely cause | Fix |
|---|---|---|
| Filter editor shows stale values | The spinboxes follow the grade dropdown | Re-select the filter grade |
| Reset did nothing | Reset only affects the current paper | Select the paper you want to reset |
| **Estimate Calibration** says No reference | No reference paper | Set **Reference Paper** first |
| **Clear All Calibrations** wiped everything | You confirmed the action | Recalibrate; the confirmation screen is deliberate |
| **Save Session** says Nothing to export | No readings yet | Take a reading first |
| **Load Session** says Session 3 is empty | That slot has no saved session | Pick a slot whose picker entry is not `empty` |
| **Load Session** says Session load failed | Card read error or malformed session | Current state is unchanged; reinsert the card or re-save the slot |
| Settings changes lost after power-off | Flush takes about half a second | Wait a moment after the last edit |
| Custom papers gone after reboot | Card removed or file not read | Insert the card and reboot |

### Screen, power and sensor

| Symptom | Likely cause | Fix |
|---|---|---|
| Screen looks almost black | Brightness at 1 | Drag **Brightness** right |
| Screen dims during Measure | The backlight dims to 6% during reads | Normal; it restores afterwards |
| Screen dark for several seconds | Long sample count at 600 ms | Reduce samples or integration time |
| Battery bar empty but device runs | Voltage sag under load | Charge; **Battery low** is the real warning |
| **Charging...** never ends | Charger stops just below the top voltage | Normal |
| The device does not sleep | There is no sleep mode | Use **Brightness** and charge when needed |

> [!TIP] Before assuming a fault
> Check the sensor cable, the selected paper, and the battery. The three cause most
> “wrong reading” reports.

---

# 14. Firmware updates

The firmware can be updated over USB-C with a `.uf2` file. No special tools or
drivers are needed.

## 14.1 Check your version

The firmware version is **v1.0**. You can see it:

- on the splash screen (**SafelightIO Darkroom Meter v.1.0**);
- at the bottom of the sidebar (**SafelightIO v.1.0**);
- in the Help Center.

## 14.2 Update

1. **Get the file.** Use the firmware file supplied for your meter. The project
   page is `https://atriantas.github.io/SafelightIO/`; the QR code on the Help
   Center's Start tab opens it.
2. **Enter the bootloader.** With the meter off, press the small **BOOTSEL** hole at
   the top of the device with a pin, keep it pressed, and connect USB-C. The computer
   shows a removable drive called **RP2350**.
3. **Copy the `.uf2` file** to that drive. The meter verifies it and reboots.
4. **Wait for the main screen.** Your settings and paper calibrations are kept
   unless the release changes the settings format.

> [!WARNING] Use the right file
> Do not install a firmware file for a different device. If the drive does not
> appear, try a data-capable USB-C cable and press the BOOTSEL hole again.

## 14.3 If the update does not start

| Symptom | Likely cause | Fix |
|---|---|---|
| No **RP2350** drive | The BOOTSEL hole was not pressed, or the cable is charge-only | Press the hole with a pin and repeat with a data cable |
| The file disappears immediately | The file is corrupt or for another device | Download it again from the project page |
| The meter still runs the old version | The copy did not complete | Repeat the update |
| Calibrations are gone | The settings format changed | Recalibrate the sensor and your papers |

---

# 15. Reference

## 15.1 Ranges and defaults

| Setting | Range | Default |
|---|---|---|
| Zone of measurement | 0–X | V |
| Calibration Lux / Time | 0.00–99.99 | — |
| Sensor Averaging Samples | 1–16 | 5 |
| Sensor Gain | Auto, LOW, MED, HIGH, MAX | Auto |
| Intergration Time | 100–600 ms | 200 ms |
| Brightness | 1–100 | — |
| Grid width | 2–40 | — |
| Grid height | 2–30 | — |
| Uniformity Limit | 5–50% | 15% |
| Filter factor | 0.01–99.99 | built-in per grade |
| ISO R / ISO P | 1–999 | built-in per paper |
| Filter overrides | up to 64 | 0 |
| Contrast/Split trims | ±1.5 stops, 1/6-stop steps | 0 |
| Dodge & burn | ±2.25 stops, ¼-stop steps | 0 |
| Battery warning | 10% | — |
| Battery poll | every 5 s | — |

## 15.2 Glossary

- **Zone** — a step on the print's tone scale, from 0 (black) to X (paper white).
  Zone V is middle gray.
- **Grade** — the contrast of the paper/filter combination. Higher grade = harder
  (more contrast).
- **Stop / EV** — a doubling or halving of exposure. One stop = 1 EV.
- **Contrast Range** — the brightness range of the negative, in stops.
- **Highlight** — the brightest important part of the print; it comes from the
  **dim** part of the projected image.
- **Shadow** — the darkest important part with detail; it comes from the **bright**
  part of the projected image.
- **Midtone** — the middle of the tone range; the meter anchors exposure there.
- **Calibration constant** — the paper's lux × seconds value. It turns a light
  reading into a time.
- **ISO R** — the paper's contrast range. Higher = softer.
- **ISO P** — the paper's speed. Higher = faster, shorter time.
- **Filter factor** — how many times longer the exposure is through a filter.
- **Dodge / burn** — hold back or add light locally under the enlarger. The
  device's **DODGE & BURN** panel is a whole-print trim.
- **Split grade** — two exposures through a soft and a hard filter.
- **Virtual proof** — a grid preview built from point readings.
- **Uniformity** — how evenly the enlarger lights the easel.
- **Reciprocity** — the loss of paper sensitivity at very long exposures; the meter
  corrects for it automatically.
- **Lux** — the unit of illuminance the sensor measures.
- **Fixed grade** — a paper with one contrast grade; no variable filter.
- **Session** — a saved snapshot of the current readings, grid and settings, kept
  in one of eight numbered slots on the card.
- **Reference paper** — the calibrated paper used as the source for estimates.

## 15.3 Index of controls

| Control or readout | Where |
|---|---|
| **ADDITIONAL TIME** | Exposure, Contrast, Split Grade |
| **ANALYSIS DETAILS** | Split Grade |
| **Auto-Est. All Papers** | Control Panel → Estimate Calibration |
| **Back** | Help Center |
| **Base ISO P** | Control Panel → Paper & Filter Editor |
| **Battery** | Sidebar |
| **Brightness** | Sidebar |
| **CALIBRATION CONSTANT** | Exposure, Contrast, Split Grade |
| **Calibration Lux Value** | Sidebar |
| **Calibration Time Value** | Sidebar |
| **Calibrate Dark** | Control Panel → Sensor Calibration |
| **Calibrate Enlarger Light** | Control Panel → Sensor Calibration |
| **Calibrate Environment Noise** | Control Panel → Sensor Calibration |
| **Calibrate Light** | Control Panel → Sensor Calibration |
| **Clear** | Control Panel → Sensor Calibration |
| **Clear All Calibrations** | Control Panel → Estimate Calibration |
| **Clear Grid** | Virtual Proof |
| **Clipping** | Virtual Proof → Selected Sample |
| **CONTRAST CALCULATOR** | Contrast |
| **CONTRAST GRADE** | Contrast |
| **CONTRAST RANGE** | Contrast, Split Grade |
| **Contrast** (slider) | Contrast, Split Grade → Tunables |
| **Control Panel** | Main tab |
| **DATA MANAGER** | Control Panel |
| **Default** | Control Panel → Filter Values |
| **Density** | Virtual Proof → Selected Sample |
| **Dev % / Dev EV** | Virtual Proof → Enlarger mode |
| **DODGE & BURN** | Exposure, Contrast, Split Grade |
| **Dodge and burn slider** | Exposure, Contrast, Split Grade |
| **Enlarger Mode** | Virtual Proof → Settings |
| **Equivalent grade** | Split Grade |
| **Estimate Calibration** | Control Panel → Estimate Calibration |
| **EV Range** | Virtual Proof → Selected Sample |
| **EXPOSURE CALCULATOR** | Exposure |
| **EXPOSURE TIME** | Contrast |
| **Exposure** (slider) | Contrast, Split Grade → Tunables |
| **Exposure Note** | Contrast |
| **Factor** | Control Panel → Filter Values |
| **Filter Brand** | Sidebar |
| **FILTER GRADE TRANSFORM** | Exposure |
| **Filter Grade** | Contrast; Virtual Proof selector |
| **FILTER VALUES** | Control Panel |
| **F-Stop** | Exposure, Contrast, Split Grade |
| **Fully charged** | Sidebar → Battery |
| **Grid Size** | Virtual Proof |
| **Grid width / height** | Virtual Proof |
| **HARD EXPOSURE** | Split Grade |
| **Help** | Sidebar |
| **Help Center** | Help screen |
| **HIGHLIGHTS** | Contrast, Split Grade |
| **HISTOGRAM** | Virtual Proof |
| **Intergration Time** | Sidebar |
| **ISO P** | Control Panel → Filter Values |
| **ISO R** | Control Panel → Filter Values; Virtual Proof readout |
| **ISO R Range** | Control Panel → Paper & Filter Editor |
| **Lengthening Factor** | Control Panel → Paper & Filter Editor |
| **Load Session** | Control Panel → Data Manager |
| **Load settings** | Control Panel → Data Manager |
| **Lux** | Exposure; Virtual Proof |
| **Match Quality** | Contrast |
| **Measure** | Virtual Proof |
| **Measure Highlight** | Contrast, Split Grade |
| **Measure LUX** | Exposure |
| **Measure Shadow** | Contrast, Split Grade |
| **Start scan (n/total)** / **Stop scan (n/total)** | Virtual Proof with Stability Detection on |
| **Midpoint LUX** | Contrast |
| **Midpoint Time** | Contrast |
| **Midtones** | Split Grade → Tunables |
| **Min Delta (lux)** | Virtual Proof → Settings |
| **Min Stable Reads** | Virtual Proof → Settings |
| **PAPER & FILTER EDITOR** | Control Panel |
| **Paper Brand** | Sidebar |
| **Paper Type** | Sidebar |
| **Range / Mean / Min–Max** | Virtual Proof → Enlarger mode |
| **Reference Paper** | Control Panel → Estimate Calibration |
| **Reset** | Contrast, Split Grade, Control Panel |
| **SafelightIO v.1.0** | Sidebar |
| **Saved per paper** | Contrast, Split Grade |
| **Save Session** | Control Panel → Data Manager |
| **Save Settings** | Control Panel → Data Manager |
| **SELECT ZONE OF MEASUREMENT** | Exposure |
| **Select Filter** | Control Panel → Paper & Filter Editor |
| **SELECTED SAMPLE** | Virtual Proof |
| **Sensor Averaging Samples** | Sidebar |
| **Sensor Gain** | Sidebar |
| **Set Reference** | Virtual Proof → Enlarger mode |
| **Set V Zone** | Virtual Proof |
| **SHADOWS** | Contrast, Split Grade |
| **SOFT EXPOSURE** | Split Grade |
| **Stability Detection** | Virtual Proof → Settings |
| **Tolerance (%)** | Virtual Proof → Settings |
| **TOTAL EXPOSURE TIME** | Split Grade |
| **TOTAL TIME** | Exposure, Contrast, Split Grade |
| **TUNABLES** | Contrast, Split Grade |
| **Uniformity Limit** | Virtual Proof → Settings |
| **Verdict** | Virtual Proof → Enlarger mode |
| **Zone** | Exposure; Virtual Proof readout |

## 15.4 One-page cheat sheet

| I want to… | Do this |
|---|---|
| Get a printing time | Exposure → select paper → zone V → **Measure LUX** → read time |
| Print a shadow at Zone III | Exposure → zone III → measure the shadow |
| Choose a grade | Contrast → measure highlight (dim) and shadow (bright) → read grade |
| Split-grade a contrasty negative | Split Grade → two readings → use soft + hard times |
| Preview the print | Virtual Proof → Grid Size → Measure each cell → read histogram |
| Check the enlarger | Virtual Proof → Enlarger Mode → 3×3 → measure → Set Reference |
| Calibrate a paper | Chapter 10: test strip, enter lux and time |
| Calibrate the sensor | Control Panel → Calibrate Dark, then Calibrate Light |
| Save my work | Control Panel → Save Session; Save Settings for a full backup |
| Update firmware | Press the BOOTSEL hole with a pin, connect USB-C, copy the `.uf2` to **RP2350** |
