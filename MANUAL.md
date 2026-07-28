<small>

# Darkroom Exposure Meter — User Manual

A tablet-sized companion for black-and-white enlarger printing. Point the sensor at the easel, choose the paper you’re about to print on, and the meter tells you how long to expose, which contrast grade to use, and how a tricky negative will distribute across the paper before you commit to it.

---

## 1. Quick start

1. Power the device on. A splash screen appears with an inspirational photography quote and a practical darkroom tip, then the Main Screen opens with five tabs: Exposure, Contrast, Split Grade, Virtual Proof, Filter Editor, plus a Settings panel (paper, sensor, calibration, brightness).
2. In Settings, choose **Paper Brand**, **Paper Type**, and **Filter Brand** (the filter system you use in your enlarger head).
3. The first time you use a paper, do §7 Calibrating a new paper.
4. On the Exposure tab, place the sensor where you want the midtone on the easel, press Measure, read the suggested time.

---

## 2. The light sensor

A light sensor reads the light at the easel and reports it in lux (the SI unit of illuminance — how bright a surface is). Three controls govern how each reading is taken.

| Control | What it does | When to change it |
|---|---|---|
| **Gain** (LOW 1× / MED 25× / HIGH 428× / MAX 9876×) | Amplifies the sensor signal. | Default **MED** suits a typical enlarger at f/8–f/11. Drop to **LOW** if a reading pegs (saturates). Raise to **HIGH/MAX** for very dim scenes (small apertures, deep shadows). |
| **Integration Time** (100–600 ms) | How long each individual reading lasts. Longer is quieter but slower. | Default **200 ms**. Raise for noisy low-light scenes; lower (100 ms) when you want a Virtual-Proof auto-scan to fly through cells. |
| **Sample count** (1–16) | How many readings to average each time you press *Measure*. | Default **5**. Increase for very low light or to even out lamp flicker. |

> Treat the sensor like a real spotmeter — shield it from stray room light (even red safelight) and only press Measure with the enlarger lamp on.

### 2.1 Backlight dimming during readings

The LCD backlight can contaminate light-sensor readings in a darkroom. Every time you press **Measure** (on any tab), the screen automatically dims to 10% brightness before the sensor is read, then restores to your chosen brightness afterward. This happens transparently — you may notice the screen flicker briefly, especially during long sample sequences. There is no setting to disable this; it is always active to ensure accurate lux readings.

### 2.2 Sensor calibration (one-time per device)

Two pairs of buttons in the Sensor panel:

- **Sensor Offset Calibration** / **Clear Offset** — the dark-current baseline. The sensor captures the electrical noise floor for the current gain and integration time (24 per-gain, per-integration slots are stored). Sensor must be in **real darkroom printing conditions, total darkness** when you press it (sensor open on easel, head off, lights and safelight off). Takes a few seconds. Persisted automatically. Do once, redo only if drift suspected.
- **Sensor Light Calibration** / **Clear Light Cal** — per-device gain-stage trimming. The sensor walks all four sensor gain stages under a **steady, moderate light** — bright enough that MED registers but not so bright MED saturates — and measures the real gain ratios so lux readings agree across sensor gains. Takes several seconds. Run once per device; re-run if readings disagree when you switch gain.

Status messages (e.g. "dark calib…", "gain cal set", "dark calib failed") appear on every tab's lux label simultaneously, so you don't have to be on a particular tab to see the result.

> **Tip:** If you ever see readings that don't agree when you switch gain (e.g. MED says 2.00 lux but HIGH says 1.50 lux on the same scene), run Sensor Light Calibration. If readings drift upward in very low light, re-run Sensor Offset Calibration in complete darkness.

---

## 3. Exposure tab — printing-time suggester

The everyday tool. Once a paper is calibrated, point the sensor at the easel and the device gives you the time. You can use this tool with fixed and variant grade papers. Always take readings without contrast filter.

### 3.1 What every element does

| Element | Purpose |
|---|---|
| **Paper Brand / Paper Type** dropdowns | Pick the emulsion you're about to print on. The two are dependent: choosing a brand repopulates the type list. |
| **Filter Brand** dropdown | Choose which contrast-filter system is in your enlarger head. **Ilford Multigrade** (grades 00–5), **FOMA Variant** (Y/M notation), or colour-head filters (**AGFA**, **KODAK**, **DURST**, **MEOPTA**). The meter works cross-brand — you can use Ilford filters with FOMA paper, and vice versa. The filter tables come from manufacturer datasheets. |
| **Calibration Lux** spinbox | Lux you measured during your reference test print. |
| **Calibration Time** spinbox | Seconds that produced the “correct” test print at that lux. |
| **Calibration Constant** | Derived from the two boxes above. This is the per-paper number the device actually stores and uses. Larger = darker paper. |
| **Measure** button | Take an averaged lux reading right now. |
| **Lux Number** | The most recent live reading. |
| **Zone dropdown** (0–X) | Which Zone System zone you are measuring. Default is **Zone V** (middle gray). Change this when you meter a shadow (Zone III) or highlight (Zone VII) instead of a midtone — the meter scales the reading to its Zone V equivalent automatically (§3.2). With this feature you can measure a cloud, select Zone VII and you will get the exposure time to achieve Zone VII at the cloud. |
| **Filter Grade Transform** dropdown |  Transform the exposure time with the lengthening factor of the selected contrast filter. |
| **F-Stop Transform** slider (−9 … +9) | Push or pull the time in ⅓-stop increments. Right = more exposure (darker print), left = less. ±9 covers ±3 stops. |
| **Exposure Time** | The final number, in seconds. While anything is missing, this label tells you what to do (`calibrate` → no calibration yet; `measure lux` → press Measure). |

