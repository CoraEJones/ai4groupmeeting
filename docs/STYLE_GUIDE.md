# Yiyu reference-deck style guide (from `yiyu_reference.pptx`, 31 slides)

Source: `/workspace/slides/style-ref/yiyu_reference.pptx` (PowerPoint 16; footer says "Meta-Optics @ Tsinghua University"). This is the group's English group-meeting style.
Renders: `renders/full-1/slide-NN.jpg`, contact sheet `renders/full-1/contact.jpg`, grids `renders/full-1/grid-{1,2,3}.jpg`.
Representative renders: `renders/representative/slide-{01,03,10,21,26}.jpg`.
All measurements are in inches (EMU / 914400). They come from the slide XML.

---

## 1. One-paragraph summary (the "look")
This is a clean, flat, white **16:9 research-talk** look with a single **steel-blue accent `#316886`**. Every content slide has a light-grey full-width title band with a blue tab on the left, and a left-aligned, bold, blue Calibri title. The content is built from **figures plus short phrases, not bullets**. Blue rounded "pill" bars label the columns. Light-grey rounded "takeaway" bars carry the one-sentence message, with **key words in bold blue**. Equations are pasted as images. Every content slide has a small group logo bottom-left and a grey page-number square bottom-right. There are no animations, no speaker notes, no bullets and no decorative imagery.

## 2. Slide setup, master, layouts, background
- Size: **13.333 × 7.5 in (16:9, 12192000 × 6858000 EMU)**.
- 4 masters and 31 layouts exist (leftovers from merged decks: Office theme, a Chinese "自定义主题", and others). **All 31 slides use one layout: `slideLayout12` → `slideMaster2` → `theme2`**, and that layout is **empty** (no placeholders).
- The theme is default Office 2013+ (dk2 44546A, accents 4472C4/ED7D31/A5A5A5/FFC000/5B9BD5/70AD47). The theme fonts are Arial, but the real text uses **Calibri** set by hand on each run. The accent colour is not in the theme; it is set as a direct `srgbClr`.
- **Every element is a free-floating shape, text box or picture, with no placeholders.** The title bar, logo and page number are drawn again on each slide. They are not on the master.
- Background: solid **white `#FFFFFF`** on every slide. There are no images, gradients or textures behind the content.
- To imitate it, use a blank layout and place the chrome on each slide (or put it on a master, which gives the same visual result).

