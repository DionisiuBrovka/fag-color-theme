# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build

```bash
npm run build:color-themes   # runs: cd src && python build.py
```

This regenerates all JSON theme files in `themes/` and prints a suggested `package.json` `contributes.themes` snippet to stdout. Always run after editing `src/tokens.py` or `src/build.py`.

## Architecture

The project is a VS Code color theme extension that supports 7 accent colors × 2 brightness levels = 14 themes. Everything is generated — the JSON files in `themes/` are build artifacts, not edited by hand.

### Source files (`src/`)

- **`tokens.py`** — the single source of truth for all color values. Two exports:
  - `COLORS_TOKENS` (`CT`) — base palette (named Adwaita/GNOME colors), plus `dark` and `light` sub-dicts each containing `panel-N`, `foreground-N`, `border-N`, and `hover-N` scales.
  - `ACCENT_COLORS_TOKENS` (`ACT`) — one entry per accent (defualt, green, yellow, orange, red, purple, brown). Each is built with `_accent()` and contains `main-accent`, `accent-transparent-N`, `accent-hover-N`, and nested `dark`/`light` sub-dicts with `accent-up-N` / `accent-down-N` tints.

- **`build.py`** — iterates every `(color, brightness)` pair, calls `build_color_theme()`, and writes `themes/fag-{color}-{brightness}-color-theme.json`. The `build_color_theme()` function assembles the full VS Code color-theme dict by referencing `CT` and `ACT` tokens. Unimplemented keys are left commented out; `UNSET = CT['unset']` (magenta `#ff00ff`) marks intentionally unstyled keys so they're easy to spot.

### Token lookup pattern

Inside `build_color_theme(brightness, color, accent_color_dict)`:

| What you need | Expression |
|---|---|
| Brightness-independent palette color | `CT['pallete-blue-3']` |
| Brightness-specific panel/foreground/border | `CT[brightness]['panel-2']` |
| Accent main color | `ACT[color]['main-accent']` |
| Accent at opacity | `ACT[color]['accent-transparent-2']` |
| Accent tint for current brightness | `ACT[color][brightness]['accent-up-1']` |

### Adding a new accent color

1. Add an entry to `ACCENT_COLORS_TOKENS` in `tokens.py` using `_accent()`.
2. Add the new theme labels to `package.json` `contributes.themes` (or let the build script print the updated snippet and paste it in).
3. Run the build.

### Unset keys

`CT['unset']` is `#ff00ff` (magenta). If a VS Code color key appears as magenta in the editor, that token is intentionally not styled yet. To style it, uncomment the line in `build.py` and assign a real token reference.

## Docs and assets

- **`README.md`** / **`README.ru.md`** — English and Russian documentation. Both contain image placeholders (commented out) pointing to `images/`.
- **`ROADMAP.md`** — planned and in-progress work. Update this alongside feature work.
- **`images/`** — logo and screenshots. Filenames expected by the READMEs: `logo.png`, `screenshot-dark.png`, `screenshot-light.png`, `screenshot-accents.png`.
