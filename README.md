# ai4groupmeeting

Long-term memory for AI-assisted group-meeting decks.

- `docs/PREFERENCES.md` – the user's rules and workflow (authoritative).
- `docs/STYLE_GUIDE.md` – measured visual spec of the group's reference deck.
- `skills/group-meeting-deck/SKILL.md` – the reusable build recipe.
- `tools/` – helper scripts: `omml_lib.py` (native PowerPoint equations from LaTeX-like input, with fallback images), `g_lib.py` (slide chrome, styled text runs, image placement), `prev.py` (render helper). Paths at the top of each file point to a local working folder; change `W` before use.