### 3.2 Overall logic

The calibration spinboxes describe one print you already know works. Internally the device boils them down to a single per-paper constant. Once that constant exists, any new lux reading from the easel translates directly into a print time. Changing the filter dropdown multiplies the time by that filter’s exposure factor; the F-Stop slider applies an additional ⅓-stop push/pull on top.
Calibration is stored per paper — switch paper and the meter instantly reloads the calibration for that emulsion. Edits to the spinboxes are written to flash about 1.5 s after you stop tapping, so rapid +/- presses coalesce into one save.
#### Zone correction — measuring any tone

The **Zone dropdown** lets you meter any tonal area — not just midtones. The classic exposure formula assumes you are measuring a Zone V (middle gray) tone. When you meter something else (a shadow, a highlight, a black shirt), pick its zone from the dropdown and the meter does the rest.

| Zone | Example subject tone | Multiplier |
|---|---|---|
| 0 | Maximum black (paper Dmax) | ×32 |
| I | First discernible shadow detail | ×16 |
| II | Deep shadow with texture | ×8 |
| III | Dark shadow — black hair, dark foliage | ×4 |
| IV | Shadow side of a portrait | ×2 |
| **V** | **Middle gray (18% card) — default** | ×1 |
| VI | Caucasian skin tone | ÷2 |
| VII | Light concrete, snow with detail | ÷4 |
| VIII | White with texture — wedding dress | ÷8 |
| IX | Glossy white — paper base white | ÷16 |
| X | Specular highlight / light source | ÷32 |

**Example:** You meter a dark shadow (Zone III) and read 0.25 lux. With the zone set to III, the meter internally scales to 0.25 × 4 = 1.00 lux (Zone V equivalent), then calculates the time from that. If you had left the zone at V, the meter would assume the shadow IS a midtone and recommend a print that is far too dark.

You calibrated the paper at Zone V. As long as the Zone dropdown correctly describes whatever you are pointing at, the calibration stays valid no matter what you measure.
#### Cross-brand filter compatibility

The meter ships with six filter brands: **Ilford Multigrade** (0–5), **FOMA Variant** (Y/M notation), plus four colour-head systems (**AGFA**, **KODAK**, **DURST**, **MEOPTA**). Choose your filter brand in the Settings panel. The meter automatically loads the correct filter factors, ISO R values, and gamma data for whichever paper + filter-brand combination you're using. You can use Ilford under-the-lens filters with FOMA paper, FOMA filters with Ilford paper, or dial in a colour head with any paper — the database has cross-compatibility data for all 22 papers × 6 filter brands.
### 3.3 Workflow example

> *Portrait shot on FP4, printing on Ilford MG Classic Cooltone.*
>
> 1. In Settings, choose **Ilford / MG Classic Cooltone**.
> 2. If this paper has never been calibrated, do §7 Calibrating a new paper first.
> 3. Tab to **Exposure**. Stop the lens to f/11. Place the sensor on the easel where the model's cheek will fall (Zone VI — caucasian skin). Set **Zone dropdown** to **VI**.
> 4. Press **Measure**. Lux Number reads 2.84 lux. The meter scales to its Zone V equivalent (2.84 ÷ 2 = 1.42 lux) internally. Exposure Time label updates to 8.80 s.
> 5. Grade **3** looks right from the contact sheet — pick **3** in the filter dropdown. Time updates to **~10.2 s**.
> 6. Print. It’s ⅓ stop too light. Pull **F-Stop Transform** to +3 (one stop more); Exposure Time becomes ~12.85 s. Print again.

---

## 4. Contrast tab — Contrast Analyzer

Spotmeter the brightest area, spotmeter the darkest area, the device tells you the grade to use and a single exposure time that puts both ends where you want them. You can use this tool with fixed and variant grade papers. Always measure without contrast filter.

### 4.1 What every element does

| Element | Purpose |
|---|---|
| **Measure Highlight** | Average-read the easel, tag the result as the highlight zone. |
| **Measure Shadow** | Same, tagged as the shadow zone. |
| **Highlight Lux / Shadow Lux** | The two lux readings. Until both are present, every result label shows -- and the suggested-time label tells you which one is missing. |
| **ΔEV Display** | The subject contrast range, in stops. (3 stops ≈ a fairly contrasty negative; 5 stops ≈ extreme.) |
| **Recommended Grade** | The VC filter grade the meter recommends for this negative on this paper. |
| **Match Quality** | How well that grade fits — Exact, Close, Acceptable, or Approximate. Acceptable/Approximate means the negative isn’t a great match for any single grade — consider Split Grade or local control. |
| **Analysis Reasoning** | One-line explanation. If the negative exceeds the paper’s range, this is where you’ll see “negative exceeds paper range — consider split-grade printing, pre-flashing, or dodging/burning” or “negative is flatter than paper range — softest grade still prints with reduced contrast”. |
| **Suggested Exposure Time** | Single midpoint exposure time, in seconds. Includes the chosen filter’s factor. |
| **Midpoint Lux** | The “true midtone” brightness implied by your two readings. |
| **Meter Calibration Value** | The paper’s calibration constant after the Overall-Offset slider. Lets you check the slider is doing what you expect. |
| **Exposure Note** | Tells you whether long-exposure reciprocity-failure correction was applied and how much it added. |
| **Overall Offset** slider (±1.5 stops) | Push or pull the whole suggested time without changing the grade. |
| **Contrast Bias** slider (±1.5 stops) | Bias the grade selection. Positive → recommends a harder grade; negative → softer. Use it when you consistently disagree with the recommendation in one direction or you want different aesthetics. |
| **Highlight Trim** slider (±1.5 stops) | Treat the highlight as if it had received more (+) or less (−) exposure on the negative. Affects both contrast grade and time in order to have the perfect exposure on shadows and highlights. |
| **Shadow Trim** slider (±1.5 stops) | Same for the shadow. |
| **Reset** button | Zero all four sliders for the current paper. |