## 3. Slide chrome (repeated on every content slide, slides 2–31)
| Element | Geometry (x, y, w × h) | Style |
|---|---|---|
| Title band | 0, 0, 13.33 × 0.92 | Rect (roundRect with adj 0). **Horizontal gradient F2F2F2 at 100% → F2F2F2 at 64% alpha**, so it reads as a very light grey (about #F2F2F2), no outline |
| Left accent tab | 0, 0, 0.31 × 0.92 | Solid **#316886**, no outline |
| Title text box | 0.31, 0, 12.72 × 0.92 | Calibri **28 pt bold #316886** (28 pt on 26 of 30 content slides; 32 pt on slide 14, 36 pt on slides 2 and 30), left-aligned, vertically centred, insets 0.1/0.05 in, single line, no autofit |
| Footer logo | 0.31, 7.00, 2.71 × 0.42 | PNG `ppt/media/image2.png`: dot-grid logo + "Meta-Optics @ Tsinghua University" + red URL `https://www.thumetaoptics.com` |
| Page-number tile | 12.57, 7.03, 0.42 × 0.40 | Square, fill **#F2F2F2**, no outline |
| Page number | 12.54, 7.03, 0.49 × 0.40 | Calibri **16 pt regular**, colour #316886 (#2F5597 on a few slides, an inconsistency), centred on the tile |
- There is no underline under the title, no subtitle line, no section markers, no progress bar or agenda tracker, and no date or footer text.
- Titles are short claims or topic phrases in sentence case, e.g. "Challenge: all six motions must be observable", "Drift: the VCSEL dominates the optical error", "Principle", "Outlook". Some titles repeat over 2–3 slides ("Joint design by mutual-information optimization" on slides 10–13) as an informal section marker.

### Title slide (slide 1), different from the others
- It has no title band, logo or page number.
- Title: Calibri **32 pt bold #316886**, centred, two lines, box at (0.91, 0.47) 11.23 × 1.18.
- Author block: Calibri **24 pt black**, centred, line spacing 125%. The name is bold, then department and university are regular ("Tsinghua University, CHINA").
- The bottom ~45% of the slide is a **wide hero schematic** of the work: three images across (0.29–13.04 in, y 3.56–6.62) with a caption-arrow image under them.

### Closing slides
- Slide 29 is "Outlook" (two-column figures with blue down-arrows). Slide 30 is "Discussion", the one off-style slide: a plain numbered list in the theme's Arial 24 pt with a leftover hidden Chinese placeholder. Do not copy slide 30. Slide 31 is a backup/appendix plot slide.
- There is no "Thank you" or "Questions" slide.

## 4. Typography
- Font: **Calibri for everything**, including titles, labels, tables and takeaways. Math symbols (θ, φ, ∂I/∂q) are runs in **Arial** or italic Calibri with sub/superscripts made by baseline offset (−25% subscript, +30% superscript). There is a single stray Microsoft YaHei run (hidden).
- Distinct sizes in use. The 11 pt values in the XML are only empty `endParaRPr` and never show.
  - **36 / 32 pt**: rare title variants
  - **28 pt bold**: slide titles (standard)
  - **24 pt**: title-slide author block; slide 30 list
  - **20 pt**: main body size, used for column-header pills (bold white), takeaway bars, and phrase captions under figures
  - **18 pt**: secondary size, used for small pills, figure labels, table text, sub-headings (bold blue)
  - **16 pt**: page numbers
  - **12 pt**: literature citations in the comparison table
  - Smallest visible slide text is 12 pt (citations only). Normal text is never below 18 pt.
- Weight and colour roles:
  - Normal text: **black #000000, regular** (a few runs are #1F2329)
  - Emphasis: **bold + #316886** on the key word or phrase *inside* a black sentence. This is the signature move: "One observation: some motions are **hidden**", "MI: **observability and conditioning** in one decoder-independent number".
  - Secondary or "consequence" line: regular #316886 (e.g. "Sideways: hidden" under "1 beam → 1 distance")
  - Text on blue: white bold
- Line spacing is tight: 83% on free labels and 92% in pills. Text boxes have **zero insets** and are vertically centred.
- Alignment: text under or beside a figure is centred in its column, or left-aligned next to the figure. Takeaways are centred.
- **No bullets anywhere** (0 `buChar`/`buAutoNum` in content). Text comes as short phrases of 1–2 lines each.
- Text amount: median ~35 words per slide (range 2–64; the comparison table slide has 131 including citations). A typical slide has a title, 2–3 pill headers, 3–6 short phrases of ≤ 10 words each, and one takeaway sentence.
- The arrow glyph "→" is used heavily inside text ("hidden → revealed", "1 point → (u, v)"), along with "↑" for improvement.

## 5. Colour palette
| Role | Hex | Use |
|---|---|---|
| Primary accent | **#316886** (steel/teal blue) | title text, left title tab, pill fills, table headers, emphasis words, down-arrows, connectors on key paths |
| Text | #000000 (some #1F2329) | body text |
| On-accent text | #FFFFFF | pills, table headers |
| Takeaway / highlight fill | **#E7E6E6** | rounded takeaway bars; "This work" table row |
| Light panel | **#F2F2F2** | title band (gradient), page tile, alternating table bands |
| Rule line | #C9D3DA | thin 1 pt divider after a sub-heading (slide 2) |
| Neutral mark | #A6A6A6 | grey bars in the information-budget chart (slide 18) |
| Variant blue | #2F5597 | page number on some slides (inconsistent; prefer #316886) |
- The palette is **monochrome blue + greys**. Other colours (orange/copper VCSEL, red arrows, green/orange scatter points) only appear inside figures. There is no second UI accent.

## 6. Shapes, highlight boxes and callouts
1. **Column-header pill** (most common element, on ~20 slides): `roundRect` adj ≈ 9491 (corner radius ≈ 0.045 in at h 0.47, nearly square), fill #316886, 1 pt #316886 outline, **h 0.47 in** at **y = 1.11**, text 20 pt bold white centred, insets 0.083/0.028 in. Its width equals the column width (6.22 for 2 columns, 4.06 for 3 columns, or full width). A **small pill** variant is h 0.39–0.42, adj ≈ 10756–11525, 18 pt bold white; it labels individual figures in diagrams (slides 9, 11, 13).
2. **Takeaway / message bar** (on ~14 slides): `roundRect` adj 13000–23500 (corner radius ≈ 0.08–0.1 in, softly rounded), fill **#E7E6E6**, **no outline**, h 0.36–0.75. Text is 20 pt (18 on dense slides) and centred: black regular plus **bold #316886 keywords**. It sits in two places:
   - **Bottom conclusion**: x 0.97–1.33, w 10.67–11.39 (centred, inset from the margins), y ≈ 6.19–6.44, just above the footer.
   - **Full-width row divider**: x 0.31, w 12.72, h 0.39–0.42, under the pills. It states the observation for the figure row below it (slides 3–5: "One observation…" / "More observations…").
3. **Sub-heading with rule** (slide 2): 18 pt bold #316886 text followed by a 1 pt #C9D3DA horizontal line to the column edge.
4. **Arrows**: straight connectors with small arrowheads, **2 pt black** (sometimes #316886) between figure stages, 1 pt for chart pointers. There are freeform elbow arrows (2–3 pt, accent for the "our method" path), block `downArrow`s filled #316886 (0.42 × 0.53) for "therefore" steps, and an outlined rounded "Inference" box (1 pt black, adj 15000).
5. There are no shadows, glows, 3-D, icons or clip-art. Every corner is near-square or softly rounded; nothing uses pill-capsule radii.

## 7. Figures
- **Figures dominate.** Pictures cover ~10–66% of the slide area (median ~41%). There are 142 media files; slides carry 1–15 pictures each.
- Figures are flat PNGs on a white or very light background. They have **no borders, frames or shadows**, and are placed edge-aligned to the column grid. Some figures have their own light panel background (e.g. a grey derivative-map panel on slide 10, cream/blue panels on slide 1).
- Arrangement patterns:
  - **Two columns** with a pill over each (slides 3, 4, 6, 7, 23, 28): figure blocks of 6.22 or 5.8–6.7 in wide.
  - **Three equal columns** of 4.06 in (slide 21): pill, then photo/diagram, then a centred 2-line caption, then a full-width takeaway.
  - **Thumbnail grids** of small images (1.97 × 1.39 in, 4 per row, 0.14 in gutter, label under each; slide 2) or 1.67 in squares in a row with arrows between them (slide 13).
  - **Flow diagram** (slide 9): left panel → two middle panels → right panel, joined by black diagonal arrows, each with a small pill title and a bold-blue result word ("Observability ↑", "Both ↑").
  - **One big figure**: full width 12.72 × 5.17 (slides 24, 25) or 12.22 × 3.42 (slide 16), with a takeaway bar below.
  - **Paired plots** at 5.9–6.2 in each, side by side (slides 19, 20), with a table or takeaway below.
- Captions are short phrases in 18–20 pt placed **under** the figure (centred) or **to the right** of it. They never use "Fig. 1" numbering. Labels sit directly on the image (e.g. "Shift", "Tilt", "Source", "Camera").
- Source citations are rare. Literature appears only in the comparison table, as 12 pt "X. Li, et al. Opt. Eng. 53, 122405 (2014)" or "API, XD6 LP datasheet (2026)" under each method name. Borrowed figures (slide 21 panels "(c)", "(d)") carry no on-slide citation. If you add sources, use the same 12 pt author-journal-volume-page-year form, black, under the item.

## 8. Equations
- **No OMML** (0 `m:oMath`). **Equations are pasted PNG images** (LaTeX/MathType-style serif math, bold vectors), e.g. slide 10: `F_ij(φ,d)=Σ…`, `MI(q;I)≈½log₂det(…)`, and slide 31 top-right.
- Placement: **under the figure, in two side-by-side columns** (left x 0.83, right x 6.14), equation height 0.85 in. Each is followed by 1–2 short definition lines (also images, h 0.38) such as "Shot + read noise: σ²=μ+σ_r²". A takeaway bar sits under them.
- Equations are not boxed. Glyph size matches the ~20 pt body text.
- Simple inline math is typed text (θ_x, φ, ∂I/∂q₁) in Arial or italic with baseline sub/superscripts.
- When restyling, either keep equations as images at this size or use native OMML at 20 pt, unboxed, two-column under the figure. Note that LibreOffice renders OMML blank, so check those slides in PowerPoint.

## 9. Tables
- **Native table** (slides 17, 19): header row fill #316886 with **18 pt bold white** text. Body rows have **no fill and no borders at all**, 18 pt black, centred, row height ≈ 0.43 in, cell margins 0.11/0.05 in. Units go in parentheses in the first column, e.g. "θ_x (μrad)".
- **Shape-built comparison table** (slide 26): a full-width #316886 header band (h 0.67) with a two-level header. Rows are 0.74 in tall with **alternating #F2F2F2 bands** and white. Each row holds a bold method name, a 12 pt citation, a thumbnail image (1.94 × 0.68) and centred numbers. The **last row, "This work", has an #E7E6E6 band with every value in bold #316886**.
- A recurring device is the "ours" result highlighted in bold accent, e.g. the final column "100.0", "2.0×" in bold blue on slide 13.

## 10. Layout grid, margins and whitespace
- **Left/right margin: 0.31 in** (content x from 0.31 to 13.03; the right margin is 0.30). This matches the blue tab width.
- **Top of content: y ≈ 0.97–1.11** (pills at 1.11, just 0.19 below the 0.92 title band). **Bottom of content: y ≈ 6.9.** The footer zone is 7.0–7.42.
- **Two-column grid**: columns at x 0.31 and 6.81, width 6.22, **gutter 0.28**.
- **Three-column grid**: x 0.31 / 4.64 / 8.97, width 4.06, gutter 0.27.
- **Four-up thumbnails**: width 1.97, pitch 2.11.
- Vertical rhythm: pill (0.47) → 0.06–0.14 gap → figure → caption → takeaway. Gaps are small (0.05–0.15 in).
- **Density: high but orderly.** The slide is filled edge to edge in the content area, and big empty areas are rare (slide 9 and slide 30 are the airiest). Whitespace comes from the white background and from short phrases rather than from big margins.
- Typical compositions, in order of frequency:
  1. **Two-column comparison**: [pill A | pill B], full-width observation bar, figures with phrases, a second observation bar, more figures (slides 3–7, 23, 27–29).
  2. **Figure + takeaway**: one or two large figures, then a centred grey takeaway bar at the bottom (10, 20, 22, 24).
  3. **Three-column cards**: pill / image / caption ×3, then a takeaway (21).
  4. **Diagram flow** with arrows and small pills (9, 11, 13, 18).
  5. **Table left + plots right** (17), or full-width table (26).
  6. **Hero title slide** (1).

## 11. Animations and transitions
- **No animations**: there are no `<p:timing>` nodes on any slide. Everything appears at once, and step-by-step reveals are done by repeating slides with the same title (e.g. slides 10–13).
- **Transitions**: only **slide 1 has a slow Fade** (`<p:transition spd="slow"><p:fade/>`). Slides 2–31 have none.

## 12. Speaker notes
- **There are effectively none.** Every slide has a notes page that holds only leftover date/slide-number fields ("1.7.2013", "‹#›") from an old notes master, with no written notes. The language would be English (the deck is all English).
- The style therefore puts the narrative in the **takeaway bars and slide titles**, not in notes. If notes are needed for a restyled deck, keep them short English talking points, since the reference sets no precedent.

## 13. Distinctive taste vs. a generic template
- **One accent colour, #316886, used with discipline**: titles, pills, table headers and emphasised words. It is never used as a large background, and there is no second accent.
- **Bold-blue keyword inside a black sentence** marks the point of each sentence.
- **Grey rounded takeaway bar** with one sentence per slide, which works as the slide's thesis.
- **Blue column pills**, not sub-titles or bullet headings.
- **Figure-first and bullet-free**: phrases, arrows ("→", "↑") and diagrams replace bullet lists.
- **Flat and frameless**: no picture borders, shadows or decorative graphics, and near-square corners.
- **Light grey title band + narrow blue tab** at left, instead of a dark header bar or an underline.
- **Small institutional chrome**: group logo + URL bottom-left, grey page tile bottom-right.
- **No animations**, only a fade into the title. Builds are made with duplicate slides.
- Numbers are compared in **tables or tiles with "This work" highlighted** in bold blue.
- Generic templates differ: they use placeholders with bullets at multiple levels, theme fonts, dark or coloured title bars, picture borders and shadows, animations, and section-divider slides. **This deck has none of these.** It also has **no section-divider, agenda or outline slides**.

## 14. Restyle checklist (apply to another deck)
1. 16:9, white background, Calibri everywhere. Do not rely on the theme's Arial.
2. On each content slide add: the band (0,0,13.33×0.92, #F2F2F2 → 64% alpha gradient), the tab (0,0,0.31×0.92, #316886), the title (0.31,0,12.72×0.92, 28 pt bold #316886, left, centred vertically), the footer logo (0.31,7.00,2.71×0.42; reuse `unpacked/ppt/media/image2.png` from the reference), and the page tile (12.57,7.03,0.42×0.40 #F2F2F2) with 16 pt #316886 number.
3. Turn bullet lists into 1–2-line phrases at 20 pt (18 pt for labels), placed under or next to figures.
4. Put a #316886 pill (h 0.47, 20 pt bold white) over each column at y 1.11, using the 2-column (6.22/0.28 gutter) or 3-column (4.06/0.27) grid with 0.31 margins.
5. End most slides with one #E7E6E6 rounded takeaway bar (20 pt, centred, keywords bold #316886) at y ≈ 6.2–6.4, x ≈ 0.97–1.33.
6. Give figures no borders, scale them to the column widths, and let them take ~40–60% of the slide.
7. Put equations as unboxed images or 20 pt OMML in two columns under the figure, with short definition lines.
8. Tables get a #316886 header (18 pt bold white) and borderless body rows. Highlight "this work" in bold #316886 on an #E7E6E6 row.
9. Remove animations and use no transitions (optional slow fade on the title slide only).
10. Title slide: 32 pt bold #316886 centred title, 24 pt centred author block with the name in bold, and a hero schematic strip across the bottom half. It has no band, logo or number.
