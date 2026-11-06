# 13. Messages and troubleshooting

## 13.1 The top bar

| What you see | What it means | What to do |
|---|---|---|
| **No meter** | No dongle, or Android has not granted access | Check the cable and the USB permission |
| **Linking** | The port is open; the app is waiting for `HELLO` | Wait a moment; then **Setup → Meter → Reconnect** |
| **Ready · fw …** | The dongle answered | Normal |
| **No reply** / a short error | The port opened but the dongle did not answer | Unplug, replug, reconnect |
| **Firmware too old** | The dongle cannot list papers | Update the firmware (chapter 14) |

## 13.2 The common refusals

The app quotes the dongle's own sentence. The words are the firmware's, not a
summary.

| Sentence | Meaning | Route |
|---|---|---|
| **select paper** | No paper is in force | Tap the selection bar and choose a paper |
| **calibrate** | The paper has no calibration | Calibrate the paper (chapter 10) |
| **no paper** | The dongle has no paper selected | Choose a paper |
| **no_data** | The paper and brand have no table row for that grade | Choose another grade or brand |
| **bad_arg** | A token the firmware does not accept | Check the value; use the in-app control |
| **measure the highlight and the shadow first** | Contrast/Split needs both readings | Measure both tiles |
| **select a measured cell** | Set V Zone has no valid selected cell | Tap a measured cell |
| **scan already running** | A proof scan is in progress | Wait or Stop |

The **Help & messages** page in the app explains the current sentence and the
route to the fix.

## 13.3 Troubleshooting

### The app never leaves No meter

- Use a data cable, not a charge-only cable.
- Accept the Android USB permission.
- Close any other app that holds the USB port.
- Try another USB-C port or OTG adapter.
- Open **Setup → Meter → Reconnect**.

### The top bar says Ready but there is no paper

- The dongle may have no paper selected; open **Paper & filter**.
- The catalogue read may still be in flight; wait a moment.
- Use **Setup → Meter** to see the firmware and the catalogue state.

### The times are consistently wrong

- Check the sensor calibration: dark and enlarger light.
- Check the paper calibration pair.
- Check that the paper in force is the paper on the easel.
- Check the filter brand and grade; a wrong brand gives a wrong factor.

### Contrast or Split says one spot is missing

- The hint under the tile names the missing spot.
- Meter it; the answer appears when both readings exist.
- A 0.00 lux reading is a real reading, not a missing one.

### The proof grid is empty

- The paper must be selected and the dongle ready.
- Start scan or measure the next cell; the canvas fills as readings arrive.
- If the scan stops early, the remaining cells stay empty; that is a valid
  partial proof.

### A firmware update fails

- Do not unplug until the `RP2350` drive disappears.
- If the update is interrupted, try the 1200-baud touch again.
- If the app no longer starts and the touch does not work, the unit needs a
  service recovery; a sealed unit has no BOOTSEL button. See chapter 14.

---

# 14. Firmware updates

## 14.1 Check your version

The top bar shows **Ready · fw 0.11** (or your version). **Setup → Meter** shows
the firmware, protocol, board and serial number. Write the version down before
an update.

## 14.2 Update with the 1200-baud touch

The dongle has no BOOTSEL button. Its USB serial stack supports the standard
Pico 1200-baud touch: opening the port at 1200 baud asks the running firmware to
reset into the RP2350 ROM bootloader. The ROM exposes the **RP2350** USB drive.

![Firmware update: 1200-baud touch, RP2350, UF2](manual/figures/fig-firmware-update.svg)

1. Save any Session file you need. The update does not change the paper
   catalogue or the calibrations, but a backup is cheap.
2. Plug the dongle into the computer with a data cable.
3. Open the dongle's serial port at **1200 baud** and close it.
   - macOS: `screen /dev/cu.usbmodem* 1200`, then quit.
   - Windows: a terminal program with the COM port set to 1200.
   - Linux: `stty -F /dev/ttyACM0 1200`, then close.
4. Wait for the **RP2350** drive to appear.
5. Copy the new `.uf2` onto that drive.
6. Wait until the drive disappears. Do not unplug during the copy.
7. Reconnect the dongle to the phone; the top bar should return to **Ready**
   with the new version.

No SDK or Picotool is required on the computer. The 1200-baud touch is a
feature of the firmware's USB serial stack, not a separate program.

> [!WARNING] No button, no easy recovery
> The 1200-baud touch only works while the current firmware runs. If an update
> is interrupted, the app may no longer start and the touch may not respond.
> The unit then needs a service recovery. Keep the cable connected until the
> `RP2350` drive disappears, and do not update on a low phone battery or a
> flaky hub.

## 14.3 What is kept