The four sliders persist **per paper**, alongside calibration. Dial in your preferences for FOMA Variant III, then switch to Ilford MG and dial in different ones — they’ll each come back when you reselect that paper. Each slider step is 1/6 of a stop, so the labels read in increments like +0.17 / +0.33 / +0.50 stops.

### 4.2 Overall logic

The Contrast Analyzer asks two questions:

1. **Which grade?** The contrast range between highlight and shadow, after any Contrast Bias, is matched against the paper’s filter table — the grade whose contrast (ISO R) is closest to the negative’s range wins.
2. **For how long?** The meter takes two readings (the "true" midpoint), feeds it into the paper's calibration constant, and multiplies by that filter's exposure factor. Long exposures get an automatic reciprocity-failure correction — papers under-respond when exposed for a long time at low intensity, so the meter lengthens those exposures using a Schwarzschild model. Resin-coated (RC) papers use an exponent of ~0.07; fibre-base (FB) papers use ~0.10 which produces a stronger correction. The reference time is 10 seconds. When reciprocity correction is applied, the Exposure Note field tells you how much time was added.

If the negative is too contrasty for the paper, the recommendation pegs at the softest grade and the Reasoning warns you. Too flat — pegs at the hardest grade with a similar warning. In both cases you’ll get a better print with the **Split Grade** tab.
#### Fixed-grade papers

Fixed-grade papers (e.g. FOMA FOMASPEED Normal) have a single built-in contrast — there is no filter to change. For these papers:
- The Contrast tab shows the grade as "Fixed grade" and still calculates a midpoint exposure time from your two readings.
- Highlight/Shadow trim sliders are ignored (there is no contrast to adjust).
- The Split Grade tab is not applicable — use the Contrast tab instead.
- In the Filter Editor, the Factor and ISO R spinboxes are disabled (greyed out) and the default labels read "Fixed-grade paper" / "ISO R & Factor fixed at manufacture". Only ISO P can be adjusted.

The built-in database includes one fixed-grade paper: **FOMA FOMASPEED Normal**. You can add more via the custom paper registration system (§10.3).
### 4.3 Workflow example

> *Backlit landscape — bright sky, deep foreground shadow.*
>
> 1. Compose and focus on the easel. Place the sensor on the **brightest
>    cloud** area, press **Measure Highlight** → `4.10 lux`.
> 2. Move the sensor to the **deep shadow** of the foreground, press
>    **Measure Shadow** → `0.32 lux`.
> 3. ΔEV reads `3.68 stops`. Recommended Grade `1` (Close). Suggested
>    Exposure Time `14.20 s`. Reasoning warns the negative sits at the soft
>    end of the paper’s range.
> 4. You want more punch in the trees. Pull **Contrast Bias** to +0.5 stops or until the contrast grade filter changes, then the grade jumps to `2`, time updates.
> 5. The sky is going gray. Pull **Highlight Trim** to -0.3 stops (telling the meter “the highlight received plenty of exposure on the negative”); suggested time drops slightly to keep highlights in Zone I.
> 6. Run the print at the suggested time. Burn the corners by eye.

---

## 5. Split Grade tab — Split-grade calculator

Two readings, two filter changes during the exposure, a print that holds both ends. Use this when the Contrast tab says "negative exceeds paper range" — or any time you'd normally split-grade by feel. You can only use this tool with variant grade papers. Always measure without contrast filter. Long total times get automatic reciprocity correction.

### 5.1 What every element does

| Element | Purpose |
|---|---|
| **Measure Highlight / Measure Shadow** | Same as the Contrast tab, but stored separately for the split calculation. |
| **Split Highlight Lux / Shadow Lux** | The two lux readings. |
| **ΔEV** | Subject contrast range in stops, identical definition to the Contrast tab. |
| **Equivalent Grade** | The single VC grade that would have produced the same overall midtone if the negative had fit on one grade — useful as a sanity reference. |
| **Analysis Reasoning** | The split, expressed as a percentage of each filter (e.g. “65% 00 / 35% 5”), plus any trim, reciprocity, or out-of-range note. |
| **Soft Filter Name / Soft Time** | Which soft filter to use (e.g. 00 or 2× Y) and how many seconds to expose with it. |
| **Hard Filter Name / Hard Time** | Same for the hard filter (e.g. 5 or 2× M2). |
| **Total Time** | Soft + Hard, the total bulb-on time the print sees. |
| **Meter Calibration Value 2** | Effective calibration constant after Overall Offset (matches the Contrast tab’s same-named field). |
| **Overall Offset** slider (±1.5 stops) | Push/pull the total time without changing the soft/hard ratio. |
| **Contrast Bias** slider (±1.5 stops) | Bias the equivalent-grade calculation, which in turn shifts the soft/hard ratio. Positive → more hard filter. |
| **Soft Trim** slider (±1.5 stops) | Push/pull the soft leg only — gives you more (or less) shadow detail. |
| **Hard Trim** slider (±1.5 stops) | Push/pull the hard leg only — gives you more (or less) highlight contrast. |
| **Reset** button | Zero all four split sliders for the current paper. |

