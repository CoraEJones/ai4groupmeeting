---
name: Group-meeting research deck
description: Build or edit an English research group-meeting (组会) PowerPoint deck in the Meta-Optics @ Tsinghua style, with OMML math, ≥18 pt whole-number fonts, GIF principle figures and Chinese speaker-note scripts.
---
# Steps
1. Read `docs/PREFERENCES.md` and `docs/STYLE_GUIDE.md`. They override any default deck style.
2. Collect sources: the user's previous decks/modules, results and figures from the simulation side. List every number you plan to show with its source; drop any number without one. If a claim needs a simulation that hasn't been run, request it before building.
3. Write a storyboard (one line per slide: title claim, figure, formula, takeaway) and get it approved.
4. Build in groups of 3–6 slides with python-pptx + raw XML:
   - chrome per slide (title band, #316886 tab, logo, page tile) as in STYLE_GUIDE §3;
   - all math via `tools/omml_lib.py` (native OMML with fallback PNG), including inline values with units;
   - figures redrawn at their placed size so every label is ≥18 pt; principle figures as animated GIFs;
   - speaker notes: ~300-character Chinese script per slide covering every formula and panel.
5. Render each group (`soffice --headless --convert-to pdf`, then `pdftoppm`) and inspect every slide: overflow, overlaps, font sizes (whole numbers ≥18), no bullets, no plain-text math.
6. Deliver new/changed slides as a standalone file first; merge into the full deck after approval, then renumber pages and update the agenda ranges.
7. Keep any slide the user hand-edited verbatim when asked.
