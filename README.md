# NC Septic Inspector website (ncsepticinspector.com)

Septic-only sister site of Inspect-All Home Inspections (inspectallnc.com). Static site; Netlify project `nc-septic-inspector` publishes this repository as-is on every push to `main`.

Sources (edit these, never the built pages):
- `_home.html`, `_template.html`, `_contact.html`, `_icons.html`, `_404.html`, `_thanks.html`
- `.claude/site.json` (business facts, towns, page order), `.claude/reviews.json`, `.claude/photos.json`
- `.claude/pages-src/<page>.main.html` + `<page>.meta.json` (one pair per content page)
- `.claude/tools/make-town-pages.py` writes the 11 town-page pairs from its TOWNS data

Build: `node .claude/build.js` (regenerate town pages first with `python3 .claude/tools/make-town-pages.py` if their data changed). The build refuses to finish while its PROBLEMS list is non-empty.
