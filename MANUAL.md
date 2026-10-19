<small>

<p align="center">
  <img src="ManualImage.png" alt="SafelightIO Digital Darkroom Exposure Meter" width="420"/>
</p>

<p align="center">
  <img src="HeaderLogoBlack.png" alt="SafelightIO" width="320"/>
</p>

<p align="center">
  <em style="font-size: 1.1em; color: #888;">Digital Darkroom Exposure Meter</em>
</p>

---

<p align="center"><strong>One reading at the easel. Perfect prints, every time.</strong></p>

| | |
|---|---|
| **Measure** — point the sensor, press Measure, get the time | **Analyze** — contrast grade recommendation in seconds |
| **Split** — automatic soft/hard grade timing for tricky negatives | **Preview** — virtual proof grid before you commit paper |

---

## User Manual

# SafelightIO — User Manual

A tablet-sized companion for black-and-white enlarger printing. Point the sensor at the easel, choose the paper you're about to print on, and SafelightIO tells you how long to expose, which contrast grade to use, and how a tricky negative will distribute across the paper before you commit to it.

---

## 1. Quick start

1. Power the device on. The backlight comes up at its lowest level (7% PWM) while the firmware boots, then switches to your saved brightness as soon as the UI is ready; a splash screen appears with an inspirational photography quote and a practical darkroom tip, then the Main Screen opens with five tabs: Exposure, Contrast, Split Grade, Virtual Proof, Filter Editor, plus a Settings panel (paper, sensor, calibration, brightness).
2. In Settings, choose **Paper Brand**, **Paper Type**, and **Filter Brand** (the filter system you use in your enlarger head).
3. The first time you use a paper, do §7 Calibrating a new paper.
4. On the Exposure tab, place the sensor where you want the midtone on the easel, press Measure, read the suggested time.

### Where your settings are stored

All of your settings — brightness, sensor setup, per-paper calibrations, Contrast/Split trims, filter overrides, the paper and filter selections, and the sensor calibrations — are saved automatically, about 1.5 s after your last edit.

- **With a microSD card inserted** (FAT32), everything is stored on the card in a file called `SETTINGS.TXT`. You can back the file up, copy it to another device, or edit it by hand. The sidebar shows `SD: settings.txt` and saves happen invisibly.
- **Without a card**, everything is stored in the device's internal flash memory and the sidebar shows `SD: none (flash)`. Saves then cause a brief freeze of the screen — this is normal. Note: the internal flash record is a single copy, so removing power in the instant a save is being written can lose the stored settings; with a card inserted the card copy covers this.
- The first time you boot with a new card, the device automatically copies its current settings onto it; afterwards the card is the master copy. Removing the card mid-session falls back to internal flash. A backup copy of the file is kept as `SETTINGS.BAK` after every save.

### Adding your own papers (PAPERS.CSV)

With the SD card inserted, you can add papers or correct built-in paper data without a firmware update. On first boot with a card the device writes a commented template file called `PAPERS.CSV` to the card; edit it on a computer and reboot.

- One `P` row defines a paper (id, manufacturer, paper type, VC/FG, ILFORD/FOMA, Dmin, Dmax, fibre-base 0/1, ISO P) and the `F` rows that follow it define its filter grades.
- An id matching a built-in paper (e.g. `ilford_cooltone`) **replaces** that paper's data; any other id adds a new paper at the end of the list.
- Comma or semicolon separators are both accepted (spreadsheet locale differences).
- Custom papers appear in the dropdowns like built-ins. Their calibrations and trims are stored in `SETTINGS.TXT` on the card — with the card removed, custom papers cannot be calibrated (built-in papers still use internal flash).

The sidebar also has an **Export** button: it writes the current session to `SESSION.CSV` on the card — the selected paper/filter/calibration, the last Contrast and Split-Grade readings with their on-screen results, and every measured Virtual Proof cell (column, row, lux, grayscale, clipping flags). Open it in a spreadsheet to review or re-print a session. Pressing it with no measurements shows "Nothing to export".

A **Load** button restores the latest exported session: the paper selection, the Contrast and Split-Grade readings (re-analyzed on load), and every measured Virtual Proof cell. Derived results are recomputed from the loaded lux, so re-grading under a different paper or filter works. When there are current measurements, Load asks for confirmation first. A toggle next to the button chooses whether the session's calibration (lux and time) is restored too; a session exported without a calibration never clears the current one. With no `SESSION.CSV` on the card, Load reports "No session file".

The sidebar also has **Backup** and **Restore** buttons. Backup writes a manual snapshot to `BACKUP.TXT` **and stores the same state in the device's internal flash** (except calibrations and trims of papers *added* via PAPERS.CSV, which exist only on the card) — use it before experimenting (the snapshot survives any number of later auto-saves), or copy that file to another device and Restore it there; if the card is ever lost, the device still holds the last backup. Restore asks for confirmation, stores the restored state in both the card and the device flash, and then reboots with the snapshot's settings.

---

## 2. The light sensor

A light sensor reads the light at the easel and reports it in lux (the SI unit of illuminance — how bright a surface is). Three controls govern how each reading is taken.

| Control | What it does | When to change it |
|---|---|---|
| **Gain** (Auto / LOW 1× / MED 25× / HIGH 428× / MAX 9876×) | Amplifies the sensor signal; **Auto** lets the meter pick. | **Auto** (default): every measurement starts at **MAX** and steps down one stage at a time only when the reading would saturate — dim scenes get the finest resolution, bright scenes step down until they fit. Pick a specific gain to pin the meter to it: the reading is then taken at that gain only, and if the scene is too bright for it the meter reports an error (`error` / `read error`) instead of stepping down. At 100 ms integration the meter steps down early (75 % of full scale) to avoid clipping from lamp flicker. |
| **Integration Time** (100–600 ms) | How long each individual reading lasts. Longer is quieter but slower. | Default **200 ms**. Raise for noisy low-light scenes; lower (100 ms) when you want a Virtual-Proof auto-scan to fly through cells. |
| **Sample count** (1–16) | How many readings to average each time you press *Measure*. | Default **5**. Increase for very low light or to even out lamp flicker. |

