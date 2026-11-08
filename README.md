# Estúdio

Two tools on one page, switched from the top bar:

- **Colchetes**: animated words framed by brackets, exported as GIF, video or PNG
- **Chart Atelier**: charts in the deck's visual language (columns, capsules, pills, donut, pie, gauge, line, big number), exported as PNG

`index.html` is the finished page, served by GitHub Pages (Settings → Pages → Deploy from branch `main`, folder `/`).

Shortcuts: Alt + 1–2 switches tools; `#colchetes` and `#graficos` link straight to one.

## Editing

Each tool's source lives in `src/` (`colchetes.html`, `graficos.html`, plus `shell.html` for the top bar). After changing one, run `python3 build.py` to regenerate `index.html`.