The firmware update replaces the program, not the paper catalogue or the
calibrations. The dongle's persistent records are kept. The phone's Settings
and Session files are not touched.

If the update includes a storage-format change, the release notes will say so;
read them before updating.

## 14.4 If the update does not start

- Check the cable is a data cable.
- Close the app on the phone; the phone and the computer cannot both own the
  port.
- Try another serial terminal; the port name changes each time the dongle
  reconnects.
- If the port opens but no `RP2350` appears, the firmware may not be running;
  see the warning above.

---

# 15. Reference

## 15.1 Ranges and defaults

| Control | Range | Default |
|---|---|---|
| Zone | 0–X | V |
| Filter grade | The paper/brand table | None |
| Burn | ±2.25 stops in ¼-stop steps | 0.00 |
| Contrast/Split trims | ±1.50 stops in ⅙-stop steps | 0.00 |
| Sensor gain | Auto, Low, Med, High, Max | Auto |
| Integration time | 100–600 ms | 200 ms |
| Averaging samples | 1–16 | 5 |
| Proof grid | 1–40 columns, 1–30 rows | 3 × 3 |
| Proof stability | On/off | From the dongle |
| Proof uniformity limit | 0.5–99.5% | 15% |

## 15.2 Glossary

**Calibration constant** — the paper's lux × time product; the number the meter
divides by the light reading.

**Contrast** — the tool that reads a highlight and a shadow and returns a time
and a grade.

**Dongle** — the USB meter: sensor, RP2350, catalogue and records. It has no
screen.

**Exposure** — the one-spot tool: choose a zone, measure, get a time.

**Filter brand** — the manufacturer of the variable-contrast filter; the brand
selects the grade table.

**Filter grade** — the contrast grade, such as 2xM1; chosen on Exposure, stored
on the dongle.

**Fine tune** — the collapsed Contrast/Split card holding the four trims and the
burn.

**Paper calibration** — the one-time test-strip pair that gives the paper its
constant.

**Proof** — the grid tool that previews the print, or in Enlarger Mode checks
the light's evenness.

**Split** — the two-filter tool: a soft time and a hard time from the same two
spots.

**Trim** — a per-paper, per-tool adjustment to exposure, contrast, highlights
or shadows.

## 15.3 Index of controls

| Control | Where | What it does |
|---|---|---|
| **Exposure / Contrast / Split / Proof / Setup** | Bottom navigation | Switches tool |
| Paper and brand bar | Under the top bar | Opens **Paper & filter** |
| Meter state | Top right | Opens **Setup → Meter** |
| **Measure** | Exposure | One sensor reading and a compute |
| **Highlights / Shadows** | Contrast, Split | Capture the two spots |
| **Measure** in a capture tile | Contrast, Split | Measures that spot |
| **Fine tune** | Contrast, Split | Opens the trims and burn |
| **Reset** | Contrast, Split | Neutralises the trims (and the Midtones pair on Split) |
| **Dodge & Burn** | Exposure, Contrast, Split | Global quarter-stop burn |
| **Start scan / Stop** | Proof | Runs or stops the grid scan |
| **Set V Zone / Set Reference** | Proof | Anchors the selected cell |
| **Clear Grid** | Proof | Clears the grid |
| **Columns / Rows** | Proof | Grid size |
| **Filter brand** | Paper & filter | Chooses the brand rail |
| Paper brand row | Paper & filter | Opens the paper list |
| **Gain / Integration time** | Setup → Sensor | Sensor rails |
| **Averaging samples** | Setup → Sensor | Number of samples |
| **Known lux / Known time** | Setup → Calibration | Paper calibration pair |
| **Calibrate Dark / Calibrate Enlarger Light** | Setup → Sensor → Sensor Calibration | Sensor calibration |
| **Save / Load Settings / Session** | Tools & data → Data Manager | Phone files |
| **Reconnect** | Setup → Meter | Reopens the USB port |

## 15.4 One-page cheat sheet

1. **Connect:** dongle → phone; allow USB; wait for **Ready**.
2. **Choose:** selection bar → Filter brand, then paper.
3. **Exposure:** zone rail → V; **Measure**; use the time and grade.
4. **Contrast:** meter **Highlights**, then **Shadows**; use **Time** and
   **Grade**.
5. **Split:** the same two spots; use **Soft** and **Hard**; **Midtones** in
   **Fine tune**.
6. **Proof:** set the grid; **Start scan**; tap a cell; read **Result**.
7. **Calibrate:** sensor first, then paper; one test strip sets the constant.
8. **Update:** open the serial port at 1200; copy the UF2 to **RP2350**; wait.

> [!TIP] If in doubt
> The app's **Help & messages** page quotes the dongle's own refusal and the
> route to the fix. The **Setup → Meter** page is the first place to look when
> the connection is not **Ready**.
