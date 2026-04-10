#!/usr/bin/env python3
import json
from tokens import ACCENT_COLORS_TOKENS, COLORS_TOKENS

def build_color_theme(brightness:str, color:str, accent_color_dict:dict) -> dict:
    colors = {
		"editor.background": COLORS_TOKENS['black'],
		"editor.foreground": COLORS_TOKENS['white'],
		"activityBarBadge.background": ACCENT_COLORS_TOKENS[color][brightness]['main-accent'],
		"sideBarTitle.foreground": COLORS_TOKENS['white']
	}

    token_colors = [
		{
			"name": "Comment",
			"scope": [
				"comment",
				"punctuation.definition.comment"
			],
			"settings": {
				"fontStyle": "italic",
				"foreground": ACCENT_COLORS_TOKENS[color][brightness]['main-accent']
			}
		},
    ]

    return {
        '$schema': 'vscode://schemas/color-theme',
        'name': f'fag-${color}-color-theme',
        'type': brightness,
        'colors': colors,
        'tokenColors': token_colors
    }


def build():
    package_json_entry = {
        'contributes': {
            'themes': []
        }
    }

    for color in ACCENT_COLORS_TOKENS:
        for brightness in ('dark', 'light'):
            theme = build_color_theme(brightness, color, ACCENT_COLORS_TOKENS[color])

            file_name = f'fag-{color}-{brightness}-color-theme.json'
            json.dump(theme, open(f'../themes/{file_name}', 'w'), indent=2)

            package_json_entry['contributes']['themes'].append({
                'label': f'FAG-{color} {brightness} color theme',
                'uiTheme': 'vs-dark' if brightness == 'dark' else 'vs',
                'path': f'./themes/{file_name}'
            })

    print('Suggested package.json entry:')
    print(json.dumps(package_json_entry, indent=2)[2:-2])


if __name__=="__main__":
    build()