Like the Contrast trims, these four sliders persist **per paper**. They are a separate set from the Contrast-tab trims — you can have different bias and trims for the two analyzers on the same emulsion.

### 5.2 Overall logic

Each paper publishes a soft filter and a hard filter. The meter computes how much of the total exposure should happen under each, given the negative’s brightness range and the paper’s contrast endpoints. The midtone time is anchored at the geometric mean of the two readings (so the print midtones land where you’d expect from the calibration), and that total time is then split into the two legs in the proportion the math demands.
Long total times are corrected for reciprocity failure automatically (see §4.2 for details on the Schwarzschild model), and the two legs scale together so the soft/hard ratio stays the same.
When the negative is so contrasty that the equivalent grade exceeds the paper’s softest filter, the Reasoning warns “highlights may burn” and the soft leg gets most of the time. When it’s too flat, you’ll see “limited contrast” and the hard leg dominates.

### 5.3 Workflow example

> *High-contrast portrait — bright window backlight, dark hair against shadow.*
>
> 1. Tab to **Split Grade**. Measure Highlight on the window glare:
>    `5.80 lux`.
> 2. Measure Shadow on the hair detail: `0.18 lux`.
> 3. ΔEV = `5.01 stops`. Equivalent Grade *0* (Close), Reasoning warns
>    *“highlights may burn”*.
> 4. Split times: Soft **00** → `34.2 s`, Hard **5** → `1.1 s`,
>    Total `35.3 s`.
> 5. Print: drop in the 00 filter, expose 34.2 s; swap to the 5 filter,
>    expose 1.1 s. Develop, fix, evaluate.
> 6. Shadows look gray. Pull **Hard Trim** to -0.5 stops; the Hard time rises to ~0.78 s. Reprint.

> **Tip.** If one leg is wildly bigger than the other, the negative is genuinely outside the paper’s contrast range. Consider pre-flashing, dodging the highlight, or picking a different paper.

---

## 6. Virtual Proof tab — characteristic-curve preview

Sweep the easel and the device paints a grayscale preview of the print — cell by cell, on the chosen paper, at the chosen grade — before you commit a sheet to it.

### 6.1 What every element does

| Element | Purpose |
|---|---|
| **Grid Width / Grid Height** spinboxes | Number of cells across × down (2..40 × 2..30). More cells = finer preview, longer to scan. Changing the size **wipes** the grid. |
| **Proof Grid (the canvas)** | One block per cell, painted with the predicted gray. Cells with a coloured frame are special: **amber** = next cell to read, **red** = your selection, **cyan** = Zone V reference, **light gray** = highlight clipping, **dark gray** = shadow clipping, no frame = ordinary measured (or empty) cell. |
| **Measure Next Cell** button | Read one cell at the cursor and advance. When **Stability Enabled** is ON, this button becomes **Start Scan / Stop Scan** and the device walks the grid for you. |
| **Set Zone V Reference** button | Use the currently selected cell as the “middle gray” anchor; every other measured cell is re-derived in relation to it. |
| **Recompute Preview** button | Re-run the preview for every measured cell. Use after switching paper, switching the preview filter grade, or recalibrating. |
| **Clear Grid** button | Erase all samples, the selection, and the reference. |
| **Stability Enabled** switch | Turn on automatic settle detection so a scan records each cell only when its reading has stopped changing. |
| **Stability Tolerance** (%) | Two consecutive reads must agree within this percentage to count as “stable”. |
| **Stability Min Delta** (lux) | A floor on Tolerance. In very dim cells, a strict percentage gets unreasonably tight; this gives it some absolute breathing room. |
| **Stability Min Stable** | How many consecutive stable reads before the cell is recorded. |
| **Stability Max Wait** (ms) | After this long without settling, the cell is recorded anyway so the scan doesn’t stall. |
| **Filter Grade** dropdown | The grade the preview is rendered for. Changing it re-renders every cell. |
| **Histogram** (proofHistogram) | 10 Zone distribution of the predicted print tones — a fast read on "does the print sit mostly in shadows / midtones / highlights?". |
| **Selected-sample readouts** (Lux / Zone / ISO R / EV Range / Density / Exposure / Clipping) | Detail on whichever cell is red-framed. With nothing selected, the *Clipping* slot turns into a global verdict: *"Negative too contrasty"* / *"too flat"* / *"-- "*. |

### 6.2 Overall logic

Each measured cell is run through the paper’s published characteristic curve (toe → straight line → shoulder) and rendered as a grayscale block. The filter you choose changes the curve’s steepness, the same way a real filter does in the enlarger head — so a softer grade flattens the preview, a harder grade steepens it. Cells whose brightness fell outside the paper’s range get a coloured frame to flag them as clipped (highlight or shadow).
The Zone V reference is what anchors the tonal scale. With no reference set, each cell is rendered as if it were itself Zone V (i.e. middle gray) — which isn’t very useful for comparing cells. Set one cell as Zone V (or let the auto-scan pick the average for you) and the whole preview falls into place.
Cells are walked in a snake order — left to right on row 1, right to left on row 2, and so on — so you don’t have to keep jumping the sensor back to the left edge.

### 6.3 Auto-scan settling

When **Stability Enabled** is on, the device repeatedly samples the current cell and waits for the reading to stop moving. When the reading has been stable for Min Stable consecutive samples (or Max Wait has elapsed), it records and advances. The four Stability spinboxes let you tune this for your enlarger and lamp — slower lamps and dim cells want larger Min Delta and longer Max Wait. When the whole grid finishes, the meter automatically picks the average-brightness cell as Zone V so the preview is meaningful right away.

### 6.4 Workflow example

