"""
Color tokens for the VS Code theme generator.

COLORS_TOKENS  – base palette, panels, borders, and foreground shades.
ACCENT_COLORS_TOKENS – per-accent-color overrides (each generates its own theme).

Naming conventions
──────────────────
  panel-N      : background layers, 1 = deepest, 5 = most elevated
  foreground-N : text layers, 1 = dimmest, 5 = brightest
  border-N     : border layers, 1 = subtlest
  accent-up-N  : lighter tints of the accent (for hovers, highlights)
  accent-down-N: darker shades of the accent (for pressed states, shadows)
  accent-transparent-N : accent at increasing opacity (1 = most transparent)
"""

# ─── Base palette ───────────────────────────────────────────────────────────

COLORS_TOKENS = {
    # Special values
    "unset": "#ff00ff",  # magenta — easy to spot unstyled keys
    "black": "#000000",
    "white": "#FFFFFF",

    # Palette — blue
    "pallete-blue-1": "#99c1f1",
    "pallete-blue-2": "#62a0ea",
    "pallete-blue-3": "#3584e4",
    "pallete-blue-4": "#1c71d8",
    "pallete-blue-5": "#1a5fb4",

    # Palette — green
    "pallete-green-1": "#8ff0a4",
    "pallete-green-2": "#57e389",
    "pallete-green-3": "#33d17a",
    "pallete-green-4": "#2ec27e",
    "pallete-green-5": "#26a269",

    # Palette — yellow
    "pallete-yellow-1": "#f9f06b",
    "pallete-yellow-2": "#f8e45c",
    "pallete-yellow-3": "#f6d32d",
    "pallete-yellow-4": "#f5c211",
    "pallete-yellow-5": "#e5a50a",

    # Palette — orange
    "pallete-orange-1": "#ffbe6f",
    "pallete-orange-2": "#ffa348",
    "pallete-orange-3": "#ff7800",
    "pallete-orange-4": "#e66100",
    "pallete-orange-5": "#c64600",

    # Palette — red
    "pallete-red-1": "#f66151",
    "pallete-red-2": "#ed333b",
    "pallete-red-3": "#e01b24",
    "pallete-red-4": "#c01c28",
    "pallete-red-5": "#a51d2d",

    # Palette — purple
    "pallete-purple-1": "#dc8add",
    "pallete-purple-2": "#c061cb",
    "pallete-purple-3": "#9141ac",
    "pallete-purple-4": "#813d9c",
    "pallete-purple-5": "#613583",

    # Palette — brown
    "pallete-brown-1": "#cdab8f",
    "pallete-brown-2": "#b5835a",
    "pallete-brown-3": "#986a44",
    "pallete-brown-4": "#865e3c",
    "pallete-brown-5": "#63452c",

    # Palette — light neutrals
    "pallete-light-1": "#ffffff",
    "pallete-light-2": "#f6f5f4",
    "pallete-light-3": "#deddda",
    "pallete-light-4": "#c0bfbc",
    "pallete-light-5": "#9a9996",

    # Palette — dark neutrals
    "pallete-dark-1": "#9a9996",
    "pallete-dark-2": "#5e5c64",
    "pallete-dark-3": "#3d3846",
    "pallete-dark-4": "#241f31",
    "pallete-dark-5": "#000000",

    # Transparency helpers
    "transparent":   "#00000000",
    "transparent-1": "#00000033",  # ~20 %
    "transparent-2": "#00000066",  # ~40 %
    "transparent-3": "#00000099",  # ~60 %

    # Terminal
    "terminal-background": "#0f0f0f",

    # ── Dark brightness variant ─────────────────────────────────────────
    "dark": {
        # Background panels (deepest → most elevated)
        "panel-1": "#0f0f0f",
        "panel-2": "#1c1c1f",
        "panel-3": "#222226",
        "panel-4": "#2e2e32",
        "panel-5": "#424246",

        # Borders
        "no-border": "#00000000",
        "border-1": "#2e2e32",
        "border-2": "#424246",
        "border-3": "#5e5c64",

        # Semi-transparent hover overlays (light-on-dark)
        "hover-1": "#ffffff08",  # ~3 %  — subtle list hover
        "hover-2": "#ffffff0f",  # ~6 %  — list hover
        "hover-3": "#ffffff1a",  # ~10 % — button / tab hover
        "hover-4": "#ffffff26",  # ~15 % — active / pressed
        "hover-5": "#ffffff33",  # ~20 % — drag-drop overlay

        # Foreground (dimmest → brightest)
        "foreground-1": "#5e5c64",
        "foreground-2": "#9a9996",
        "foreground-3": "#c0bfbc",
        "foreground-4": "#deddda",
        "foreground-5": "#ffffff",
    },

    # ── Light brightness variant ────────────────────────────────────────
    "light": {
        # Background panels (deepest → most elevated)
        "panel-1": "#c0bfbc",
        "panel-2": "#deddda",
        "panel-3": "#eeeded",
        "panel-4": "#f6f5f4",
        "panel-5": "#ffffff",

        # Borders
        "no-border": "#00000000",
        "border-1": "#deddda",
        "border-2": "#c0bfbc",
        "border-3": "#9a9996",

        # Semi-transparent hover overlays (dark-on-light)
        "hover-1": "#00000008",  # ~3 %  — subtle list hover
        "hover-2": "#0000000f",  # ~6 %  — list hover
        "hover-3": "#0000001a",  # ~10 % — button / tab hover
        "hover-4": "#00000026",  # ~15 % — active / pressed
        "hover-5": "#00000033",  # ~20 % — drag-drop overlay

        # Foreground (dimmest → brightest)
        "foreground-1": "#c0bfbc",
        "foreground-2": "#9a9996",
        "foreground-3": "#5e5c64",
        "foreground-4": "#3d3846",
        "foreground-5": "#241f31",
    },
}