> **After updating from a firmware without Auto:** the Sensor Gain setting comes up as **Auto** — the meter cycles gains exactly as it did before the update. Pick a fixed gain only when you want to lock one in (e.g. to force a specific stage during a comparison test).

> Treat the sensor like a real spotmeter — shield it from stray room light (even red safelight) and only press Measure with the enlarger lamp on.

### 2.1 Backlight dimming during readings

The LCD backlight can contaminate light-sensor readings in a darkroom. Every time you press **Measure** (on any tab), the screen automatically dims to 6% brightness before the sensor is read, then restores to your chosen brightness afterward. This happens transparently — you may notice the screen flicker briefly, especially during long sample sequences. There is no setting to disable this; it is always active to ensure accurate lux readings.

### 2.2 Sensor calibration (one-time per device)

Two pairs of buttons in the Sensor panel:

- **Sensor Offset Calibration** / **Clear Offset** — the dark-current baseline. The sensor sweeps **all four gains at all six integration times** (24 slots, one stored per combination) in one press, so every gain/integration setting gets its own measured dark baseline. Sensor must be in **real darkroom printing conditions, total darkness** when you press it (sensor open on easel, head off, lights and safelight off). Takes ≈30 s at 100 ms integration up to ~3 min at 600 ms; the status line counts up (`dark calib… 12/24`). Persisted automatically. Do once, redo only if drift suspected (dark roughly doubles every 8–10 °C, so re-run if the darkroom temperature changed a lot).
- **Sensor Light Calibration** / **Clear Light Cal** — per-device gain-stage trimming in **two phases**. Phase 1 measures under your current **steady light**; the meter then asks you to **dim the light ~4 stops** (stop down or move the sensor back) and tap Yes to measure phase 2, or No to finish with phase 1 only. Each phase measures the real gain ratios of **both sensor channels** (visible CH0 and infrared CH1), and the phases are chained across adjacent gain stages so that **MAX and HIGH — the gains your dim readings use — get real measured factors** (a single light level can never measure the full ~10,000× gain span; LOW is pinned at 1×, the datasheet's definitional reference). Use the **enlarger's own light** when possible: its IR content is what makes the CH1 factor measurable and meaningful. Takes a few seconds per phase. Run once per device; re-run if readings disagree when you switch gain.

The **Calibrate** and **Clear** buttons all ask for confirmation on a confirmation screen before they run.

Status messages appear on every tab's lux label simultaneously, so you don't have to be on a particular tab to see the result. For the light calibration there are three outcomes:

| Status | Meaning |
|---|---|
| `gain calib… phase 1/2` / `phase 2/2` | Calibration running (blocks for a few seconds per phase). |
| `gain cal set` | Every stage got a real measured factor (LOW is always set — pinned at 1×). |
| `gain set - MAX sat` (or `HIGH zero`, etc.) | That stage fell back to its datasheet value: `sat` = saturated, `zero` = read too few counts (~<50) to trust. The other stages are calibrated. |
| `gain cal failed - adjust light` | No adjacent gain pair was measurable at either light level — **nothing** was saved. Change the light level and re-run. |
| …`- moved` | The light drifted >3% during the sweep. Announced only — the factors are still applied; re-run for cleaner data if you want. |
| …`- no IR` | The light had too little infrared for a meaningful CH1 factor (announced only). Fine under LED light; use the enlarger lamp for best accuracy under incandescent. |

(Dark-offset statuses: `dark calib… N/24` while the sweep runs, then `dark offsets set (24)` on success or `dark calib failed` on error.)

> **Lux scale:** lux readings use the correct device factor for the TSL25911FN glass package (408; the chipscale CS value would be 53), so displayed lux now matches a real lux meter. This firmware update discards settings stored by earlier firmware (the settings formats changed): re-run Sensor Offset / Sensor Light Calibration and re-calibrate your papers once. A completely clear glass window in the sensor housing attenuates a few percent — that is absorbed by the per-paper calibration, so no extra setting is needed.

> **Tip:** If you ever see readings that don't agree when you switch gain (e.g. MED says 2.00 lux but HIGH says 1.50 lux on the same scene), run Sensor Light Calibration. If readings drift upward in very low light, re-run Sensor Offset Calibration in complete darkness.

---

## 3. Exposure tab — printing-time suggester

The everyday tool. Once a paper is calibrated, point the sensor at the easel and the device gives you the time. You can use this tool with fixed and variant grade papers. Always take readings without contrast filter.

### 3.1 What every element does

| Element | Purpose |
|---|---|
| **Paper Brand / Paper Type** dropdowns | Pick the emulsion you're about to print on. The two are dependent: choosing a brand repopulates the type list. |
| **Filter Brand** dropdown | Choose which contrast-filter system is in your enlarger head. **Ilford Multigrade** (grades 00–5), **FOMA Variant** (Y/M notation), or colour-head filters (**AGFA**, **KODAK**, **DURST**, **MEOPTA**). The meter works cross-brand — you can use Ilford filters with FOMA paper, and vice versa. The filter tables come from manufacturer datasheets where published; combinations without a published table (FOMA filters on Ilford papers, some colour-head brands) are derived estimates computed from the closest published data (see §10.2 and DATABASE_VERIFICATION.md). Exception: for **FOMATONE MG Classic**, only the DURST/MEOPTA dials (grades 0–4) are datasheet values; its AGFA/KODAK and grade-5 colour-head entries are derived estimates, marked with **~** in the filter lists (see §10.2). |
| **Calibration Lux** spinbox | Lux you measured during your reference test print. Two decimal places, range **0.00 – 99.99**. |
| **Calibration Time** spinbox | Seconds that produced the “correct” test print at that lux. Two decimal places, range **0.00 – 99.99**. |
| **Calibration Constant** | Derived from the two boxes above. This is the per-paper number the device actually stores and uses. Larger = darker paper. |
| **Measure** button | Take an averaged lux reading right now. |
| **Lux Number** | The most recent live reading. |
| **Zone dropdown** (0–X) | Which Zone System zone you are measuring. Default is **Zone V** (middle gray); the last selection is remembered across power cycles. Change this when you meter a shadow (Zone III) or highlight (Zone VII) instead of a midtone — the meter scales the reading to its Zone V equivalent automatically (§3.2). With this feature you can measure a cloud, select Zone VII and you will get the exposure time to achieve Zone VII at the cloud. |
| **Filter Grade Transform** dropdown |  Transform the exposure time with the lengthening factor of the selected contrast filter. |
| **Dodge & Burn slider** (−9 … +9) | Push or pull the time in ¼-stop increments. Right = burn (more exposure, darker print), left = dodge. ±9 covers ±2.25 stops. See §3.1b below. |
| **Exposure Time** | The final number, in seconds. While anything is missing, this label tells you what to do (`calibrate` → no calibration yet; `measure lux` → press Measure). Times below 1 s or above 300 s get a sanity hint appended. |

### 3.1b Dodge & Burn panel

Each tab has a **DODGE & BURN** panel below the main results that lets you fine-tune the exposure after the first working print. On the Exposure tab:

| Element | Purpose |
|---|---|
| **Dodge & Burn slider** (±2.25 stops, ¼-stop steps) | Multiply the calculated exposure time by a factor to dodge (less time) or burn (more time). Set to 0 for no adjustment. |
| **ADDITIONAL TIME** | How many seconds the dodge/burn adds or subtracts from the base exposure. |
| **TOTAL TIME** | The final exposure time with dodge/burn applied. This is the number you set on your enlarger timer. |

The slider works independently from the Filter Grade Transform and Zone settings — all three stack together. The base time (before dodge/burn) includes the filter factor, zone correction, and reciprocity if applicable; the dodge/burn factor is applied last.

The slider resets to 0 whenever you switch paper, so a previous print's adjustment can't sneak into the next one.

### 3.2 Overall logic

The calibration spinboxes describe one print you already know works. Internally the device boils them down to a single per-paper constant. Once that constant exists, any new lux reading from the easel translates directly into a print time. Changing the filter dropdown multiplies the time by that filter's exposure factor.
Calibration is stored per paper — switch paper and the meter instantly reloads the calibration for that emulsion. Edits to the spinboxes are written to flash about 1.5 s after you stop tapping, so rapid +/- presses coalesce into one save.
The Dodge & Burn slider (§3.1b) applies an additional ¼-stop push/pull on top of the calculated time — use it after the first working print to fine-tune density.
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

The meter ships with six filter brands: **Ilford Multigrade** (0–5), **FOMA Variant** (Y/M notation), plus four colour-head systems (**AGFA**, **KODAK**, **DURST**, **MEOPTA**). Choose your filter brand in the Settings panel. The meter automatically loads the correct filter factors, ISO R values, and gamma data for whichever paper + filter-brand combination you're using. You can use Ilford under-the-lens filters with FOMA paper, FOMA filters with Ilford paper, or dial in a colour head with any paper — the database has cross-compatibility data for all papers. One exception: **FOMATONE MG Classic** — its datasheet publishes colour-head tables for **DURST and MEOPTA, grades 0–4**. Those dials are stored exactly as printed; its AGFA/KODAK and grade-5 colour-head entries are derived estimates (marked **~** in the filter lists), because the datasheet publishes no such rows.
### 3.3 Workflow example

> *Portrait shot on FP4, printing on Ilford MG Classic Cooltone.*
>
> 1. In Settings, choose **Ilford / MG Classic Cooltone**.
> 2. If this paper has never been calibrated, do §7 Calibrating a new paper first.
> 3. Tab to **Exposure**. Stop the lens to f/11. Place the sensor on the easel where the model's cheek will fall (Zone VI — caucasian skin). Set **Zone dropdown** to **VI**.
> 4. Press **Measure**. Lux Number reads 2.84 lux. The meter scales to its Zone V equivalent (2.84 ÷ 2 = 1.42 lux) internally. Exposure Time label updates to 8.80 s.
> 5. Grade **3** looks right from the contact sheet — pick **3** in the filter dropdown. Time updates to **~23.3 s** (22.0 s × the grade-3 factor of 2.5, plus a small reciprocity correction).
> 6. Print. It's ½ stop too light. Pull the **Dodge & Burn** slider to +2 (½ stop more); Exposure Time becomes ~32.9 s. Print again.

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
| **Suggested Exposure Time** | Single midpoint exposure time, in seconds. Includes the chosen filter’s factor. Times below 1 s or above 300 s get a sanity hint in the Exposure Note. |
| **Midpoint Lux** | The geometric mean of your two readings after the Overall-Offset slider — the brightness the time calculation uses. |
| **Meter Calibration Value** | The paper’s raw calibration constant. The Overall-Offset slider does NOT change it — the slider’s effect is folded into the Midpoint Lux value instead. |
| **Exposure Note** | Tells you whether long-exposure reciprocity-failure correction was applied and how much it added. |
| **Overall Offset** slider (±1.5 stops) | Push or pull the whole suggested time without changing the grade. |
| **Contrast Bias** slider (±1.5 stops) | Bias the grade selection. Positive → recommends a harder grade; negative → softer. Use it when you consistently disagree with the recommendation in one direction or you want different aesthetics. |
| **Highlight Trim** slider (±1.5 stops) | Treat the highlight as if it had received more (+) or less (−) exposure on the negative. Affects both contrast grade and time in order to have the perfect exposure on shadows and highlights. |
| **Shadow Trim** slider (±1.5 stops) | Same for the shadow. |
| **Reset** button | Zero all four sliders for the current paper. |

The four sliders persist **per paper**, alongside calibration. Dial in your preferences for FOMA Variant III, then switch to Ilford MG and dial in different ones — they’ll each come back when you reselect that paper. Each slider step is 1/6 of a stop, so the labels read in increments like +0.17 / +0.33 / +0.50 stops.

#### Dodge & Burn panel

The Contrast tab also has a **DODGE & BURN** panel below the analysis results:

| Element | Purpose |
|---|---|
| **Dodge & Burn slider** (±2.25 stops, ¼-stop steps) | Applies a global dodge/burn to the suggested midpoint exposure time without changing the grade recommendation. |
| **ADDITIONAL TIME** | How many seconds the dodge/burn adds or subtracts from the suggested midpoint time. |
| **TOTAL TIME** | The final midpoint exposure time with dodge/burn applied. |

This is useful when the contrast recommendation is correct but the overall print density needs a nudge — e.g. the first print is slightly too dark at the recommended grade; pull the slider negative a few steps instead of recalculating everything.

### 4.2 Overall logic

The Contrast Analyzer asks two questions:

1. **Which grade?** The contrast range between highlight and shadow, after any Contrast Bias, is matched against the paper’s filter table — the grade whose contrast (ISO R) is closest to the negative’s range wins.
2. **For how long?** The meter takes two readings (the "true" midpoint), feeds it into the paper's calibration constant, and multiplies by that filter's exposure factor. Long exposures get an automatic reciprocity-failure correction — papers under-respond when exposed for a long time at low intensity, so the meter lengthens those exposures using a Schwarzschild model. Resin-coated (RC) papers use an exponent of ~0.07; fibre-base (FB) papers use ~0.10 which produces a stronger correction. The reference time is 30 seconds — the correction starts only for exposures longer than 30 s. When reciprocity correction is applied, the Exposure Note field tells you how much time was added.

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
| **Equivalent Grade** | The single VC grade whose ISO(R) paper range matches the negative's contrast range — the grade a single-filter print of this negative would use. Reference only. |
| **Analysis Reasoning** | The split, expressed as a percentage of each filter's **unfiltered-equivalent light** (time ÷ lengthening factor), the soft:hard light ratio, and the split's effective ISO R (e.g. “65% 00 / 35% 5 (light soft:hard 1.9:1, ISO R 84)”), plus any trim, reciprocity (with the seconds it added), or out-of-range note. |
| **Soft Filter Name / Soft Time** | Which soft filter to use (e.g. 00 or 2× Y) and how many seconds to expose with it. |
| **Hard Filter Name / Hard Time** | Same for the hard filter (e.g. 5 or 2× M2). |
| **Split filter pair** slider | One slider picks the split pair. Centre = the paper's extremes (00/5, 2xY/2xM2). Slide **left** to step the HARD filter softer (00+5 → 00+4 → 00+3 …); slide **right** to step the SOFT filter harder (00+5 → 0+5 → 1+5 …). On FOMA Variant the no-filter **Special** grade is included as a selectable leg. Times are recomputed with the correct per-grade speed compensation, and a pair too narrow for the negative's range gets a warning. |
| **Total Time** | Soft + Hard, the total bulb-on time the print sees. Times below 1 s or above 300 s get a sanity hint in the Analysis Reasoning. |
| **Meter Calibration Value 2** | The paper’s raw calibration constant. The Overall-Offset slider does NOT change it — the slider’s effect is applied in the time calculation instead. |
| **Overall Offset** slider (±1.5 stops) | Push/pull the total time without changing the soft/hard ratio. |
| **Contrast Bias** slider (±1.5 stops) | Bias the equivalent-grade calculation, which in turn shifts the soft/hard ratio. Positive → more hard filter. |
| **Highlights** slider (±1.5 stops) | Reinterprets the **highlight reading**, same semantics as the Contrast tab: + = treat the highlight as if the negative received **more** exposure there (prints darker); − = treat it as **less** exposed (prints lighter, whiter highlights). Changes the split ratio AND the total exposure coherently. |
| **Shadows** slider (±1.5 stops) | Reinterprets the **shadow reading**, same semantics as the Contrast tab: + = treat the shadow as if the negative received **more** exposure there (prints darker); − = treat it as **less** exposed (prints lighter). Changes the split ratio AND the total exposure coherently. |
| **Reset** button | Zero all four split trims and reset the filter pair to the extremes for the current paper. |

Like the Contrast trims, these four sliders persist **per paper**. They are a separate set from the Contrast-tab trims — you can have different bias and trims for the two analyzers on the same emulsion.

#### Dodge & Burn panel

The Split Grade tab has a **DODGE & BURN** panel below the split results:

| Element | Purpose |
|---|---|
| **Dodge & Burn slider** (±2.25 stops, ¼-stop steps) | Applies the same dodge/burn factor to BOTH the soft and hard filter times. The soft/hard ratio is preserved; both legs scale together. |
| **ADDITIONAL TIME** | How many seconds the dodge/burn adds or subtracts from each leg (soft and hard shown separately). |
| **TOTAL TIME** | The final time for each leg with dodge/burn applied (soft and hard shown separately). |

This is useful when the split ratio is correct but the overall density needs adjustment — apply a small burn to darken the print without changing the soft/hard balance.

### 5.2 Overall logic

Each paper publishes a soft filter and a hard filter. The meter computes how much of the total exposure should happen under each, given the negative’s brightness range and the paper’s contrast endpoints. The split is derived from the soft:hard **light ratio in stops** — the ratio of the two legs' unfiltered-equivalent light (time ÷ lengthening factor), so the filter factors compensate the blocked light *after* the ratio is decided: measured split-grade data (Woodhouse’s *Way Beyond Monochrome* fig. 5 and Lindan’s measured app note) shows ISO(R) tracks this ratio roughly linearly, with an 8:1 split already delivering the softest published grade — so the ratio is clamped to the 8:1 … 1:8 band rather than ever running to a pure single-filter exposure. At the extremes of that band the dominant leg also gets a small +0.1-stop boost (Lindan’s recommendation).
The midtone exposure is anchored at the geometric mean of the two readings — so the print midtones land where you’d expect from the calibration — and that light is then split into the two legs in the proportion the math demands: each leg's bulb time = its light share × its own lengthening factor. The Highlights/Shadows trims reinterpret the two readings — exactly like the Contrast tab — so they move the anchor and the split ratio coherently (see §5.1).
Long total times are corrected for reciprocity failure automatically (see §4.2 for details on the Schwarzschild model), and the two legs scale together so the soft/hard ratio stays the same.
When the negative is so contrasty that the equivalent grade exceeds the paper’s softest filter, the Reasoning warns “highlights may burn” and the split pins at the softest ratio (8:1). When it’s too flat, you’ll see “limited contrast” and the split pins at the hardest ratio (1:8).

### 5.3 Workflow example

> *High-contrast portrait — bright window backlight, dark hair against shadow. Paper: Ilford MULTIGRADE RC COOLTONE, calibration constant 12.0 lux·s.*
>
> 1. Tab to **Split Grade**. Measure Highlight on the window glare:
>    `8.00 lux`.
> 2. Measure Shadow on the hair detail: `0.12 lux`.
> 3. ΔEV = `6.06 stops`. Equivalent Grade *00* (Exact), Reasoning warns
>    *“highlights may burn”* (the negative sits just past the softest grade).
> 4. Split times: Soft **00** → `29.5 s`, Hard **5** → `6.9 s`,
>    Total `36.4 s` (includes reciprocity; 89% / 11% light, light ratio 8.0:1).
> 5. Print: drop in the 00 filter, expose 29.5 s; swap to the 5 filter,
>    expose 6.9 s. Develop, fix, evaluate.
> 6. Highlights print too light. Pull the **Highlights** slider to +0.5 stops (treats the highlight as 0.5 stop more exposed on the negative): ΔEV becomes 5.56, the equivalent grade drops to 0 and the split shifts harder — Soft **00** → 33.6 s, Hard **5** → 12.0 s, Total ~45.6 s. The highlights print darker. Reprint.

> **Tip.** If one leg is wildly bigger than the other, the negative is genuinely outside the paper’s contrast range. Consider pre-flashing, dodging the highlight, or picking a different paper.

---

## 6. Virtual Proof tab — print preview & enlarger uniformity test

Sweep the easel and the device paints a grayscale preview of the print — cell by cell, on the chosen paper, at the chosen grade — before you commit a sheet to it. With the **Enlarger Mode** switch ON, the same grid measures the bare enlarger light and paints a uniformity map instead (§6.5).

### 6.1 What every element does

| Element | Purpose |
|---|---|
| **Grid Width / Grid Height** spinboxes | Number of cells across × down (2..40 × 2..30). More cells = finer preview, longer to scan. Changing the size **wipes** the grid. |
| **Proof Grid (the canvas)** | One block per cell, painted with the predicted gray. Cells with a coloured frame are special: **amber** = next cell to read, **red** = your selection, **cyan** = Zone V reference, **light gray** = highlight clipping, **dark gray** = shadow clipping, no frame = ordinary measured (or empty) cell. |
| **Measure Next Cell** button | Read one cell at the cursor and advance. When **Stability Enabled** is ON, this button becomes **Start Scan / Stop Scan** and the device walks the grid for you. |
| **Set Zone V Reference** button | Use the currently selected cell as the “middle gray” anchor; every other measured cell is re-derived in relation to it. |
| *Auto re-render* | Switching paper, changing the preview filter grade, or recalibrating re-derives every measured cell automatically — no button needed. |
| **Clear Grid** button | Erase all samples, the selection, and the reference. |
| **Stability Enabled** switch | Turn on automatic settle detection so a scan records each cell only when its reading has stopped changing. |
| **Stability Tolerance** (%) | Two consecutive reads must agree within this percentage to count as “stable”. |
| **Stability Min Delta** (lux) | A floor on Tolerance. In very dim cells, a strict percentage gets unreasonably tight; this gives it some absolute breathing room. |
| **Stability Min Stable** | How many consecutive stable reads before the cell is recorded. |
| **Stability Max Wait** (ms) | After this long without settling, the cell is recorded anyway so the scan doesn’t stall. |
| **Filter Grade** dropdown | The grade the preview is rendered for. Changing it re-renders every cell. Hidden in Enlarger mode (paper/filter mean nothing to bare light). |
| **Histogram** (proofHistogram) | 10 Zone distribution of the predicted print tones — a fast read on "does the print sit mostly in shadows / midtones / highlights?". In Enlarger mode it becomes a **deviation histogram** (10 bins spanning ±1.25× the limit). |
| **Selected-sample readouts** (Lux / Zone / ISO R / EV Range / Density / Exposure / Clipping) | Detail on whichever cell is red-framed. With nothing selected, the *Clipping* slot turns into a global verdict: *"Negative too contrasty"* / *"too flat"* / *"-- "*. In Enlarger mode the same seven slots become Lux / Dev% / Dev EV / Range / Mean / Min-Max / uniformity verdict — see §6.5. |
| **Enlarger Mode** switch | Toggles the whole tab between the negative preview (OFF) and the enlarger light-uniformity map (ON). Measurements are shared — flipping the switch just re-derives the display. |
| **Uniformity Limit** (%) | In Enlarger mode: the deviation tolerance (5..50 %, default 15 %) that the verdict and the heat map are judged against. |

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
> 2. Choose **2xM1** (Normal) in the Filter Grade dropdown — your usual starting grade.
> 3. Turn **Stability Enabled** ON. Press **Start Scan**.
> 4. Sweep the sensor methodically across the easel, top-to-bottom. Pause
>    briefly at each cell — the meter records and advances on its own. The
>    button label updates to *“Stop scan (47/192)”*, *“(48/192)”*, ….
> 5. When the scan completes, Zone V is set automatically; the preview is
>    fully painted; the histogram fills in.
> 6. Tap a midtone cell on the canvas — last-sample readout shows
>    `Zone: 5.1`, `Density: 0.62`, `Exposure: 8.40 s`, `Clipping: none`.
> 7. Tap a highlight cell with the light-gray frame — readout says
>    `Clipping: highlight`. You pick **2xY** (Extra soft) in the Filter
>    Grade dropdown — the preview re-renders immediately: the highlight
>    un-clips, the shadows deepen slightly, the histogram shifts left.
> 8. Tap empty space to clear the selection — the Clipping slot now shows
>    *“Negative too contrasty”*. Time to consider Split Grade or
>    pre-flashing.

### 6.5 Enlarger mode — light-uniformity test

Flip the **Enlarger Mode** switch ON and the same grid becomes a uniformity map of the *bare enlarger light* — the classic corner-falloff / hot-spot test, but with numbers instead of squinting at the baseboard.

**Set up the enlarger as you would print, but with no negative in the carrier:**
the lens at your *working aperture*, the head at your *working height* (falloff changes with magnification — test at the size you actually print). Let the lamp warm up for a few minutes first; a cold lamp drifts while you measure. Place the sensor flat on the easel at each point, with an opal/diffusing disc over it and the device positioned so it doesn’t cast a shadow on the point being read.

**Procedure**

1. Set the grid to **3 × 3** (the classic nine-point test) or 5 × 5 for a finer map.
2. Turn **Stability Enabled** ON and press **Start Scan**; sweep the easel like a negative scan. When it finishes, the reference point is set automatically to the average-brightness cell.
3. The grid repaints as a heat map: **blue = dimmer than average, gray = on average, amber/red = brighter**, each cell framed **white when it exceeds the Uniformity Limit**. The histogram shows the spread of deviations.
4. Read the numbers in the detail panel:

| Slot | Meaning in Enlarger mode |
|---|---|
| `Lux:` | The selected point’s brightness |
| `Dev: +x.x %` / `Dev: +x.xx EV` | How far the selected point sits from the anchor (mean, or the reference point) |
| `Range: x.xx EV` | Brightest-to-dimmest spread across the grid |
| `Mean:` | Geometric-mean lux of all measured points |
| `Min/Max:` | Dim-/brightest point |
| `GOOD / MARGINAL / UNEVEN unif xx% ±x%` | Verdict against the **Uniformity Limit**: GOOD = every point within half the limit, MARGINAL = worst point between half and the full limit, UNEVEN = beyond. `unif` is the classic min/max figure; the signed figure is the worst point's deviation; `corn +x%` (3×3 only) is the four-corners average vs. the centre. |

5. Tap a point to inspect it; press **Set Reference** on the centre point to read every other point *relative to the centre* — the usual way enlarger specs are quoted.
6. Toggle the switch back to Negative mode any time — the same measurements re-render as the normal preview (nothing is lost; the two views share the cells).

**Interpreting results.** A healthy enlarger at working aperture typically keeps every point within ~±15 % (≈0.2 EV) of the centre. A dark corner suggests condenser/diffuser or lamp misalignment; a bright centre with strong corner falloff is normal for condenser heads (and gets worse at large magnifications — burn the edges, or stop down); a hot spot off-centre usually means the lamp needs centring. The verdicts are just a flag — trust the map.

**Session export/load** stores the mode (`proof_mode,negative|enlarger`) with the cells, so a saved uniformity run reloads as a uniformity run.

---

## 7. Calibrating a new paper

Do this **once per emulsion**. The whole device hinges on one stored
number per paper — without it, the Exposure tab shows `calibrate`, and the
Contrast and Split tabs report `--` everywhere, and the Virtual Proof preview still renders (only its per-cell Exposure readout shows `--`).

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
- **Battery Bar** — red bar in the corner, updates every 5 seconds. See §8.1 for charging behaviour.

### 8.1 Battery, charging & power

The device runs from a LiPo battery. The battery bar shows the discharge percentage (16-point curve, load-sag compensated). Because this board exposes no charger-status pin and its USB VBUS line is not readable by the MCU, charging is inferred from the battery voltage itself (plug/unplug load steps plus the charger's constant-voltage level), so plugging and unplugging is recognised within one poll (~5 s). Four states are shown:

| State | What you see |
|---|---|
| **Discharging** | Red percentage bar |
| **Charging** (USB plugged in) | Orange "Charging…" label — the bar is hidden because voltage readings are unreliable during charge |
| **Fully charged** | Green "Fully charged" label |
| **Battery absent** | Grey, empty bar |

#### Low-battery warning

When the battery falls to **10%**, the battery bar is replaced by a red **"Battery low — charge now"** warning. The device deliberately has **no auto-sleep / dormant mode**: it keeps running so the user sees the warning and plugs in USB. Don't leave a critically low battery connected — the cell's own protection circuit is the last line of defence against over-discharge.


#### Device power and charging

- Plug a USB-C cable at the left side of the device to power on with external power.
- Plug a USB-C cable at the left side of the device while it is powered on to charge the battery.
- On battery, the device runs until the battery is drained — the low-battery warning above is your cue to charge.

---

## 9. Filter Editor tab — customising filter data

The Filter Editor lets you override the built-in filter factors, ISO R values, and paper base speed (ISO P) for any paper + grade combination. All edits persist to flash and survive power cycles. Every other tab uses the effective (overridden) values in its calculations. You can use this tool with fixed and variant grade papers.

### 9.1 What every element does

| Element | Purpose |
|---|---|
| **Filter Grade** dropdown | Pick the grade you want to edit (e.g. "00", "2", "5", "2× Y"). The list is populated from the current paper + filter brand. |
| **Current factor / Current ISO R** labels | Show the **effective** values — your override if one exists, otherwise the built-in default. These are what every other tab uses in its calculations. |
| **Default Factor / Default ISO R** labels | Show the **built-in** factory values from the paper database. Use these as a reference to see how far you've deviated. |
| **Factor spinbox** | Edit the filter's exposure multiplier (e.g. 2.17 for a grade 2 filter on Ilford MG FB Classic). Two decimal places. Set to 1.00 to effectively remove the filter factor. |
| **ISO R spinbox** | Edit the contrast range this filter grade produces on this paper (e.g. 110 for grade 2). Higher ISO R = softer contrast. Changing ISO R directly affects grade matching in the Contrast and Split Grade tabs. |
| **ISO P spinbox** | The paper's base unfiltered speed. Default is 500 for Ilford MG papers. Raising ISO P makes the meter suggest shorter times; lowering it suggests longer times. This is a **per-paper** setting (not per-grade). |
| **Reset to defaults** button | Clear **all** overrides for the current paper (factors, ISO R values, and ISO P) and restore the built-in database values. |
| **Base ISO P** label | Shows the current effective ISO P for the paper. |

### 9.2 When to use the Filter Editor

- **Your filter set doesn't match the datasheet.** Old filters fade and shift — measure their actual factor with a step wedge and enter the real number here.
- **You want a different paper speed.** Maybe your developer runs warm, or you prefer slightly lighter prints — bump ISO P up or down.
- **You're dialling in a new paper** that isn't in the built-in database. Use a similar paper as a starting point and tweak the ISO R and factor values per grade.
- **Cross-brand filter fine-tuning.** Using Ilford filters on FOMA paper? The built-in cross-brand data is based on published tech specs, but your specific setup may benefit from small adjustments.

> **Note:** the device stores at most **64 filter overrides** (factor / ISO R edits, across all papers and grades) in flash. If you exceed that, edits beyond the limit are not persisted across power cycles — reset unneeded overrides with **Reset to defaults** to stay under it.
>
> Editing a spinbox commits only **that field** — the other two keep their previous values, so no unwanted "no-op" overrides are created. And if you change the grade right after typing, your pending edit is committed to the grade you were editing, not lost.

### 9.4 Advanced calibration tools — cross-paper estimation

The Filter Editor also contains four buttons that help you calibrate multiple papers quickly by leveraging the ISO P speed rating. These appear below the spinboxes.

| Button | Purpose |
|---|---|
| **Set as Ref** | Snapshot the currently selected paper's calibration (lux + time + ISO P) as a reference template. The reference label updates to show which paper is the source. |
| **Est. Cal from ISO P** | Estimate a calibration for the currently selected paper, using the stored reference, scaled by ISO P speed ratio. Requires a reference to be set first. |
| **Auto Estimate All** | Apply the reference calibration to **every** paper that isn't already calibrated, scaling each by its ISO P speed ratio. Already-calibrated papers are skipped. A confirmation screen appears before it runs. |
| **Clear All Calibrations** | ⚠️ **DANGEROUS** — Irreversibly wipes every paper's calibration (lux + time) back to uncalibrated. Also clears the reference snapshot. **A confirmation screen appears first — check it before pressing Yes.** Only use this when you want to start completely fresh. |

#### How cross-paper estimation works

Every paper has a manufacturer-rated ISO P speed (visible as "Base ISO P" in the Filter Editor). Faster papers (higher ISO P) need less exposure for the same density. The estimation tools exploit this — and they use each paper's **effective** base ISO P (the value shown in the **Base ISO P** label), so any ISO P override you've set is respected:

1. Calibrate **one** paper properly (§7) — this becomes your anchor.
2. Press **Set as Ref** on the Filter Editor tab to snapshot it.
3. Select a different (uncalibrated) paper, press **Est. Cal from ISO P**. The meter computes what the calibration *would* be if that paper had been used in the same enlarger setup, scaled by the speed ratio.
4. For bulk setup, press **Auto Estimate All** to populate every paper at once.

> **Important:** ISO-P-based estimation is approximate. For critical work, do a real test-strip calibration (§7) on each paper you use regularly. The estimation tools are best for getting a reasonable starting point on papers you use occasionally.

#### Workflow example

> *You've calibrated Ilford MG FB Classic with a test strip. You want a rough calibration for FOMA FOMATONE MG Classic without burning another sheet.*
>
> 1. With **Ilford / MG FB Classic** selected, go to Filter Editor → press **Set as Ref**. The label shows: *"Ref: Ilford MG FB Classic (ISO P 500, 1.42 lux × 8.8 s)"*.
> 2. Switch to **FOMA / FOMATONE MG Classic** in Settings.
> 3. Go to Filter Editor → press **Est. Cal from ISO P**. The label updates: *"Ilford MG FB Classic -> FOMATONE MG Classic (ISO P 500→30, ×16.67, est. 146.7 s)"*.
> 4. The calibration spinboxes in Settings are now pre-filled with the estimated values. You can refine them later with a real test strip.

### 9.5 Workflow example (override)

> *Your old Ilford grade 2 filter has faded and prints need more time than the meter suggests.*
>
> 1. Tab to **Filter Editor**. Choose **Ilford / MG FB Classic**. The grade dropdown shows all grades.
> 2. Select **2** from the grade dropdown. Current factor shows `2.17` (default).
> 3. You've measured that your actual grade 2 filter needs ~15% more exposure. Increase the factor spinbox to `2.50`.
> 4. Switch to the **Exposure** tab. The time now uses factor 2.50 instead of 2.17.
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

All papers work with all filter brands. For **FOMATONE MG Classic**, the DURST/MEOPTA dials (grades 0–4) are the datasheet's published values; its other colour-head rows (AGFA, KODAK, grade 5, and the Beseler/Chromega/De Vere Kodak-scale rows) are derived estimates marked with **~** in the filter lists — see DATABASE_VERIFICATION.md §8 for the derivation. For **Ilford papers**, Meopta grade 5 (200M) is also an estimate marked **~** — Ilford's table leaves grade 5 "not published", so 200M is the published grade-4½ setting (the hardest published Meopta value). Data sources: manufacturer datasheets and published technical specifications. Where no published table exists — FOMA Variant filters on Ilford papers, and the Beseler / Chromega / De Vere colour-head rows for FOMA papers — the values are derived estimates: for FOMA Variant filters on Ilford papers, the ISO R values are anchored to the paper's own published unfiltered ISO R plus the filter's published ISO-R offset, and each lengthening factor is the filter's published lengthening factor (its light loss, = ISO P without filter ÷ ISO P with filter) scaled by the ratio of the paper's own Ilford-filter factor to FOMASPEED's at the achieved ISO R; the Beseler / Chromega / De Vere colour-head rows reuse the Kodak scale, matching Ilford's own head grouping. See DATABASE_VERIFICATION.md for the full audit.

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
3. Insert the filter you want to measure. Make a second test strip, varying the time around t_no_filter × the manufacturer's stated factor (e.g. if the datasheet says 2.17× for grade 2, centre your strip around 2.17 × t_no_filter).
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

Filter extension factors multiply the *base* exposure time. The meter then applies the Schwarzschild reciprocity correction to the result if the total time exceeds 30 seconds. This means:

$$t_{\text{final}} = t_{\text{base}} \times \text{factor} \times \left(\frac{t_{\text{base}} \times \text{factor}}{t_{\text{ref}}}\right)^p$$

Where $p$ ≈ 0.07 for RC papers and ≈ 0.10 for FB papers, and $t_{\text{ref}}$ = 10 s. The reciprocity correction is applied *after* the filter factor — so an incorrect factor compounds the reciprocity error for long exposures. This is another reason to measure your real factors carefully.

---

## 13. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| **Exposure Time** shows `calibrate` | This paper has no stored calibration yet. | §7. |
| **Exposure Time** shows `measure lux` | Calibrated, but no live reading. | Press **Measure** on the Exposure tab. |
| Lux label shows `no sensor` | Light sensor not responding. | Check the sensor cable; reboot. |
| Lux label shows `error` | The sensor read failed (typically saturation at the fixed gain). | Select **Auto** in Sensor Gain, or drop the gain one step (HIGH → MED, MAX → HIGH). |
| Suggested time consistently off by 2× or ½× | Gain-stage factors uncalibrated for this device, or a different aperture / head height than when you calibrated. | Run **Sensor Light Calibration**, or recalibrate the paper. |
| Readings disagree when you switch gain | Gain-stage factors need trimming for your specific sensor. | Run **Sensor Light Calibration** (§2.2). |
| Contrast / Split tab shows `--` everywhere | One of the two readings is missing, or the paper isn't calibrated. The suggested-time label tells you which. | Measure that zone, or calibrate the paper. |
| Virtual Proof has clipping frames on every highlight cell | Negative range exceeds what the paper + filter can hold. | Pick a softer grade and press **Recompute Preview**, or switch to Split Grade. |
| Backlight looks dead | Brightness slider at 1 is intentionally very dim. | Drag right; the screen will reappear within the first few steps. |
| Calibration edits didn't stick after power cycle | They're flushed 1.5 s after the last tap. If you cut power inside that window they're lost. | Edit, pause one second, then power down. |
| Filter Editor spinboxes show stale values | Spinbox display is synchronised to the grade dropdown. | Re-select the grade from the dropdown to refresh. |
| Filter Editor "Reset to defaults" had no effect | The reset only affects the current paper. Other papers keep their overrides. | Switch to the paper you want to reset, then press the button. |
| Battery bar replaced by "Battery low — charge now" | The battery has reached ~10% charge. | Plug in USB-C to charge (§8.1). The device has no sleep mode — the warning stays visible until the battery recovers. |
| Battery bar shows empty but device still runs | The bar reads voltage under load; a sagging battery may show 0% while still having enough capacity to keep the MCU alive briefly. | Charge the battery; the low-battery warning appears at 10% as your cue (§8.1). |
| "Charging…" never goes away | Charging is inferred from the battery voltage: unplugging is recognised by the load step, and "Fully charged" appears only once the cell reaches the charger's top voltage. Some chargers terminate slightly below that voltage, so the label can stay at "Charging…" when the battery is actually full. | Normal. The battery is protected; unplug when done printing. |
| Screen flickers briefly during Measure | Normal — the backlight dims to 6% during sensor reads to prevent LCD light from contaminating lux readings (§2.1). | No action needed. |
| Filter Editor Factor / ISO R spinboxes greyed out | You have a fixed-grade paper selected (e.g. FOMA FOMASPEED Normal). These papers have a single built-in contrast — ISO R and factor cannot be changed. | Switch to a variable-contrast paper, or adjust only ISO P. |
| "No reference" when pressing Est. Cal from ISO P | You haven't set a reference paper yet. | Calibrate one paper, then press **Set as Ref** on the Filter Editor tab first. |
| "Clear All Calibrations" wiped everything | There is no confirmation dialog for this button. All calibrations are gone permanently. | Re-calibrate your most-used paper (§7), set it as reference, then use **Auto Estimate All** to restore approximate calibrations for the others. |
| Screen briefly goes dark then recovers during sensor read | The backlight dimming feature (§2.1) is active. On very long sample counts (16 reads × 600 ms integration) this can last ~10 seconds. | Reduce sample count or integration time in Settings if the flicker is distracting. |

---

## 14. Firmware updates

The device firmware can be updated with new features, paper database additions, and bug fixes from the official SpotlightIO website. Updates use the UF2 bootloader — no special tools or drivers needed.

### 14.1 How to update

1. **Download the firmware.** Visit **spotlightio.com** and download the latest `.uf2` file for your device model (SpotlightIO Digital Darkroom Meter).
2. **Connect the device.** Plug the device into your computer via USB-C while pressing with a pin the button on the top of the device. The device will appear as a USB mass-storage drive called **"RP2350"** on your computer.
3. **Drag and drop.** Drag (or copy) the downloaded `.uf2` file onto the RP23502 drive. The device copies the firmware, verifies it, and reboots automatically — all in about a second.
4. **Done.** The device restarts with the new firmware. All your calibrations, filter overrides, trim preferences, and settings are preserved — they live in a separate flash region that is not touched by firmware updates.

### 14.2 Troubleshooting updates

| Symptom | Likely cause | Fix |
|---|---|---|
| RPI-RP2 drive doesn't appear | BOOTSEL not held during reset, or USB cable is charge-only. | Try a different USB cable (data-capable). Hold BOOTSEL firmly, then tap RESET. |
| `.uf2` file is rejected (disappears immediately) | File is corrupted or not for this device. | Re-download from spotlightio.com/downloads. Check the file size matches the download page. |
| Device boots to old firmware after update | The UF2 was copied but the bootloader didn't verify it. | Re-enter bootloader mode and try again. |
| Calibrations lost after update | Very rare — only if the flash layout changed between firmware versions. | Re-calibrate your papers (§7). Consider backing up calibration values (lux × time) before major version updates. |

> **Tip:** You can check your current firmware version by looking at the splash screen at power-on. Compare it with the version listed on spotlightio.com/downloads to see if an update is available.

</small>