> *Evaluating whether a tricky negative will fit on FOMA Variant III before
> wasting paper.*
>
> 1. Tab to **Virtual Proof**. Set grid to **16 × 12** (192 cells).
> 2. Choose **2** in the Filter Grade dropdown — your usual starting grade.
> 3. Turn **Stability Enabled** ON. Press **Start Scan**.
> 4. Sweep the sensor methodically across the easel, top-to-bottom. Pause
>    briefly at each cell — the meter records and advances on its own. The
>    button label updates to *“Stop scan (47/192)”*, *“(48/192)”*, ….
> 5. When the scan completes, Zone V is set automatically; the preview is
>    fully painted; the histogram fills in.
> 6. Tap a midtone cell on the canvas — last-sample readout shows
>    `Zone: 5.1`, `Density: 0.62`, `Exposure: 8.40 s`, `Clipping: none`.
> 7. Tap a highlight cell with the light-gray frame — readout says
>    `Clipping: highlight`. You pick **2** in the Filter Grade dropdown
>    and press **Recompute Preview**: the highlight un-clips, the shadows
>    deepen slightly, the histogram shifts left.
> 8. Tap empty space to clear the selection — the Clipping slot now shows
>    *“Negative too contrasty”*. Time to consider Split Grade or
>    pre-flashing.

---

## 7. Calibrating a new paper

Do this **once per emulsion**. The whole device hinges on one stored
number per paper — without it, the Exposure tab shows `calibrate`, and the
Contrast / Split / Virtual Proof tabs report `--` everywhere.

### Procedure

1. Pick the paper in the Brand / Type dropdowns.
2. Set up the enlarger as you would for a real print: lens stop, head
   height, focus. **These must stay the same when you use the meter
   later** — change any of them and you’re reading a different scene.
3. Place a **mid-toned, flat negative** in the carrier (you can use a
   negative with a gray card photographed or color checker to compare it
   with the printed tone).
4. Remove any contrast filter from the enlarger. Every reading must be
   made with no filter grade.
5. Place the sensor on the **middle gray point** on the easel where the
   print will be. Press **Measure** on the Exposure tab. Note the lux.
   Don't move the sensor until you've also done the next step.
6. Make a **test strip** and develop fully. Pick the strip section whose
   midtone is exactly right. Note its exposure time in seconds.
7. Type that **lux** into **Calibration Lux** and that **time** into
   **Calibration Time**. The Calibration Constant label updates immediately.
   The value is written to flash about 1.5 s after your last edit.

From now on, every tab on this paper will produce real numbers. To re-calibrate (different developer, new lens, lost confidence in the old calibration), simply overwrite the two spinboxes.

> **Why two boxes and not one constant?** So you can re-enter the things you
> actually measured (a lux number and a time) instead of computing a constant
> yourself. The device handles the multiplication.

---

## 8. Settings panel (visible alongside the tabs)

- **Paper Brand / Paper Type** — global; every tab uses the current selection.
- **Filter Brand** — which filter system is in your enlarger head. Choices: Ilford Multigrade (0–5), FOMA Variant (Y/M), AGFA, KODAK, DURST, MEOPTA. Cross-brand compatible — see §3.2.
- **Calibration Lux / Calibration Time** — see §7.
- **Sensor Gain / Integration Time** — see §2.
- **Sample count** — averaging for every Measure press on every tab.
- **Sensor Offset Calibration / Clear Offset** — dark-current baseline, §2.2.
- **Sensor Light Calibration / Clear Light Cal** — gain-stage trim, §2.2.
- **Brightness** slider (1–100) — LCD backlight. The bottom step keeps the panel just lit (no risk of accidentally blanking the screen); the top step is bench-light brightness.
- **Battery Bar** — red bar in the corner, updates once a minute. See §8.1 for charging behaviour.

### 8.1 Battery, charging & power

The device runs from a LiPo battery. The battery bar shows the discharge percentage (16-point curve, load-sag compensated). Three states are shown:

| State | What you see |
|---|---|
| **Discharging** | Red percentage bar |
| **Charging** (USB plugged in) | Orange "Charging…" label — the bar is hidden because voltage readings are unreliable during charge |
| **Fully charged** | Green "Fully charged" label |
| **Battery absent** | Grey, empty bar |

#### Auto-dormant battery protection

When the battery falls to **10%**, the device automatically enters dormant sleep to protect the LiPo from over-discharge (which can permanently damage the cell). The screen goes dark and the MCU enters its lowest-power state. Auto-dormant is rate-limited to once every 60 seconds so it won't repeatedly trigger if the battery voltage bounces near the threshold.


#### Device power and charging

- Press the **Power Button** at the top right corner of the device to power on by battery.
- Plug a USB-C cable at the left side of the device to power on with external power.
- Plug a USB-C cable at the left side of the device while it is powered on to charge the battery.

---

## 9. Filter Editor tab — customising filter data

The Filter Editor lets you override the built-in filter factors, ISO R values, and paper base speed (ISO P) for any paper + grade combination. All edits persist to flash and survive power cycles. Every other tab uses the effective (overridden) values in its calculations. You can use this tool with fixed and variant grade papers.

### 9.1 What every element does

