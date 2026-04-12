# Contributing

Thanks for your interest in contributing to FAG-theme!

## How to contribute

### Reporting bugs

Open an issue on [GitHub Issues](https://github.com/DionisiuBrovka/fag-color-theme/issues) and describe:
- What looks wrong and in which theme variant (e.g. "FAG-default dark")
- A screenshot if possible
- The language or UI element affected

### Suggesting improvements

Open an issue with the `enhancement` label. Describe what you'd like to change and why.

### Making changes

1. Fork the repository
2. Edit `src/tokens.py` or `src/build.py` — **do not edit files in `themes/` directly**, they are generated
3. Run the build to regenerate theme files:
   ```bash
   npm run build:color-themes
   ```
4. Open a pull request with a clear description of what changed

## Project structure

- `src/tokens.py` — all color values (single source of truth)
- `src/build.py` — generates the 14 JSON theme files
- `themes/` — generated output, do not edit by hand
