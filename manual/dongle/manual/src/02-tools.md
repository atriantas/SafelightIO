# 4. Contrast

## 4.1 What the two readings mean

Contrast uses two readings:

- the **highlight**: the dim spot under the enlarger, where you want detail in
  the print;
- the **shadow**: the bright spot, where you want the dark areas to separate.

The dongle compares them and answers with a time and a suggested grade. The two
readings are stored on the dongle; changing paper or grade asks the dongle to
re-price the same two readings, so you do not have to go back to the easel.

## 4.2 The screen

![Contrast: Time and Grade, the two spots, and the trims](manual/figures/screen-contrast.png)

- **Time** and **Grade** share the answer well. Both values use the same font
  size; if one has to shrink to fit, the other shrinks with it.
- **Highlights** and **Shadows** are capture tiles. Each shows the physical
  hint, the lux and its **Measure** action.
- **Fine tune** holds the four trims and the burn. It is collapsed until you
  open it.
- **Dodge & Burn** is the same symmetric burn slider as Exposure.

The line under the two values carries the midpoint lux, the range, the grade
label, the match and the burn. It is limited to two lines; if it would need a
third, it shrinks just enough instead of pushing the rest of the screen down.

## 4.3 Step by step

![Contrast: two readings produce a time and a grade](manual/figures/fig-contrast-flow.svg)

1. Confirm the paper and filter brand.
2. Tap **Measure** on **Highlights** and meter the dim spot.
3. Tap **Measure** on **Shadows** and meter the bright spot.
4. Read **Time** and **Grade** in the answer well.
5. Open **Fine tune** if the print needs adjustment; use the trims for
   highlights, shadows, exposure and contrast, and the burn for a global shift.
6. **Reset** puts every trim and the burn back to neutral. It does not clear
   the two readings.

## 4.4 How the recommendation works, without the maths

The dongle turns the two lux values into a density range, compares that range
with the paper's response and chooses the grade whose contrast fits. The time is
the exposure that places the highlight and shadow where the paper can hold
them. You do not need the formula; you need the two readings and a calibrated
paper.

## 4.5 Fixed-grade papers

A fixed-grade paper has no variable-contrast ladder. The grade rail shows the
paper's fixed grade, and **Contrast** still gives a time from the two readings.
Changing to another grade is not offered because the paper cannot use one.

## 4.6 A worked example

Meter the brightest area you want to keep detail in as **Highlights**; meter the
darkest area you want to keep separation in as **Shadows**. The answer might be
**8.4 s** at **grade 2xM1**. Set the enlarger to 8.4 seconds and the filter to
2xM1.

If the print is too contrasty, move the **Contrast** trim toward **−** in
**Fine tune**. If the highlights are too bright, move **Highlights** toward
**−**. The trims are per paper and per tool, so they survive a session change.

## 4.7 Common questions

**The answer says No time.** At least one spot has no reading. The hints under
the tiles tell you which one is missing.

**The time did not change when I changed the paper.** The app re-asks the dongle
when the paper change is confirmed; if the dongle is not ready, the old answer
stays. Check the top bar and **Setup → Meter**.

**The values have different sizes.** They should not: the two columns share one
fitted size. If you see a difference, the app is not the current build.

---

# 5. Split Grade

## 5.1 The idea

A split-grade print uses two exposures through two filters: a **soft** leg for
the highlights and a **hard** leg for the shadows. The dongle measures the same
two spots as Contrast and answers with a soft time and a hard time.

## 5.2 The screen

![Split Grade: Soft and Hard, the two spots and the Midtones pair](manual/figures/screen-split.png)

The answer well shows **Soft** and **Hard** side by side. The two values share a
font size, so the pair stays symmetrical. Under them are the conditions and the
midpoint.

The two capture tiles are the same highlight/shadow pair as Contrast.
**Fine tune** adds one control that Contrast does not have: the **Midtones**
pair. The pair is the meter's own soft/hard ladder position; **Reset** resets it
to the ladder's centre together with the four trims.

## 5.3 Step by step

1. Choose the paper and brand.
2. Meter the dim spot as **Highlights**.
3. Meter the bright spot as **Shadows**.
4. Read **Soft** and **Hard**.
5. Expose the print in two steps: the soft time through the soft filter, then
   the hard time through the hard filter. Cover the paper between the two.