| Element | Purpose |
|---|---|
| **Filter Grade** dropdown | Pick the grade you want to edit (e.g. "00", "2", "5", "2× Y"). The list is populated from the current paper + filter brand. |
| **Current factor / Current ISO R** labels | Show the **effective** values — your override if one exists, otherwise the built-in default. These are what every other tab uses in its calculations. |
| **Default Factor / Default ISO R** labels | Show the **built-in** factory values from the paper database. Use these as a reference to see how far you've deviated. |
| **Factor spinbox** | Edit the filter's exposure multiplier (e.g. 2.08 for a grade 2 Ilford filter). Two decimal places. Set to 1.00 to effectively remove the filter factor. |
| **ISO R spinbox** | Edit the contrast range this filter grade produces on this paper (e.g. 110 for grade 2). Higher ISO R = softer contrast. Changing ISO R directly affects grade matching in the Contrast and Split Grade tabs. |
| **ISO P spinbox** | The paper's base unfiltered speed. Default is 500 for Ilford MG papers. Raising ISO P makes the meter suggest shorter times; lowering it suggests longer times. This is a **per-paper** setting (not per-grade). |
| **Reset to defaults** button | Clear **all** overrides for the current paper (factors, ISO R values, and ISO P) and restore the built-in database values. |
| **Base ISO P** label | Shows the current effective ISO P for the paper. |

### 9.2 When to use the Filter Editor

- **Your filter set doesn't match the datasheet.** Old filters fade and shift — measure their actual factor with a step wedge and enter the real number here.
- **You want a different paper speed.** Maybe your developer runs warm, or you prefer slightly lighter prints — bump ISO P up or down.
- **You're dialling in a new paper** that isn't in the built-in database. Use a similar paper as a starting point and tweak the ISO R and factor values per grade.
- **Cross-brand filter fine-tuning.** Using Ilford filters on FOMA paper? The built-in cross-brand data is based on published tech specs, but your specific setup may benefit from small adjustments.

### 9.4 Advanced calibration tools — cross-paper estimation

The Filter Editor also contains four buttons that help you calibrate multiple papers quickly by leveraging the ISO P speed rating. These appear below the spinboxes.

| Button | Purpose |
|---|---|
| **Set as Ref** | Snapshot the currently selected paper's calibration (lux + time + ISO P) as a reference template. The reference label updates to show which paper is the source. |
| **Est. Cal from ISO P** | Estimate a calibration for the currently selected paper, using the stored reference, scaled by ISO P speed ratio. Requires a reference to be set first. |
| **Auto Estimate All** | Apply the reference calibration to **every** paper that isn't already calibrated, scaling each by its ISO P speed ratio. Already-calibrated papers are skipped. |
| **Clear All Calibrations** | ⚠️ **DANGEROUS** — Irreversibly wipes every paper's calibration (lux + time) back to uncalibrated. Also clears the reference snapshot. **No confirmation dialog.** Only use this when you want to start completely fresh. |

#### How cross-paper estimation works

Every paper has a manufacturer-rated ISO P speed (visible as "Base ISO P" in the Filter Editor). Faster papers (higher ISO P) need less exposure for the same density. The estimation tools exploit this:

1. Calibrate **one** paper properly (§7) — this becomes your anchor.
2. Press **Set as Ref** on the Filter Editor tab to snapshot it.
3. Select a different (uncalibrated) paper, press **Est. Cal from ISO P**. The meter computes what the calibration *would* be if that paper had been used in the same enlarger setup, scaled by the speed ratio.
4. For bulk setup, press **Auto Estimate All** to populate every paper at once.

> **Important:** ISO-P-based estimation is approximate. For critical work, do a real test-strip calibration (§7) on each paper you use regularly. The estimation tools are best for getting a reasonable starting point on papers you use occasionally.

#### Workflow example

> *You've calibrated Ilford MG FB Classic with a test strip. You want a rough calibration for FOMA FOMABROM without burning another sheet.*
>
> 1. With **Ilford / MG FB Classic** selected, go to Filter Editor → press **Set as Ref**. The label shows: *"Ref: Ilford MG FB Classic (ISO P 500, 1.42 lux × 8.8 s)"*.
> 2. Switch to **FOMA / FOMABROM VARIANT** in Settings.
> 3. Go to Filter Editor → press **Est. Cal from ISO P**. The label updates: *"Ilford MG FB Classic -> FOMABROM VARIANT (ISO P 500→130, ×3.85, est. 33.9 s)"*.
> 4. The calibration spinboxes in Settings are now pre-filled with the estimated values. You can refine them later with a real test strip.

### 9.5 Workflow example (override)

> *Your old Ilford grade 2 filter has faded and prints need more time than the meter suggests.*
>
> 1. Tab to **Filter Editor**. Choose **Ilford / MG FB Classic**. The grade dropdown shows all grades.
> 2. Select **2** from the grade dropdown. Current factor shows `2.08` (default).
> 3. You've measured that your actual grade 2 filter needs 20% more exposure. Increase the factor spinbox to `2.50`.
> 4. Switch to the **Exposure** tab. The time now uses factor 2.50 instead of 2.08.
> 5. The override is written to flash ~1.5 s after your last edit. Power-cycle the device — the 2.50 factor survives.

---

## 10. Built-in paper & filter database

### 10.1 Papers (22 built-in)

