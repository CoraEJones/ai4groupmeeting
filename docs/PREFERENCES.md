# Group-meeting deck preferences (Yiyu)

Authoritative list of how Yiyu wants group-meeting (组会) decks made. Chat in Chinese; slides in English.

## Content
- Group meetings are progress reports on Yiyu's own research.
- Slides hold only **formulas, figures and key conclusions**. All explanation goes into the speaker notes.
- Speaker notes: a **Chinese spoken script, about 300 characters per slide**, explaining every formula and every figure panel.
- **Every number must come from a verified source** (simulation/training results or Yiyu's files). Unsourced or hard-coded numbers are dropped.
- Never put tags like "derived, not simulated" on a slide. Anything not yet simulated must be simulated first, then go in.
- Citation format: `Author et al., Venue, pages (year)`, e.g. `Wu et al., ICCP, 1–12 (2019)`, `Levin et al., ACM Trans. Graph., 26, 70-es (2007)`.

## Typography and math
- Every font size is a **whole number and ≥ 18 pt** (slides and figure labels alike).
- Calibri everywhere. No bullets: short phrases, with **bold #316886 keywords inside black text**.
- **All math, display and inline** (symbols, variables, `w ≈ 166 µm`, `θ_j`, `λ/p`, values with units in labels and captions) is **native PowerPoint equation-editor OMML**, never plain text or images.

## Visual style (details in STYLE_GUIDE.md)
- 16:9 white. Light-grey title band (#F2F2F2) with a #316886 left tab; title Calibri 28 pt bold #316886, short claim in sentence case.
- Group logo bottom-left, grey page-number tile bottom-right.
- #316886 is the single accent; greys #E7E6E6 / #F2F2F2.
- Rounded blue column-header pills with white bold text; one grey rounded takeaway bar per slide with bold-blue key words.
- No animations on shapes, no decorative imagery, no "Thank you" slide.

## Figures
- Principle / optics figures are **animated GIFs**, not static diagrams (e.g. emitters firing one by one to show position→angle mapping; a scan over the zoomed phase plate; spot evolution vs depth).
- Figures are all-English, labels ≥ 18 pt **at their placed size**. If a supplied figure would shrink labels below 18 pt, redraw it from the data at the placed size and move titles/legends onto the slide as native shapes.
- Bar charts: say where an axis does not start at 0 (e.g. PSNR from 28 dB); draw target lines (e.g. 3 cm, 10%) when there is a target.

## Workflow
1. Agree a storyboard (slide-by-slide outline) before building.
2. Build group by group; render previews (LibreOffice → JPG) and check every slide visually.
3. New or changed slides go out first as a **standalone .pptx**; merge into the full deck only after approval.
4. Slides Yiyu hand-edited are kept **verbatim** when asked, even if off-style.
5. Image-only requests: deliver just the PNG, don't touch the deck.
6. Files over 25 MB can't go through chat; copy to Yiyu's desktop instead.
7. LibreOffice previews show OMML fallback images (small fractions, odd spacing); judge equations in PowerPoint.
