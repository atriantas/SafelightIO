# 4. Contrast

**Use this tab when you want the meter to recommend a contrast grade.**

![Contrast flow: two readings, one grade, one time](manual/figures/fig-contrast-flow.svg)

## 4.1 What the two readings mean

The meter needs two points in the projected image:

- **HIGHLIGHTS** — the **dim spot at easel**. A highlight on the print comes from a
  dense part of the negative, so less light reaches the easel.
- **SHADOWS** — the **bright spot at easel**. A shadow on the print comes from a
  clear part of the negative, so more light reaches the easel.

This is the part that surprises people. Measure the **dim** part for highlights and
the **bright** part for shadows. The small labels under the headings say exactly
that, so you do not have to remember.

![The Contrast tab on the device](manual/figures/screen-contrast.png)

## 4.2 Every control and readout

| Element | What it is | What to do |
|---|---|---|
| **CONTRAST CALCULATOR** | The tab heading | — |
| **HIGHLIGHTS** + **dim spot at easel** | The highlight reading area | Put the sensor on the dimmest important highlight and press **Measure Highlight** |
| **SHADOWS** + **bright spot at easel** | The shadow reading area | Put the sensor on the brightest important shadow and press **Measure Shadow** |
| **Highlight lux reading** | The light measured at the highlight | Read-only |
| **Shadow lux reading** | The light measured at the shadow | Read-only |
| **CONTRAST RANGE** | The brightness range of the negative in stops | Read-only; roughly 3 stops is gentle, 5 stops is contrasty |
| **CONTRAST GRADE** | The grade the meter recommends | The starting point for your filter choice |
| **Filter Grade** | The grade used for the time calculation | Shows the recommended grade; the time includes its factor |
| **Match Quality** | How closely the negative fits that grade: **Exact**, **Close**, **Acceptable** or **Approximate** | **Exact**/**Close** need no action; **Acceptable** is a compromise; **Approximate** means no grade comes close — usually the negative is outside what the paper can reach |
| **Analysis reasoning** | The explanation line under Match Quality | Read why the device chose the grade |
| **EXPOSURE TIME** | The suggested time at the midpoint | Read it |
| **Midpoint Time** | The time for the midtone | Read-only; includes all four trims, before the dodge/burn slider |
| **Midpoint LUX** | The light level of the midtone, derived from the two readings | Read-only |
| **Exposure Note** | A note about reciprocity and the time sanity check | Read it; it explains any long-exposure correction |
| **CALIBRATION CONSTANT** | The paper's lux × seconds constant | Read-only |
| **Measure Highlight** | Takes the highlight reading | Press once, with the sensor on the dim spot |
| **Measure Shadow** | Takes the shadow reading | Press once, with the sensor on the bright spot |
| **TUNABLES** | The four trim sliders | Use only when you want to override the recommendation |
| **Exposure** | Shifts the whole exposure up or down, ±1.5 stops in 1/6-stop steps | Adjust if the print is consistently light/dark |
| **Contrast** | Biases the grade softer or harder, ±1.5 stops | Adjust if the print needs more/less contrast than recommended |
| **Highlights** | Trims the highlight end, ±1.5 stops | Adjust if highlights print too light or too dark |
| **Shadows** | Trims the shadow end, ±1.5 stops | Adjust if shadows print too light or too dark |
| **Saved per paper** | Tells you the trims belong to the selected paper | Remember: changing paper loads that paper's own trims |
| **Reset** | Returns the four trims to neutral for the current paper | Use after experimenting |
| **DODGE & BURN** | A final whole-print trim | See below |
| **Additional time (Contrast)** | The seconds the dodge/burn slider adds | Read-only |
| **Total time (Contrast)** | The time to expose | Use this at the enlarger |
| **F-Stop** | The dodge/burn slider position in stops | Read-only |
| **Dodge and burn slider (Contrast)** | Adds/removes exposure in ¼-stop steps, ±2.25 stops | Drag right to darken, left to lighten |

## 4.3 Step by step

1. Select the paper in the sidebar.
2. Put the sensor on the **dimmest important highlight** and press **Measure
   Highlight**. Keep your body out of the light.
3. Put the sensor on the **brightest important shadow** and press **Measure
   Shadow**.
4. Read **CONTRAST RANGE**, **CONTRAST GRADE** and **Match Quality**.
5. Put the recommended grade in the enlarger. The **Filter Grade** readout already
   includes that grade's exposure factor.
6. Read **EXPOSURE TIME** (or **Total time** if you use the dodge/burn slider).
7. If the print is consistently off, use the **TUNABLES** and the **Reset** button.

> [!TIP] If you only have one reading
> Both readings are required. With one missing, the tab shows `--` and the
> **EXPOSURE TIME** line says which reading is missing. Measure the missing point
> and the result appears immediately.

> [!NOTE] 0.00 lux is a real reading
> A reading of 0.00 lux is below the sensor's usable range, not a missing one. The
> tab says `highlight below range` or `shadow below range` and keeps the other
> reading; add light, gain or integration and measure again.

## 4.4 How the recommendation works, without the maths

The two readings give a **brightness range**. A negative with a small range is
flat and needs a harder grade; a negative with a large range is contrasty and needs
a softer grade. The meter compares the range with the paper's contrast data and
picks the closest grade.

- **CONTRAST RANGE** is in stops of exposure.
- **CONTRAST GRADE** is the recommended filter grade.
- The **time** is taken from the middle of the two readings, so the midtone stays
  put when you change grade.
- **Match Quality** tells you how well the negative fits the paper's range.
- The **trims** let you move the result without recalibrating.

## 4.5 Fixed-grade papers

Some papers have one fixed contrast grade. For those papers the tab shows **Fixed
grade** and:

- the **Contrast**, **Highlights** and **Shadows** sliders are disabled — a fixed
  grade cannot be biased and its ends cannot be re-interpreted; the **Exposure**
  slider still shifts the exposure time;
- **Split Grade** is not applicable;
- in the **Control Panel**, the Factor and ISO R fields are disabled; only ISO P
  can be changed.

The **Analysis reasoning** line compares the negative's ISO R target with the
paper's fixed ISO R. When the negative is more than about half a stop outside the
paper's range, it warns that highlights may block (negative too contrasty) or that
the print will lose contrast (negative too flat), and suggests a softer or harder
paper.

The eight fixed-grade papers are listed in chapter 11.2. If you are printing on one,
use **Exposure** and choose the filter grade that matches the paper's grade.

## 4.6 A worked example

A landscape negative on Ilford Multigrade RC Deluxe:

- highlight reading **0.32 lux** (the dim spot);
- shadow reading **4.10 lux** (the bright spot);
- the range is about **3.7 stops**;
- the meter recommends grade **1** with **Exact** match;
- **EXPOSURE TIME** is **14.2 s**.

A grade 1 filter is soft, which suits the contrasty negative. If the print's
highlights are too bright, add a small **Highlights** trim; if the shadows are
muddy, add a **Shadows** trim.

## 4.7 Common questions

**The grade changes when I move one reading slightly.** Small changes near a grade
boundary can flip the recommendation. Look at **Match Quality**; **Close** means
either neighbouring grade is reasonable.

**The time is not what I expected.** The time is for the midpoint, not for the
highlight. That is deliberate: it keeps the midtone stable when you change grade.

**Should I use Contrast or Split Grade?** Use Contrast when one grade suits the
whole print. Use Split Grade when the shadows and highlights need different filters.

---

# 5. Split Grade

**Use this tab when shadows and highlights need different contrast.**

![Split Grade: a soft leg and a hard leg, added together](manual/figures/fig-split-flow.svg)

## 5.1 The idea

Split-grade printing gives the print two exposures through two filters:

- a **soft** filter for the highlights and midtones;
- a **hard** filter for the shadows and blacks.

The meter measures the same two points as the Contrast tab, then works out how much
of the total exposure each leg should carry. The result is a pair of times that add
up to the print you want.

![The Split Grade tab on the device](manual/figures/screen-split.png)

## 5.2 Every control and readout

| Element | What it is | What to do |
|---|---|---|
| **SPLIT GRADE CALCULATOR** | The tab heading | — |
| **HIGHLIGHTS** + **dim spot at easel** | Highlight measurement area | Measure the dim part of the image |
| **SHADOWS** + **bright spot at easel** | Shadow measurement area | Measure the bright part |
| **Split highlight lux reading** | Highlight light level | Read-only |
| **Split shadow lux reading** | Shadow light level | Read-only |
| **CONTRAST RANGE** | The negative's range in stops | Read-only |
| **Equivalent grade readout** | The single grade that would be closest to this split | Useful as a sanity check |
| **SOFT EXPOSURE** | The soft leg's filter name and time | Use this filter for the soft exposure |
| **Soft filter name** | The soft filter chosen by the meter | Changes with **Midtones** and paper |
| **Soft exposure time** | Seconds for the soft leg | Read-only |
| **HARD EXPOSURE** | The hard leg's filter name and time | Use this filter for the hard exposure |
| **Hard filter name** | The hard filter chosen by the meter | Changes with **Midtones** and paper |
| **Hard exposure time** | Seconds for the hard leg | Read-only |
| **TOTAL EXPOSURE TIME** | Soft + hard time | The total time the paper receives |
| **CALIBRATION CONSTANT** | The paper's constant | Read-only |
| **ANALYSIS DETAILS** | The reasoning: percentages of soft/hard light, and any warnings | Read it before printing |
| **Measure Highlight** / **Measure Shadow** | Take the two readings | Same as Contrast |
| **TUNABLES** | Five trims | Use after the first test print |
| **Exposure** | Shifts the total exposure, ±1.5 stops in 1/6-stop steps | Lighten/darken the whole print |
| **Contrast** | Biases the overall contrast, ±1.5 stops | More/less separation |
| **Highlights** | Reinterprets the highlight reading, ±1.5 stops | Shifts the highlight end; changes the grade, split and total together |
| **Midtones** | Chooses the soft/hard pair (e.g. `00 + 5`) | Steps the pair from the paper's extremes inward |
| **Shadows** | Reinterprets the shadow reading, ±1.5 stops | Shifts the shadow end; changes the grade, split and total together |
| **Saved per paper** | The trims belong to the selected paper | Changing paper loads its own trims |
| **Reset** | Returns all five trims to neutral | Use after experimenting |
| **DODGE & BURN** | Adds a final whole-print trim to both legs | See below |
| **Additional soft time** | Seconds added to the soft leg | Read-only |
| **Total soft time** | Soft leg after the trim | Use this at the enlarger |
| **Additional hard time** | Seconds added to the hard leg | Read-only |
| **Total hard time** | Hard leg after the trim | Use this at the enlarger |
| **F-Stop** | Dodge/burn slider position | Read-only |
| **Dodge and burn slider (Split Grade)** | Adds/removes exposure, ±2.25 stops | Drag right to darken, left to lighten |

## 5.3 Step by step

1. Select the paper and filter brand.
2. Measure the dim highlight and the bright shadow, as in chapter 3.
3. Read the **SOFT EXPOSURE** and **HARD EXPOSURE** names and times.
4. Expose the print: soft leg first, then hard leg (or the reverse, if your workflow
   prefers; the total light is the same).
5. If the print needs adjustment, use the trims, then **Reset** to start again.
6. Use **DODGE & BURN** only for a final whole-print shift; it scales both legs.

> [!WARNING] Watch the analysis details
> The meter may warn that **highlights may burn** or that contrast is **limited**.
> Those come from the paper-wide ISO R range: the negative is outside what the
> selected paper and filter brand can hold, and no Midtones setting changes that.
> Use a softer or harder paper, or a different filter brand. A separate
> **pair too narrow** warning is the one **Midtones** can fix: move it toward the
> extremes to widen the pair.

## 5.4 How the split is chosen, without the maths

The meter decides what share of the light each leg should carry. At one extreme the
print is almost all soft; at the other, almost all hard. The **Midtones** slider
moves that balance. The meter keeps the midtone anchored, so changing the balance
does not make the whole print lighter or darker; it changes how the shadows and
highlights separate.

The **Highlights** and **Shadows** trims reinterpret the two readings, as on the
Contrast tab: they change the recommended grade, the split ratio and the total
time together, not one leg on its own. **Exposure** scales the total time and
leaves the ratio alone; **Contrast** biases the split toward hard (positive) or
soft (negative).

## 5.5 A worked example

A portrait negative:

- highlight **0.12 lux**;
- shadow **8.00 lux**;
- the range is about **6.1 stops**;
- the equivalent grade is **00**;
- soft leg: grade **00**, **29.5 s**;
- hard leg: grade **5**, **6.9 s**;
- total **36.4 s**.

The soft leg carries most of the light (about 89%) because the negative is very
contrasty. To move one end of the print without re-measuring, use the **Highlights** or
**Shadows** trim; both change the split and the total, so re-read the times.

## 5.6 Common questions

**Why are there two times?** The paper receives both exposures. The total is their
sum; the split decides where the contrast goes.

**Which leg first?** It does not matter for the total exposure. Many printers do
soft first, then hard; choose one order and keep it for consistency.

**The soft and hard filters look odd.** The names follow the selected **Filter
Brand**; for FOMA papers a “Special” grade may appear as one of the legs. That is
normal.

**Can I use Split Grade on a fixed-grade paper?** No. The tab will tell you it is
not applicable. Use **Exposure**.

---

# 6. Virtual Proof

**Use this tab when you want to see how the print will look across the easel before
you commit a sheet.**

![Virtual proof: the grid, the frames and the scan order](manual/figures/fig-proof-grid.svg)

## 6.1 What it does

The grid divides the easel into cells. You measure each cell; the device paints each
cell with the gray it expects on the print at the selected paper and grade. The
result is a low-resolution preview of the print, plus a histogram of the tones.

It is a proof, not a scanner: the preview is only as good as the cells you measured.

![The Virtual Proof tab on the device](manual/figures/screen-proof.png)

## 6.2 Every control and readout

| Element | What it is | What to do |
|---|---|---|
| **Grid Size** | Sets the grid's width and height | Choose 3–5 cells per side for a quick proof; more cells for a detailed one |
| **Grid width** | Cells across, 2–40 | Changing the size clears the grid |
| **Grid height** | Cells down, 2–30 | Changing the size clears the grid |
| **Measure** | Reads the next cell | Press once per cell; with **Stability Detection** on it becomes **Start scan (n/total)** / **Stop scan (n/total)** and walks the grid for you |
| **Set V Zone** | Makes the selected cell the Zone V reference | Use it when you know which cell is the middle gray |
| **Clear Grid** | Erases all cells, the selection and the reference | Start a new proof |
| **Grid canvas** | The painted preview | Tap a cell to select it |
| **HISTOGRAM** | Distribution of the predicted gray values | Read the shape: left is shadow, right is highlight |
| **SELECTED SAMPLE** | The readouts for the selected cell | Tap a cell to inspect it |
| **Lux (selected sample)** | The measured light in that cell | Read-only |
| **Zone (selected sample)** | The predicted zone of that cell | Read-only |
| **ISO R (selected sample)** | The contrast range of the paper at this grade | Read-only |
| **EV Range (selected sample)** | The exposure range represented by the cell | Read-only |
| **Density (selected sample)** | The predicted print density | Read-only |
| **Exposure (selected sample)** | The exposure time for that cell | Read-only |
| **Clipping (selected sample)** | Whether the cell falls off the paper's range | If it clips, choose a different grade or split |
| **SETTINGS** | The proof's options | — |
| **Filter grade selector (Virtual Proof)** | The grade used to render the preview | Change it to see a different grade; the grid re-renders. The choice survives a paper or filter-brand change while the new paper offers the same grade |
| **Enlarger Mode switch** | Turns the proof into a light-evenness test (section 6.5) | Use it with no negative in the carrier |
| **Uniformity Limit** | The allowed brightness variation in Enlarger mode, 5–50% (default 15%) | Set it to what your printing requires |
| **Stability Detection switch** | Turns on automatic settling during a scan | Use it for hands-free scans |
| **Tolerance (%)** | How far a reading may move from the start of a stable run and still count as stable | Smaller is stricter |
| **Min Stable Reads** | How many reads in a row must stay inside Tolerance | More is stricter |
| **Max Wait (ms)** | The longest the meter waits for a cell to settle | If a cell does not settle in this time the scan stops and keeps no reading for it |
| **Min Delta (lux)** | A floor for very dim cells | Stops noise from looking like change |

> [!NOTE] The stability fields
> The four stability fields are used when **Stability Detection** is on. With it
> off, each press of **Measure** records a single reading immediately.

> [!IMPORTANT] Only settled readings are recorded
> With **Stability Detection** on, a cell is stored only after its reading has
> stopped moving: every read in the run must stay within **Tolerance** of the
> run's first reading, and the averaged sample that follows must stay inside the
> same window. If a cell cannot settle within **Max Wait**, the scan stops, the
> button reads **No stable reading**, and nothing is recorded for that cell — the
> cursor stays on it, so pressing **Start scan** again retries it. A drifting
> light therefore ends the scan instead of quietly recording a value the light
> never held.

> [!TIP] Size Max Wait to your integration time
> Reaching a stable run takes about **Min Stable Reads + 1** readings, each one
> integration long. Allow at least that much time: with Integration 600 ms and 3
> stable reads you need about 3 s, so the factory 2 s is only enough for the
> 200 ms default. Too short a **Max Wait** ends the scan on the first cell.

> [!NOTE] The first reference is chosen for you
> When an automatic scan finishes, the meter picks a provisional Zone V
> reference: the cell nearest the middle of the measured brightness range in
> exposure terms. It is a starting point, not a guarantee that the cell is your
> middle gray. Select the cell you trust and press **Set V Zone** to take over.
> A manual, one-cell-at-a-time proof does not set a reference automatically.

## 6.3 The grid frames

The frame colour tells you what a cell is:

| Frame | Meaning |
|---|---|
| **Amber** | The next cell the meter will read |
| **Red** | The cell you selected |
| **Cyan** | The Zone V reference cell |
| **Light gray** | Highlight clipping — the cell is too bright for the paper |
| **Dark gray** | Shadow clipping — the cell is too dark for the paper |
| **No frame** | An ordinary measured cell |

Colour is a shortcut, not the only cue: the selected sample readouts and the
histogram tell you the same story in numbers.

> [!NOTE] A cell that reads 0.00 lux is still a cell
> When the sensor reads exactly zero — the negative blocks all light at that point —
> the meter keeps it as a real measurement. The cell is painted paper white with a
> highlight-clip frame, it counts in the histogram and in the `n/total` total, and it
> is saved with the session. A 0.00 cell is never treated as "not measured".

## 6.4 A proof in ten steps

1. Set **Grid Size** to a small grid, for example 4 × 3.
2. Choose the **Filter grade** you intend to print.
3. Press **Measure** for the first cell and place the sensor in the highlighted
   cell.
4. Keep pressing **Measure** (or turn on **Stability Detection** and let the meter
   scan) until the grid is filled.
5. Read the **HISTOGRAM**. A shape crowded on the right means the print will be
   bright; crowded on the left means dark.
6. Tap a cell to see its **SELECTED SAMPLE** readouts.
7. If you know the middle gray, select that cell and press **Set V Zone**.
8. Change the grade and watch the grid re-render.
9. **Clear Grid** to start again; changing **Grid Size** also clears it.
10. Save the session if the proof is worth keeping (chapter 9).

> [!TIP] A quick proof is better than no proof
> Six cells tell you whether the print is basically even. You do not need a
> 40 × 30 grid to catch a hot corner or a vignette.

## 6.5 Enlarger mode — is the light even?

Enlarger mode uses the same grid, but there is **no negative in the carrier**. The
grid becomes a map of the bare enlarger light.

![Enlarger uniformity map and verdicts](manual/figures/fig-enlarger-map.svg)

**Set up:**

1. Remove the negative. Leave the carrier empty.
2. Set the lens to the aperture and the head to the height you will print at.
3. Let the lamp warm up.
4. Put an opal diffuser over the sensor if you have one; do not let the meter shadow
   the point you are measuring.
5. Turn **Enlarger Mode** on. The filter grade selector is not used in this mode.
6. Set **Grid Size** to 3 × 3 (nine points) or 5 × 5 for a finer map.
7. Press **Measure** for each point, or turn on **Stability Detection** and scan.
8. Select the centre cell and press **Set Reference**. The centre is the reference
   for the deviation readouts.

**The readouts:**

| Readout | Meaning |
|---|---|
| **Lux** | The light at the selected point |
| **Dev %** | How far the point deviates from the reference, in percent |
| **Dev EV** | The same deviation in stops |
| **Range** | The spread between the brightest and dimmest points |
| **Mean** | The average of all measured points |
| **Min–Max** | The dimmest and brightest points |
| **Verdict** | **GOOD**, **MARGINAL** or **UNEVEN** |

**The verdict:**

- **GOOD** — every point is within half the **Uniformity Limit**.
- **MARGINAL** — the worst point is between half the limit and the full limit.
- **UNEVEN** — the worst point is beyond the limit.

A point reading exactly **0.00 lux** counts as measured and forces **UNEVEN**: the
readout shows **Dev −100%** for it, because no light reaches the easel there at all.

The default limit is **15%**, which is roughly 0.2 stop. That is a reasonable
working tolerance for most enlargers and papers. A stricter limit (for example 10%)
is useful for critical work; a looser one (25–30%) may be acceptable for rough
proofs.

**What the map tells you:**

- dark corners — condenser or diffuser misalignment, or a lens that does not cover
  the format;
- a bright centre with dark edges — normal falloff for a condenser enlarger, worse
  at large magnification;
- an off-centre hot spot — the lamp is not centred;
- a single dark cell — something is shadowing that point (your hand, the meter, a
  cable).

Enlarger mode measurements are kept when you switch back to negative mode, so you
can inspect them later. Saving the session stores the mode and the grid
(chapter 9).