| Manufacturer | Paper | Type | Notes |
|---|---|---|---|
| Ilford | Multigrade RC Deluxe (New) | RC | |
| Ilford | Multigrade RC Portfolio (New) | RC | |
| Ilford | Multigrade IV RC Deluxe (Discontinued) | RC | legacy emulsion |
| Ilford | Multigrade IV RC Portfolio (Discontinued) | RC | legacy emulsion |
| Ilford | Multigrade Warmtone RC | RC | |
| Ilford | Multigrade Cooltone RC | RC | |
| Ilford | Multigrade FB Classic | FB | |
| Ilford | Multigrade FB Warmtone | FB | |
| Ilford | Multigrade FB Cooltone | FB | |
| Ilford | Multigrade ART 300 | FB | art matte surface, textured base |
| FOMA | FOMASPEED VARIANT | RC | |
| FOMA | FOMABROM VARIANT | FB | |
| FOMA | FOMAPASTEL MG | FB | |
| FOMA | FOMATONE MG Classic | FB | |
| FOMA | FOMASPEED Normal | RC | **[FG]** fixed-grade |
| FOMA | FOMASPEED Hard | RC | **[FG]** fixed-grade |
| FOMA | FOMABROM Normal | FB | **[FG]** fixed-grade |
| FOMA | FOMABROM Hard | FB | **[FG]** fixed-grade |
| FOMA | FOMABROM N chamois glossy | FB | **[FG]** fixed-grade, warm-tone |
| FOMA | FOMABROM N chamois matt | FB | **[FG]** fixed-grade, warm-tone |
| FOMA | RETROBROM Sp glossy | FB | **[FG]** fixed-grade, special-grade |
| FOMA | RETROBROM Sp semi-matt | FB | **[FG]** fixed-grade, special-grade |

**[FG]** = Fixed-grade paper — contrast is fixed at manufacture. Filter grade selection is disabled; Contrast tab shows "Fixed grade"; Split Grade tab is not applicable.

FB = fibre-base (stronger reciprocity correction, exponent ~0.10). RC = resin-coated (milder reciprocity correction, exponent ~0.07).

### 10.2 Filter brands (6 built-in)

| Brand | Type | Notation |
|---|---|---|
| Ilford Multigrade | Under-lens / head | 00, 0, 1, 2, 3, 4, 5 |
| FOMA Variant | Under-lens | 2× Y, Y, M1, M2, M3 |
| AGFA | Colour printing | Yellow / Magenta cc values |
| KODAK | Colour printing | Yellow / Magenta cc values |
| DURST | Colour mixing head | Yellow / Magenta density |
| MEOPTA | Colour mixing head | Yellow / Magenta density |

All papers work with all filter brands. Data sources: manufacturer datasheets and published technical specifications.

### 10.3 User paper extensions

The firmware has a hook (`user_papers.c`) for adding custom paper definitions. If you have a paper not in the built-in database, you can define its characteristic curve, filter table, and reciprocity parameters in C and rebuild the firmware. See the `user_papers.c` source file for the registration API.

---

## 11. Splash screen & tips

At power-on, the device displays a splash screen with:
- A randomly selected **inspirational photography quote** (from Ansel Adams, Dorothea Lange, Irving Penn, and others).
- A randomly selected **practical darkroom tip** (test strips, pre-flashing, developer temperature, dry-down compensation, fixing times, and more).

The splash screen is brief — after a moment the Main Screen appears and the device is ready to use. The tips cover real darkroom practice and are worth reading as they cycle.

---

## 12. Filter extension factor — how to measure your own

Every darkroom is unique. Your enlarger lamp (tungsten, halogen, LED), its age, the reflector condition, the power supply stability, and even the lens coatings all affect how much light actually reaches the paper through a given contrast filter. The built-in filter factors come from manufacturer datasheets and represent an *average* enlarger — your real factors may differ by 10–30%.

This section explains how to empirically determine the **real** filter extension factors for your specific setup and enter them into the Filter Editor so every tab uses your actual numbers.

### 12.1 What is a filter extension factor?

When you insert a contrast filter into the light path, it absorbs some of the light. The **extension factor** (or filter factor) is the number you multiply the unfiltered exposure time by to get the same print density with the filter in place.

For example, if a print needs 10.0 s without any filter and 20.8 s with a grade 2 filter to produce the same midtone density, the factor is 2.08. Manufacturer datasheets publish these numbers, but your real-world factor may be different.

### 12.2 Method A — Step-wedge / test-strip method (most accurate)

This is the gold standard. You need a step wedge (Stouffer T2115 or similar), or you can use a carefully made test strip.

**Procedure:**

1. **Calibrate without a filter first.** Do a normal paper calibration (§7) with **no filter** in the light path. Record the lux and the correct exposure time. This gives you your baseline calibration constant.

2. **Print a step wedge with no filter.** Place a step wedge (or a negative with a smooth gradient) in the carrier. Expose at the time calculated from step 1. Develop fully. This is your **reference strip**.

3. **Print the same step wedge with the filter you want to measure.** Insert the contrast filter (e.g. grade 2). Keep the lens aperture and head height identical to step 2. Make a test strip, develop identically.

4. **Find the matching density.** On the unfiltered reference strip, pick a step that has a clear, easy-to-judge midtone. On the filtered test strip, find the step that has the **same visual density**. Note the exposure time that produced that matching step.

5. **Calculate the factor.**

   $$\text{Factor} = \frac{\text{filtered exposure time that matches}}{\text{unfiltered exposure time of reference step}}$$

   For example: reference step was at 12.0 s, matching filtered step was at 26.4 s → factor = 26.4 / 12.0 = **2.20**.

6. **Enter it.** Go to Filter Editor → select the grade → type your measured factor into the Factor spinbox. The new factor is written to flash and used by every tab.

7. **Repeat for each grade** (grades 00, 0, 1, 2, 3, 4, 5).

### 12.3 Method B — Grey card visual match (no special equipment)

The most accessible method — you only need a grey card (18% reflectance) and patience.

**Procedure:**