# ─── Helper to build a consistent accent entry ─────────────────────────────

def _accent(
    main: str,
    dark_up: tuple[str, str, str],
    dark_down: tuple[str, str, str],
    light_up: tuple[str, str, str],
    light_down: tuple[str, str, str],
) -> dict:
    """
    Build one accent-color dict with a uniform structure.

    This avoids copy-paste drift between accent entries.
    """
    return {
        "main-accent": main,

        # Accent at increasing opacity levels
        "accent-transparent-1": f"{main}22",
        "accent-transparent-2": f"{main}55",
        "accent-transparent-3": f"{main}aa",
        "accent-transparent-4": f"{main}ee",

        # Accent hover overlays (for selection, highlight backgrounds)
        "accent-hover-1": f"{main}0f",   # ~6 %  — subtle highlight
        "accent-hover-2": f"{main}1a",   # ~10 % — list selection bg
        "accent-hover-3": f"{main}33",   # ~20 % — active selection bg
        "accent-hover-4": f"{main}4d",   # ~30 % — strong highlight

        "dark": {
            "accent-up-1": dark_up[0],
            "accent-up-2": dark_up[1],
            "accent-up-3": dark_up[2],
            "accent-down-1": dark_down[0],
            "accent-down-2": dark_down[1],
            "accent-down-3": dark_down[2],
        },

        "light": {
            "accent-up-1": light_up[0],
            "accent-up-2": light_up[1],
            "accent-up-3": light_up[2],
            "accent-down-1": light_down[0],
            "accent-down-2": light_down[1],
            "accent-down-3": light_down[2],
        },
    }


# ─── Accent color definitions ──────────────────────────────────────────────

ACCENT_COLORS_TOKENS = {
    "defualt": _accent(
        main="#3584e4",
        dark_up=("#4a92e8", "#6aa3ec", "#8fbaf2"),
        dark_down=("#2b6ec0", "#245da3", "#1a5fb4"),
        light_up=("#4a92e8", "#6aa3ec", "#8fbaf2"),
        light_down=("#2b6ec0", "#245da3", "#1a5fb4"),
    ),

    "green": _accent(
        main="#33d17a",
        dark_up=("#44d183", "#57de92", "#77e7a8"),
        dark_down=("#2ec27e", "#26a269", "#1f8c5a"),
        light_up=("#44d183", "#57de92", "#77e7a8"),
        light_down=("#2ec27e", "#26a269", "#1f8c5a"),
    ),

    "yellow": _accent(
        main="#f6d32d",
        dark_up=("#f7d944", "#f8e060", "#fae88a"),
        dark_down=("#e5a50a", "#d09508", "#b88207"),
        light_up=("#f7d944", "#f8e060", "#fae88a"),
        light_down=("#e5a50a", "#d09508", "#b88207"),
    ),

    "orange": _accent(
        main="#ff7800",
        dark_up=("#ff8c26", "#ffa04d", "#ffb87a"),
        dark_down=("#e66100", "#c64600", "#a33a00"),
        light_up=("#ff8c26", "#ffa04d", "#ffb87a"),
        light_down=("#e66100", "#c64600", "#a33a00"),
    ),

    "red": _accent(
        main="#e01b24",
        dark_up=("#e83a42", "#ed5a60", "#f28084"),
        dark_down=("#c01c28", "#a51d2d", "#8b1a26"),
        light_up=("#e83a42", "#ed5a60", "#f28084"),
        light_down=("#c01c28", "#a51d2d", "#8b1a26"),
    ),

    "purple": _accent(
        main="#9141ac",
        dark_up=("#a155b8", "#b06dc4", "#c48dd4"),
        dark_down=("#813d9c", "#613583", "#4e2a6a"),
        light_up=("#a155b8", "#b06dc4", "#c48dd4"),
        light_down=("#813d9c", "#613583", "#4e2a6a"),
    ),

    "brown": _accent(
        main="#986a44",
        dark_up=("#a57a56", "#b38d6c", "#c4a488"),
        dark_down=("#865e3c", "#63452c", "#4d3521"),
        light_up=("#a57a56", "#b38d6c", "#c4a488"),
        light_down=("#865e3c", "#63452c", "#4d3521"),
    ),
}