6. If the print needs a different split, adjust **Midtones** in **Fine tune**;
   the dongle recalculates the pair from the stored readings.

## 5.4 How the split is chosen, without the maths

The dongle divides the tonal range between the two filters. The soft leg holds
the highlight and the hard leg builds the shadow. The **Midtones** control moves
the balance between the legs; it is not an exposure compensation and not a
contrast trim.

## 5.5 A worked example

The answer might be **Soft 5.2 s** and **Hard 3.1 s** at grade 2. Expose 5.2
seconds through the soft filter, then 3.1 seconds through the hard filter. If
the midtones are too heavy, move **Midtones** toward the hard side and make
another print; the dongle keeps the same two readings.

## 5.6 Common questions

**One time is missing.** The pair is computed only when both spots exist. The
hint under the missing tile says which spot to meter.

**Reset did not change the times.** Reset clears the trims and the Midtones
pair; the times are recomputed from the same two readings. If the paper has no
pair table, the Midtones row is inert.

**The two times look different in size.** They share one fitted size by design.
If they do not, update the app.

---

# 6. Virtual Proof

## 6.1 What it does

Virtual Proof turns a grid of easel readings into a picture of the print. In
normal (negative) mode, the cells show the meter's grayscale proof: where the
print will be light, where it will be dark, and which cells are clipped.

In **Enlarger Mode**, the same grid measures the enlarger's evenness: the cells
show deviation from the reference, and the answer is a uniformity verdict.

## 6.2 The screen

![Virtual Proof: the cell canvas and its controls](manual/figures/screen-proof.png)

- The **cell canvas** is the main surface. The controls that move it are at the
  bottom of the same card: **Start scan**, **Set V Zone** (or **Set Reference**
  in Enlarger Mode), **Clear Grid**, the status line, and the **Columns** /
  **Rows** steppers.
- **Selected sample** shows the tapped cell's readouts.
- **Result** shows the measured count, range, mean, min, max and range fit. In
  normal mode it does **not** show Uniformity, Min/max spread or Worst cell;
  those belong to Enlarger Mode.
- **Filter grade** shows the proof grade rail. It is the grid's own grade, not
  the Exposure grade.
- **Histogram** is a disclosure card.
- **Settings** is a disclosure card below the histogram.

The explaining legend below the canvas is not permanent. It appears as a
dismissible banner only after a completed scan.

## 6.3 The grid frames

![The proof grid: selected, next, Zone V and clipping frames](manual/figures/fig-proof-grid.svg)

- **Red frame:** the selected cell; its values are in **Selected sample**.
- **Muted red / orange frame:** the next cell the scan will write.
- **Dark red frame:** the Zone V reference cell.
- **Bright or dim edge:** the cell is clipped at the highlight or shadow end.
- **Gray fill:** the meter's proof tone, 0 black to 255 white.

The legend is a reminder, not a second control list. The same information is in
this chapter.

## 6.4 A proof in ten steps

1. Choose the paper and filter brand.
2. Open **Proof**.
3. Set **Columns** and **Rows**; 3 × 3 is a good first proof.
4. Tap **Start scan**. The dongle measures each cell in turn.
5. If you scan by hand, move the sensor to the next cell and tap the action
   again. The app names the next cell.
6. Let the scan complete. The legend banner appears; read it once, then close
   it if you do not need it.
7. Tap a cell to inspect its **Selected sample**.
8. Read **Result** for the measured count and range.
9. Use **Histogram** if you want the distribution; it is above **Settings**.
10. Use **Settings** for Stability Detection, tolerance and the settle gate.

**Stop** appears while a scan is running. **Clear Grid** starts a new proof; it
does not change the paper or the calibration.

> [!NOTE] Set V Zone
> **Set V Zone** takes the selected measured cell as the grid's reference. In
> Enlarger Mode the same button is called **Set Reference**. It is enabled only
> when the tapped cell can serve as the anchor.

## 6.5 Enlarger Mode

Turn on **Enlarger Mode** in the **Settings** card. The answer well appears at
the top with the uniformity verdict; the result rows include **Uniformity** and
**Worst cell**. Use the grid to find hot spots and falloff in the enlarger's
light.

When **Enlarger Mode** is off, the verdict is not shown; the canvas is the main
theme and the result stays a print result. This is deliberate: a uniformity
percentage is meaningless for a negative proof.

---