1. Calibrate without a filter as normal (§7), using a grey card as your "negative" if you don't have a suitable midtone negative.
2. Make a test strip **without a filter** at your calibrated time. Pick the strip that matches the grey card's tone when dry. Note the time: **t_no_filter**.
3. Insert the filter you want to measure. Make a second test strip, varying the time around t_no_filter × the manufacturer's stated factor (e.g. if the datasheet says 2.08× for grade 2, centre your strip around 2.08 × t_no_filter).
4. Pick the strip that best matches the grey card from step 2 under identical lighting. Note its time: **t_filtered**.
5. Factor = t_filtered / t_no_filter.
6. Enter the Lengthening Factor in the Filter Editor tab.
7. Repeat for grades 00, 0, 1, 2, 3, 4, 5.

### 12.4 Method C — Densitometer method (if you have access to one)

If you have access to a reflection densitometer:

1. Make two identical prints of a smooth midtone negative — one with no filter, one with the filter under test. Develop identically.
2. Measure the reflection density of the same area on both prints.
3. The difference in density ($\Delta D$) tells you the exposure ratio needed:

   $$\text{Factor} = 10^{\Delta D}$$

   For example: unfiltered print reads D=0.72, filtered print reads D=0.45 → $\Delta D = 0.27$ → factor = $10^{0.27}$ = **1.86**.

4. Enter the Lengthening Factor in the Filter Editor tab.
5. Repeat for grades 00, 0, 1, 2, 3, 4, 5.

### 12.5 When to re-measure

- When you change the enlarger lamp (new bulb, different type).
- When you replace or clean the reflector.
- When you switch to a different lens.
- When you notice consistent exposure errors in one direction after filter changes.
- Annually — lamp output drifts with age.

### 12.6 Reciprocity and filter factors

Filter extension factors multiply the *base* exposure time. The meter then applies the Schwarzschild reciprocity correction to the result if the total time exceeds 10 seconds. This means:

$$t_{\text{final}} = t_{\text{base}} \times \text{factor} \times \left(\frac{t_{\text{base}} \times \text{factor}}{t_{\text{ref}}}\right)^p$$

Where $p$ ≈ 0.07 for RC papers and ≈ 0.10 for FB papers, and $t_{\text{ref}}$ = 10 s. The reciprocity correction is applied *after* the filter factor — so an incorrect factor compounds the reciprocity error for long exposures. This is another reason to measure your real factors carefully.

---

## 13. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| **Exposure Time** shows `calibrate` | This paper has no stored calibration yet. | §7. |
| **Exposure Time** shows `measure lux` | Calibrated, but no live reading. | Press **Measure** on the Exposure tab. |
| Lux label shows `no sensor` | Light sensor not responding. | Check the sensor cable; reboot. |
| Lux label shows `error` | The sensor read failed (typically saturation). | Drop the gain one step (HIGH → MED, MAX → HIGH). |
| Suggested time consistently off by 2× or ½× | Gain-stage factors uncalibrated for this device, or a different aperture / head height than when you calibrated. | Run **Sensor Light Calibration**, or recalibrate the paper. |
| Readings disagree when you switch gain | Gain-stage factors need trimming for your specific sensor. | Run **Sensor Light Calibration** (§2.2). |
| Contrast / Split tab shows `--` everywhere | One of the two readings is missing, or the paper isn't calibrated. The suggested-time label tells you which. | Measure that zone, or calibrate the paper. |
| Virtual Proof has clipping frames on every highlight cell | Negative range exceeds what the paper + filter can hold. | Pick a softer grade and press **Recompute Preview**, or switch to Split Grade. |
| Backlight looks dead | Brightness slider at 1 is intentionally very dim. | Drag right; the screen will reappear within the first few steps. |
| Calibration edits didn't stick after power cycle | They're flushed 1.5 s after the last tap. If you cut power inside that window they're lost. | Edit, pause one second, then power down. |
| Filter Editor spinboxes show stale values | Spinbox display is synchronised to the grade dropdown. | Re-select the grade from the dropdown to refresh. |
| Filter Editor "Reset to defaults" had no effect | The reset only affects the current paper. Other papers keep their overrides. | Switch to the paper you want to reset, then press the button. |
| Device won't wake from sleep | Button not held long enough, or battery is completely flat. | Hold the button for ≥1 second. If unresponsive, plug in USB to charge, then try again. |
| Battery bar shows empty but device still runs | The bar reads voltage under load; a sagging battery may show 0% while still having enough capacity to keep the MCU alive briefly. | Charge the battery. Auto-dormant triggers at 10% to prevent over-discharge damage. |
| "Charging…" never goes away | The charge-detection algorithm waits for a voltage plateau that signals a full cell. Some chargers never reach it. | Normal for some chargers. The battery is protected; unplug when done printing. |
| Screen flickers briefly during Measure | Normal — the backlight dims to 10% during sensor reads to prevent LCD light from contaminating lux readings (§2.1). | No action needed. |
| Filter Editor Factor / ISO R spinboxes greyed out | You have a fixed-grade paper selected (e.g. FOMA FOMASPEED Normal). These papers have a single built-in contrast — ISO R and factor cannot be changed. | Switch to a variable-contrast paper, or adjust only ISO P. |
| "No reference" when pressing Est. Cal from ISO P | You haven't set a reference paper yet. | Calibrate one paper, then press **Set as Ref** on the Filter Editor tab first. |
| "Clear All Calibrations" wiped everything | There is no confirmation dialog for this button. All calibrations are gone permanently. | Re-calibrate your most-used paper (§7), set it as reference, then use **Auto Estimate All** to restore approximate calibrations for the others. |
| Screen briefly goes dark then recovers during sensor read | The backlight dimming feature (§2.1) is active. On very long sample counts (16 reads × 600 ms integration) this can last ~10 seconds. | Reduce sample count or integration time in Settings if the flicker is distracting. |

</small>
