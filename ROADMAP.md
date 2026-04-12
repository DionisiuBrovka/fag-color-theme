# Roadmap

## In Progress


## Fixes & Polish

- [ ] Fix light themes — color issues
- [ ] Fix input elements (radio buttons, text fields) — they blend into the background due to wrong color tokens
- [ ] Add syntax highlighting token rules to `build.py` (currently only UI colors are defined)
- [ ] Lower minimum VS Code engine version in `package.json` for VSCodium compatibility (currently `^1.115.0`; find the VSCodium base version and adjust accordingly)

## Planned

### Icon Theme
- [ ] Design and implement a custom VS Code icon theme

### Custom UI Elements
- [ ] Style scrollbars and other UI elements via [vscode-custom-ui-style](https://github.com/subframe7536/vscode-custom-ui-style)

### Publication
- [ ] Prepare and publish to VS Code Marketplace
- [ ] Add logo and screenshots to repository
- [ ] Finalize version and changelog

## Done

- [x] Basic theme structure (14 themes: 7 accents × dark/light)
- [x] Color token system (`tokens.py` + `build.py`)
- [x] README (EN + RU)
