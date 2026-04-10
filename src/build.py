#!/usr/bin/env python3
import json
from tokens import ACCENT_COLORS_TOKENS, COLORS_TOKENS

def build_color_theme(brightness:str, color:str, accent_color_dict:dict) -> dict:
    colors = {
		"editor.background": COLORS_TOKENS[brightness]['panel-2'],
		"editor.foreground": COLORS_TOKENS['white'],

        "editorLineNumber.foreground": COLORS_TOKENS['unset'],

        "editorGroup.border": COLORS_TOKENS['unset'],
        "editorGroupHeader.tabsBackground": COLORS_TOKENS['unset'],
        "editorGroupHeader.border": COLORS_TOKENS['unset'],
        "editorGroupHeader.tabsBorder": COLORS_TOKENS['unset'],
        
        "editorIndentGuide.activeBackground1": COLORS_TOKENS['unset'],
        "editorIndentGuide.background1": COLORS_TOKENS['unset'],

        "editorRuler.foreground": COLORS_TOKENS['unset'],

        "editorBracketMatch.border": COLORS_TOKENS['unset'],
        "editorBracketMatch.background": COLORS_TOKENS['unset'],

        "sideBar.foreground": COLORS_TOKENS['unset'],
        "sideBar.background": COLORS_TOKENS[brightness]['panel-3'],
        "sideBar.border": COLORS_TOKENS['unset'],
		"sideBarTitle.foreground": COLORS_TOKENS['white'],
        "sideBarSectionHeader.background": COLORS_TOKENS['unset'],
        "sideBarSectionHeader.border": COLORS_TOKENS['unset'],

        "activityBarBadge.background": ACCENT_COLORS_TOKENS[color][brightness]['main-accent'],
		"activityBar.background": COLORS_TOKENS[brightness]['panel-3'],
        "activityBar.border": COLORS_TOKENS['unset'],
        "activityBar.dropBorder": COLORS_TOKENS['unset'],
        "activityBar.activeBorder": COLORS_TOKENS['unset'],
        "activityBar.foreground": COLORS_TOKENS['unset'],

        "scrollbar.shadow": COLORS_TOKENS['transparent'],
        
        "button.background": COLORS_TOKENS['unset'],
        "button.border": COLORS_TOKENS['unset'],
        "button.hoverBackground": COLORS_TOKENS['unset'],

        "statusBar.background": COLORS_TOKENS['unset'],
        "statusBar.noFolderBackground": COLORS_TOKENS['unset'],
        "statusBarItem.remoteBackground": COLORS_TOKENS['unset'],
        "statusBar.foreground": COLORS_TOKENS['unset'],
        "statusBar.noFolderForeground": COLORS_TOKENS['unset'],
        "statusBar.debuggingForeground": COLORS_TOKENS['unset'],
        "statusBarItem.remoteForeground": COLORS_TOKENS['unset'],
        "statusBar.border": COLORS_TOKENS['unset'],

        "titleBar.activeBackground": COLORS_TOKENS['unset'],
        "titleBar.border": COLORS_TOKENS['unset'],

        "panel.background": COLORS_TOKENS['unset'],

        "panelSectionHeader.background": COLORS_TOKENS['unset'],
        "panelSectionHeader.border": COLORS_TOKENS['unset'],

        "tab.activeBackground": COLORS_TOKENS['unset'],
        "tab.inactiveBackground": COLORS_TOKENS['unset'],
        "tab.hoverBackground": COLORS_TOKENS['unset'],
        "tab.activeForeground": COLORS_TOKENS['unset'],
        "tab.inactiveForeground": COLORS_TOKENS['unset'],
        "tab.border": COLORS_TOKENS['unset'],
        "tab.activeBorder": ACCENT_COLORS_TOKENS[color][brightness]['main-accent'],

        "breadcrumb.background": COLORS_TOKENS['unset'],
    
        "widget.shadow": COLORS_TOKENS['transparent-1'],

        "window.activeBorder": COLORS_TOKENS['unset'],

        "focusBorder": COLORS_TOKENS['unset'],

        "list.activeSelectionBackground": COLORS_TOKENS['unset'],
        "list.hoverBackground": COLORS_TOKENS['unset'],
        "list.filterMatchBorder": COLORS_TOKENS['unset'],
        "list.highlightForeground": COLORS_TOKENS['unset'],
        "list.activeSelectionForeground": COLORS_TOKENS['unset'],
        "list.activeSelectionIconForeground": COLORS_TOKENS['unset'],
        "list.focusHighlightForeground": COLORS_TOKENS['unset'],
        "list.inactiveSelectionBackground": COLORS_TOKENS['unset'],

        "panel.border": COLORS_TOKENS['unset'],

        "input.background": COLORS_TOKENS['unset'],

        "commandCenter.background": COLORS_TOKENS['unset'],
        "commandCenter.border": COLORS_TOKENS['unset'],

        "panelTitle.activeBorder": COLORS_TOKENS['unset'],
        "panelTitle.activeForeground": COLORS_TOKENS['unset'],

        "tree.indentGuidesStroke": COLORS_TOKENS['unset'],

        "editorGutter.addedBackground": "#1F7F56",
        "editorGutter.deletedBackground": "#A51D2D",
        "editorGutter.modifiedBackground": "#1A5FB4",

        "gitDecoration.addedResourceForeground": "#8FF0A4dd",
        "gitDecoration.renamedResourceForeground": "#8FF0A4dd",
        "gitDecoration.untrackedResourceForeground": "#8FF0A4dd",
        "gitDecoration.modifiedResourceForeground": "#FFBE6Fdd",
        "gitDecoration.stageModifiedResourceForeground": "#FFBE6Fdd",
        "gitDecoration.deletedResourceForeground": "#F66151dd",
        "gitDecoration.stageDeletedResourceForeground": "#F66151dd",
        "gitDecoration.ignoredResourceForeground": "#77767B",
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