#!/usr/bin/env python3
"""
VS Code color theme generator.

Builds JSON theme files for each accent color × brightness combination
and prints a suggested package.json 'contributes.themes' entry.
"""

import json
import os
from pathlib import Path
from tokens import COLORS_TOKENS as CT
from tokens import ACCENT_COLORS_TOKENS as ACT

# Sentinel value for keys that have not been styled yet.
# Replace CT['unset'] entries with real values as you design the theme.
UNSET = CT['unset']


def build_color_theme(brightness: str, color: str, accent_color_dict: dict) -> dict:
    """
    Assemble a complete VS Code color-theme dict.

    Parameters
    ----------
    brightness : str
        Either 'dark' or 'light'.
    color : str
        Accent color key present in ACCENT_COLORS_TOKENS.
    accent_color_dict : dict
        The sub-dict ACT[color] for convenience.

    Returns
    -------
    dict
        A full color-theme object ready to be serialised as JSON.
    """

    colors = {
        # ── Contrast colors ─────────────────────────────────────────────
        # "contrastActiveBorder": UNSET,
        # "contrastBorder": UNSET,

        # ── Base colors ─────────────────────────────────────────────────
        "focusBorder": ACT[color]['accent-transparent-2'],
        "foreground": CT[brightness]['foreground-3'],
        "disabledForeground": CT[brightness]['foreground-2'],
        "widget.border": CT[brightness]['no-border'],
        "widget.shadow": CT['transparent'],
        "selection.background": ACT[color]['accent-transparent-2'],
        "descriptionForeground": CT[brightness]['foreground-1'],
        "errorForeground": CT['pallete-red-2'],
        "icon.foreground": CT[brightness]['foreground-4'],
        "sash.hoverBorder": CT[brightness]['no-border'],

        # ── Window border ───────────────────────────────────────────────
        "window.activeBorder": ACT[color]['main-accent'],
        "window.inactiveBorder": CT[brightness]['no-border'],

        # ── Text colors ─────────────────────────────────────────────────
        "textBlockQuote.background": CT['transparent'],
        "textBlockQuote.border": CT[brightness]['no-border'],
        "textCodeBlock.background": CT['terminal-background'],
        "textLink.activeForeground": ACT[color][brightness]['accent-up-3'],
        "textLink.foreground": ACT[color]['accent-transparent-4'],
        "textPreformat.foreground": CT['pallete-dark-4'],
        "textPreformat.background": ACT[color][brightness]['accent-up-1'],
        "textPreformat.border": CT[brightness]['no-border'],
        "textSeparator.foreground": CT[brightness]['foreground-4'],

        # ── Action colors ───────────────────────────────────────────────
        # "toolbar.hoverBackground": UNSET,
        # "toolbar.hoverOutline": UNSET,
        # "toolbar.activeBackground": UNSET,
        # "editorActionList.background": UNSET,
        # "editorActionList.foreground": UNSET,
        # "editorActionList.focusForeground": UNSET,
        # "editorActionList.focusBackground": UNSET,

        # ── Button control ──────────────────────────────────────────────
        "button.background": ACT[color][brightness]['accent-down-1'],
        "button.foreground": CT[brightness]['foreground-5'],
        "button.border": CT[brightness]['no-border'],
        # "button.separator": UNSET,
        # "button.hoverBackground": UNSET,
        # "button.secondaryForeground": UNSET,
        # "button.secondaryBackground": UNSET,
        # "button.secondaryHoverBackground": UNSET,
        # "button.secondaryBorder": UNSET,
        "checkbox.background": CT[brightness]['panel-2'],
        # "checkbox.foreground": UNSET,
        # "checkbox.disabled.background": UNSET,
        # "checkbox.disabled.foreground": UNSET,
        # "checkbox.border": UNSET,
        "checkbox.selectBackground": CT[brightness]['panel-2'],
        # "checkbox.selectBorder": UNSET,
        # "radio.activeForeground": UNSET,
        "radio.activeBackground": CT[brightness]['panel-2'],
        # "radio.activeBorder": UNSET,
        # "radio.inactiveForeground": UNSET,
        "radio.inactiveBackground": CT[brightness]['panel-2'],
        # "radio.inactiveBorder": UNSET,
        # "radio.inactiveHoverBackground": UNSET,

        # ── Dropdown control ────────────────────────────────────────────
        "dropdown.background": CT[brightness]['panel-2'],
        "dropdown.listBackground": CT[brightness]['panel-2'],
        # "dropdown.border": UNSET,
        # "dropdown.foreground": UNSET,

        # ── Input control ───────────────────────────────────────────────
        "input.background": CT[brightness]['panel-2'],
        "input.border": CT[brightness]['no-border'],
        # "input.foreground": UNSET,
        # "input.placeholderForeground": UNSET,
        # "inputOption.activeBackground": UNSET,
        # "inputOption.activeBorder": UNSET,
        # "inputOption.activeForeground": UNSET,
        # "inputOption.hoverBackground": UNSET,
        # "inputValidation.errorBackground": UNSET,
        # "inputValidation.errorForeground": UNSET,
        # "inputValidation.errorBorder": UNSET,
        # "inputValidation.infoBackground": UNSET,
        # "inputValidation.infoForeground": UNSET,
        # "inputValidation.infoBorder": UNSET,
        # "inputValidation.warningBackground": UNSET,
        # "inputValidation.warningForeground": UNSET,
        # "inputValidation.warningBorder": UNSET,

        # ── Scrollbar control ───────────────────────────────────────────
        "scrollbar.background": CT['transparent'],
        "scrollbar.shadow": CT['transparent'],
        "scrollbarSlider.activeBackground": CT[brightness]['border-2'],
        "scrollbarSlider.background": CT[brightness]['border-1'],
        "scrollbarSlider.hoverBackground": CT[brightness]['border-2'],

        # ── Badge ───────────────────────────────────────────────────────
        "badge.foreground": CT['pallete-dark-4'],
        "badge.background": ACT[color][brightness]['accent-down-2'],

        # ── Progress bar ────────────────────────────────────────────────
        "progressBar.background": ACT[color]['main-accent'],

        # # ── Lists and trees ─────────────────────────────────────────────
        "list.activeSelectionBackground": CT[brightness]['hover-4'],
        # "list.activeSelectionForeground": UNSET,
        # "list.activeSelectionIconForeground": UNSET,
        "list.dropBackground": ACT[color]['accent-transparent-2'],      
        # "list.focusBackground": UNSET,
        # "list.focusForeground": UNSET,
        # "list.focusHighlightForeground": UNSET,
        "list.focusOutline": CT['transparent'],
        # "list.focusAndSelectionOutline": UNSET,
        # "list.highlightForeground": UNSET,
        # "list.hoverBackground": UNSET,
        # "list.hoverForeground": UNSET,
        # "list.inactiveSelectionBackground": UNSET,
        # "list.inactiveSelectionForeground": UNSET,
        # "list.inactiveSelectionIconForeground": UNSET,
        # "list.inactiveFocusBackground": UNSET,
        # "list.inactiveFocusOutline": UNSET,
        # "list.invalidItemForeground": UNSET,
        # "list.errorForeground": UNSET,
        # "list.warningForeground": UNSET,
        # "listFilterWidget.background": UNSET,
        # "listFilterWidget.outline": UNSET,
        # "listFilterWidget.noMatchesOutline": UNSET,
        # "listFilterWidget.shadow": UNSET,
        # "list.filterMatchBackground": UNSET,
        # "list.filterMatchBorder": UNSET,
        # "list.deemphasizedForeground": UNSET,
        # "list.dropBetweenBackground": UNSET,
        # "tree.indentGuidesStroke": UNSET,
        # "tree.inactiveIndentGuidesStroke": UNSET,
        # "tree.tableColumnsBorder": UNSET,
        # "tree.tableOddRowsBackground": UNSET,

        # # ── Activity Bar ────────────────────────────────────────────────
        "activityBar.background": CT[brightness]['panel-3'],
        # "activityBar.dropBorder": UNSET,
        # "activityBar.foreground": UNSET,
        # "activityBar.inactiveForeground": UNSET,
        # "activityBar.border": UNSET,
        "activityBarBadge.background": ACT[color][brightness]['accent-down-3'],
        # "activityBarBadge.foreground": UNSET,
        # "activityBar.activeBorder": UNSET,
        # "activityBar.activeBackground": UNSET,
        # "activityBar.activeFocusBorder": UNSET,
        # "activityBarTop.foreground": UNSET,
        # "activityBarTop.activeBorder": UNSET,
        # "activityBarTop.inactiveForeground": UNSET,
        # "activityBarTop.dropBorder": UNSET,
        # "activityBarTop.background": UNSET,
        # "activityBarTop.activeBackground": UNSET,
        # "activityWarningBadge.foreground": UNSET,
        # "activityWarningBadge.background": UNSET,
        # "activityErrorBadge.foreground": UNSET,
        # "activityErrorBadge.background": UNSET,

        # # ── Profiles ────────────────────────────────────────────────────
        # "profileBadge.background": UNSET,
        # "profileBadge.foreground": UNSET,
        # "profiles.sashBorder": UNSET,

        # # ── Side Bar ────────────────────────────────────────────────────
        "sideBar.background": CT[brightness]['panel-3'],
        # "sideBar.foreground": UNSET,
        # "sideBar.border": UNSET,
        # "sideBar.dropBackground": UNSET,
        "sideBarSectionHeader.background": CT[brightness]['panel-3'],
        # "sideBarSectionHeader.foreground": UNSET,
        # "sideBarSectionHeader.border": UNSET,
        # "sideBarActivityBarTop.border": UNSET,
        "sideBarTitle.foreground": CT[brightness]['foreground-5'],
        # "sideBarTitle.background": UNSET,
        "sideBarTitle.border": CT[brightness]['border-1'],
        # "sideBarStickyScroll.background": UNSET,
        # "sideBarStickyScroll.border": UNSET,
        # "sideBarStickyScroll.shadow": UNSET,

        # # ── Minimap ─────────────────────────────────────────────────────
        # "minimap.findMatchHighlight": UNSET,
        # "minimap.selectionHighlight": UNSET,
        # "minimap.errorHighlight": UNSET,
        # "minimap.warningHighlight": UNSET,
        # "minimap.background": UNSET,
        # "minimap.selectionOccurrenceHighlight": UNSET,
        # "minimap.foregroundOpacity": UNSET,
        # "minimap.infoHighlight": UNSET,
        # "minimap.chatEditHighlight": UNSET,
        # "minimapSlider.background": UNSET,
        # "minimapSlider.hoverBackground": UNSET,
        # "minimapSlider.activeBackground": UNSET,
        # "minimapGutter.addedBackground": UNSET,
        # "minimapGutter.modifiedBackground": UNSET,
        # "minimapGutter.deletedBackground": UNSET,
        # "editorMinimap.inlineChatInserted": UNSET,

        # # ── Editor Groups & Tabs ────────────────────────────────────────
        # "editorGroup.border": UNSET,
        # "editorGroup.dropBackground": UNSET,
        # "editorGroupHeader.noTabsBackground": UNSET,
        "editorGroupHeader.tabsBackground": CT[brightness]['panel-2'],
        # "editorGroupHeader.tabsBorder": UNSET,
        # "editorGroupHeader.border": UNSET,
        # "editorGroup.emptyBackground": UNSET,
        # "editorGroup.focusedEmptyBorder": UNSET,
        # "editorGroup.dropIntoPromptForeground": UNSET,
        # "editorGroup.dropIntoPromptBackground": UNSET,
        # "editorGroup.dropIntoPromptBorder": UNSET,
        "tab.activeBackground": CT[brightness]['panel-2'],
        # "tab.unfocusedActiveBackground": UNSET,
        # "tab.activeForeground": UNSET,
        "tab.border": CT['transparent'],
        # "tab.activeBorder": UNSET,
        # "tab.selectedBorderTop": UNSET,
        # "tab.selectedBackground": UNSET,
        # "tab.selectedForeground": UNSET,
        # "tab.dragAndDropBorder": UNSET,
        # "tab.unfocusedActiveBorder": UNSET,
        # "tab.activeBorderTop": UNSET,
        # "tab.unfocusedActiveBorderTop": UNSET,
        # "tab.lastPinnedBorder": UNSET,
        "tab.inactiveBackground": CT[brightness]['panel-2'],
        # "tab.unfocusedInactiveBackground": UNSET,
        # "tab.inactiveForeground": UNSET,
        # "tab.unfocusedActiveForeground": UNSET,
        # "tab.unfocusedInactiveForeground": UNSET,
        # "tab.hoverBackground": UNSET,
        # "tab.unfocusedHoverBackground": UNSET,
        # "tab.hoverForeground": UNSET,
        # "tab.unfocusedHoverForeground": UNSET,
        # "tab.hoverBorder": UNSET,
        # "tab.unfocusedHoverBorder": UNSET,
        # "tab.activeModifiedBorder": UNSET,
        # "tab.inactiveModifiedBorder": UNSET,
        # "tab.unfocusedActiveModifiedBorder": UNSET,
        # "tab.unfocusedInactiveModifiedBorder": UNSET,
        # "editorPane.background": UNSET,
        # "sideBySideEditor.horizontalBorder": UNSET,
        # "sideBySideEditor.verticalBorder": UNSET,

        # # ── Editor colors ───────────────────────────────────────────────
        "editor.background": CT[brightness]['panel-2'],
        # "editor.foreground": UNSET,
        # "editorLineNumber.foreground": UNSET,
        # "editorLineNumber.activeForeground": UNSET,
        # "editorLineNumber.dimmedForeground": UNSET,
        # "editorCursor.background": UNSET,
        # "editorCursor.foreground": UNSET,
        # "editorMultiCursor.primary.foreground": UNSET,
        # "editorMultiCursor.primary.background": UNSET,
        # "editorMultiCursor.secondary.foreground": UNSET,
        # "editorMultiCursor.secondary.background": UNSET,
        # "editor.placeholder.foreground": UNSET,
        # "editor.compositionBorder": UNSET,

        # # Editor – selection
        "editor.selectionBackground": ACT[color]['accent-transparent-2'],
        # "editor.selectionForeground": UNSET,
        # "editor.inactiveSelectionBackground": UNSET,
        # "editor.selectionHighlightBackground": UNSET,
        # "editor.selectionHighlightBorder": UNSET,

        # # Editor – word highlight
        # "editor.wordHighlightBackground": UNSET,
        # "editor.wordHighlightBorder": UNSET,
        # "editor.wordHighlightStrongBackground": UNSET,
        # "editor.wordHighlightStrongBorder": UNSET,
        # "editor.wordHighlightTextBackground": UNSET,
        # "editor.wordHighlightTextBorder": UNSET,

        # # Editor – find
        # "editor.findMatchBackground": UNSET,
        # "editor.findMatchForeground": UNSET,
        # "editor.findMatchHighlightForeground": UNSET,
        # "editor.findMatchHighlightBackground": UNSET,
        # "editor.findRangeHighlightBackground": UNSET,
        # "editor.findMatchBorder": UNSET,
        # "editor.findMatchHighlightBorder": UNSET,
        # "editor.findRangeHighlightBorder": UNSET,

        # # Editor – search results
        # "search.resultsInfoForeground": UNSET,
        # "searchEditor.findMatchBackground": UNSET,
        # "searchEditor.findMatchBorder": UNSET,
        # "searchEditor.textInputBorder": UNSET,

        # # Editor – hover
        # "editor.hoverHighlightBackground": UNSET,

        # # Editor – line highlight
        # "editor.lineHighlightBackground": UNSET,
        # "editor.inactiveLineHighlightBackground": UNSET,
        # "editor.lineHighlightBorder": UNSET,

        # # Editor – unicode highlight
        # "editorUnicodeHighlight.border": UNSET,
        # "editorUnicodeHighlight.background": UNSET,

        # # Editor – link
        # "editorLink.activeForeground": UNSET,

        # # Editor – range highlight
        # "editor.rangeHighlightBackground": UNSET,
        # "editor.rangeHighlightBorder": UNSET,

        # # Editor – symbol highlight
        # "editor.symbolHighlightBackground": UNSET,
        # "editor.symbolHighlightBorder": UNSET,

        # # Editor – whitespace & indent guides
        # "editorWhitespace.foreground": UNSET,
        # "editorIndentGuide.background": UNSET,
        # "editorIndentGuide.background1": UNSET,
        # "editorIndentGuide.background2": UNSET,
        # "editorIndentGuide.background3": UNSET,
        # "editorIndentGuide.background4": UNSET,
        # "editorIndentGuide.background5": UNSET,
        # "editorIndentGuide.background6": UNSET,
        # "editorIndentGuide.activeBackground": UNSET,
        # "editorIndentGuide.activeBackground1": UNSET,
        # "editorIndentGuide.activeBackground2": UNSET,
        # "editorIndentGuide.activeBackground3": UNSET,
        # "editorIndentGuide.activeBackground4": UNSET,
        # "editorIndentGuide.activeBackground5": UNSET,
        # "editorIndentGuide.activeBackground6": UNSET,

        # # Editor – inlay hints
        # "editorInlayHint.background": UNSET,
        # "editorInlayHint.foreground": UNSET,
        # "editorInlayHint.typeForeground": UNSET,
        # "editorInlayHint.typeBackground": UNSET,
        # "editorInlayHint.parameterForeground": UNSET,
        # "editorInlayHint.parameterBackground": UNSET,

        # # Editor – rulers
        # "editorRuler.foreground": UNSET,
        # "editor.linkedEditingBackground": UNSET,

        # # Editor – CodeLens
        # "editorCodeLens.foreground": UNSET,

        # # Editor – lightbulb
        # "editorLightBulb.foreground": UNSET,
        # "editorLightBulbAutoFix.foreground": UNSET,
        # "editorLightBulbAi.foreground": UNSET,

        # # Editor – bracket match
        # "editorBracketMatch.background": UNSET,
        # "editorBracketMatch.border": UNSET,
        # "editorBracketMatch.foreground": UNSET,

        # # Editor – bracket pair colorization
        # "editorBracketHighlight.foreground1": UNSET,
        # "editorBracketHighlight.foreground2": UNSET,
        # "editorBracketHighlight.foreground3": UNSET,
        # "editorBracketHighlight.foreground4": UNSET,
        # "editorBracketHighlight.foreground5": UNSET,
        # "editorBracketHighlight.foreground6": UNSET,
        # "editorBracketHighlight.unexpectedBracket.foreground": UNSET,

        # # Editor – bracket pair guides
        # "editorBracketPairGuide.activeBackground1": UNSET,
        # "editorBracketPairGuide.activeBackground2": UNSET,
        # "editorBracketPairGuide.activeBackground3": UNSET,
        # "editorBracketPairGuide.activeBackground4": UNSET,
        # "editorBracketPairGuide.activeBackground5": UNSET,
        # "editorBracketPairGuide.activeBackground6": UNSET,
        # "editorBracketPairGuide.background1": UNSET,
        # "editorBracketPairGuide.background2": UNSET,
        # "editorBracketPairGuide.background3": UNSET,
        # "editorBracketPairGuide.background4": UNSET,
        # "editorBracketPairGuide.background5": UNSET,
        # "editorBracketPairGuide.background6": UNSET,

        # # Editor – folding
        # "editor.foldBackground": UNSET,
        # "editor.foldPlaceholderForeground": UNSET,

        # # Editor – overview ruler
        # "editorOverviewRuler.background": UNSET,
        # "editorOverviewRuler.border": UNSET,
        # "editorOverviewRuler.findMatchForeground": UNSET,
        # "editorOverviewRuler.rangeHighlightForeground": UNSET,
        # "editorOverviewRuler.selectionHighlightForeground": UNSET,
        # "editorOverviewRuler.wordHighlightForeground": UNSET,
        # "editorOverviewRuler.wordHighlightStrongForeground": UNSET,
        # "editorOverviewRuler.wordHighlightTextForeground": UNSET,
        # "editorOverviewRuler.modifiedForeground": UNSET,
        # "editorOverviewRuler.addedForeground": UNSET,
        # "editorOverviewRuler.deletedForeground": UNSET,
        # "editorOverviewRuler.errorForeground": UNSET,
        # "editorOverviewRuler.warningForeground": UNSET,
        # "editorOverviewRuler.infoForeground": UNSET,
        # "editorOverviewRuler.bracketMatchForeground": UNSET,
        # "editorOverviewRuler.inlineChatInserted": UNSET,
        # "editorOverviewRuler.inlineChatRemoved": UNSET,
        # "editorOverviewRuler.commentDraftForeground": UNSET,

        # # Editor – errors and warnings
        # "editorError.foreground": UNSET,
        # "editorError.border": UNSET,
        # "editorError.background": UNSET,
        # "editorWarning.foreground": UNSET,
        # "editorWarning.border": UNSET,
        # "editorWarning.background": UNSET,
        # "editorInfo.foreground": UNSET,
        # "editorInfo.border": UNSET,
        # "editorInfo.background": UNSET,
        # "editorHint.foreground": UNSET,
        # "editorHint.border": UNSET,
        # "problemsErrorIcon.foreground": UNSET,
        # "problemsWarningIcon.foreground": UNSET,
        # "problemsInfoIcon.foreground": UNSET,

        # # Editor – unused source code
        # "editorUnnecessaryCode.border": UNSET,
        # "editorUnnecessaryCode.opacity": UNSET,

        # # Editor – gutter
        # "editorGutter.background": UNSET,
        # "editorGutter.modifiedBackground": UNSET,
        # "editorGutter.modifiedSecondaryBackground": UNSET,
        # "editorGutter.addedBackground": UNSET,
        # "editorGutter.addedSecondaryBackground": UNSET,
        # "editorGutter.deletedBackground": UNSET,
        # "editorGutter.deletedSecondaryBackground": UNSET,
        # "editorGutter.commentRangeForeground": UNSET,
        # "editorGutter.commentGlyphForeground": UNSET,
        # "editorGutter.commentUnresolvedGlyphForeground": UNSET,
        # "editorGutter.foldingControlForeground": UNSET,
        # "editorGutter.itemGlyphForeground": UNSET,
        # "editorGutter.itemBackground": UNSET,
        # "editorGutter.commentDraftGlyphForeground": UNSET,

        # # Editor – comments widget
        # "editorCommentsWidget.resolvedBorder": UNSET,
        # "editorCommentsWidget.unresolvedBorder": UNSET,
        # "editorCommentsWidget.rangeBackground": UNSET,
        # "editorCommentsWidget.rangeActiveBackground": UNSET,
        # "editorCommentsWidget.replyInputBackground": UNSET,

        # # Editor – inline edits
        # "inlineEdit.gutterIndicator.primaryBorder": UNSET,
        # "inlineEdit.gutterIndicator.primaryForeground": UNSET,
        # "inlineEdit.gutterIndicator.primaryBackground": UNSET,
        # "inlineEdit.gutterIndicator.secondaryBorder": UNSET,
        # "inlineEdit.gutterIndicator.secondaryForeground": UNSET,
        # "inlineEdit.gutterIndicator.secondaryBackground": UNSET,
        # "inlineEdit.gutterIndicator.successfulBorder": UNSET,
        # "inlineEdit.gutterIndicator.successfulForeground": UNSET,
        # "inlineEdit.gutterIndicator.successfulBackground": UNSET,
        # "inlineEdit.gutterIndicator.background": UNSET,
        # "inlineEdit.originalBackground": UNSET,
        # "inlineEdit.modifiedBackground": UNSET,
        # "inlineEdit.originalChangedLineBackground": UNSET,
        # "inlineEdit.originalChangedTextBackground": UNSET,
        # "inlineEdit.modifiedChangedLineBackground": UNSET,
        # "inlineEdit.modifiedChangedTextBackground": UNSET,
        # "inlineEdit.originalBorder": UNSET,
        # "inlineEdit.modifiedBorder": UNSET,
        # "inlineEdit.tabWillAcceptModifiedBorder": UNSET,
        # "inlineEdit.tabWillAcceptOriginalBorder": UNSET,

        # # ── Diff editor colors ──────────────────────────────────────────
        # "diffEditor.insertedTextBackground": UNSET,
        # "diffEditor.insertedTextBorder": UNSET,
        # "diffEditor.removedTextBackground": UNSET,
        # "diffEditor.removedTextBorder": UNSET,
        # "diffEditor.border": UNSET,
        # "diffEditor.diagonalFill": UNSET,
        # "diffEditor.insertedLineBackground": UNSET,
        # "diffEditor.removedLineBackground": UNSET,
        # "diffEditorGutter.insertedLineBackground": UNSET,
        # "diffEditorGutter.removedLineBackground": UNSET,
        # "diffEditorOverview.insertedForeground": UNSET,
        # "diffEditorOverview.removedForeground": UNSET,
        # "diffEditor.unchangedRegionBackground": UNSET,
        # "diffEditor.unchangedRegionForeground": UNSET,
        # "diffEditor.unchangedRegionShadow": UNSET,
        # "diffEditor.unchangedCodeBackground": UNSET,
        # "diffEditor.move.border": UNSET,
        # "diffEditor.moveActive.border": UNSET,
        # "multiDiffEditor.headerBackground": UNSET,
        # "multiDiffEditor.background": UNSET,
        # "multiDiffEditor.border": UNSET,

        # # ── Chat colors ─────────────────────────────────────────────────
        # "chat.requestBorder": UNSET,
        # "chat.requestBackground": UNSET,
        # "chat.slashCommandBackground": UNSET,
        # "chat.slashCommandForeground": UNSET,
        # "chat.avatarBackground": UNSET,
        # "chat.avatarForeground": UNSET,
        # "chat.editedFileForeground": UNSET,
        # "chat.linesAddedForeground": UNSET,
        # "chat.linesRemovedForeground": UNSET,
        # "chat.requestCodeBorder": UNSET,
        # "chat.requestBubbleBackground": UNSET,
        # "chat.requestBubbleHoverBackground": UNSET,
        # "chat.checkpointSeparator": UNSET,
        # "chat.thinkingShimmer": UNSET,
        # "chatManagement.sashBorder": UNSET,

        # # ── Inline Chat colors ──────────────────────────────────────────
        # "inlineChat.background": UNSET,
        # "inlineChat.foreground": UNSET,
        # "inlineChat.border": UNSET,
        # "inlineChat.shadow": UNSET,
        # "inlineChatInput.border": UNSET,
        # "inlineChatInput.focusBorder": UNSET,
        # "inlineChatInput.placeholderForeground": UNSET,
        # "inlineChatInput.background": UNSET,
        # "inlineChatDiff.inserted": UNSET,
        # "inlineChatDiff.removed": UNSET,

        # # ── Panel Chat colors ───────────────────────────────────────────
        # "interactive.activeCodeBorder": UNSET,
        # "interactive.inactiveCodeBorder": UNSET,

        # # ── Editor widget colors ────────────────────────────────────────
        # "editorWidget.foreground": UNSET,
        # "editorWidget.background": UNSET,
        # "editorWidget.border": UNSET,
        # "editorWidget.resizeBorder": UNSET,
        # "editorSuggestWidget.background": UNSET,
        # "editorSuggestWidget.border": UNSET,
        # "editorSuggestWidget.foreground": UNSET,
        # "editorSuggestWidget.focusHighlightForeground": UNSET,
        # "editorSuggestWidget.highlightForeground": UNSET,
        # "editorSuggestWidget.selectedBackground": UNSET,
        # "editorSuggestWidget.selectedForeground": UNSET,
        # "editorSuggestWidget.selectedIconForeground": UNSET,
        # "editorSuggestWidgetStatus.foreground": UNSET,
        # "editorHoverWidget.foreground": UNSET,
        # "editorHoverWidget.background": UNSET,
        # "editorHoverWidget.border": UNSET,
        # "editorHoverWidget.highlightForeground": UNSET,
        # "editorHoverWidget.statusBarBackground": UNSET,
        # "editorGhostText.border": UNSET,
        # "editorGhostText.background": UNSET,
        # "editorGhostText.foreground": UNSET,
        # "editorStickyScroll.background": UNSET,
        # "editorStickyScroll.border": UNSET,
        # "editorStickyScroll.shadow": UNSET,
        # "editorStickyScrollGutter.background": UNSET,
        # "editorStickyScrollHover.background": UNSET,

        # # Editor widget – debug exception
        # "debugExceptionWidget.background": UNSET,
        # "debugExceptionWidget.border": UNSET,

        # # Editor widget – marker navigation
        # "editorMarkerNavigation.background": UNSET,
        # "editorMarkerNavigationError.background": UNSET,
        # "editorMarkerNavigationWarning.background": UNSET,
        # "editorMarkerNavigationInfo.background": UNSET,
        # "editorMarkerNavigationError.headerBackground": UNSET,
        # "editorMarkerNavigationWarning.headerBackground": UNSET,
        # "editorMarkerNavigationInfo.headerBackground": UNSET,

        # # ── Peek view colors ────────────────────────────────────────────
        # "peekView.border": UNSET,
        # "peekViewEditor.background": UNSET,
        # "peekViewEditorGutter.background": UNSET,
        # "peekViewEditor.matchHighlightBackground": UNSET,
        # "peekViewEditor.matchHighlightBorder": UNSET,
        # "peekViewResult.background": UNSET,
        # "peekViewResult.fileForeground": UNSET,
        # "peekViewResult.lineForeground": UNSET,
        # "peekViewResult.matchHighlightBackground": UNSET,
        # "peekViewResult.selectionBackground": UNSET,
        # "peekViewResult.selectionForeground": UNSET,
        # "peekViewTitle.background": UNSET,
        # "peekViewTitleDescription.foreground": UNSET,
        # "peekViewTitleLabel.foreground": UNSET,
        # "peekViewEditorStickyScroll.background": UNSET,
        # "peekViewEditorStickyScrollGutter.background": UNSET,

        # # ── Merge conflicts colors ──────────────────────────────────────
        # "merge.currentHeaderBackground": UNSET,
        # "merge.currentContentBackground": UNSET,
        # "merge.incomingHeaderBackground": UNSET,
        # "merge.incomingContentBackground": UNSET,
        # "merge.border": UNSET,
        # "merge.commonContentBackground": UNSET,
        # "merge.commonHeaderBackground": UNSET,
        # "editorOverviewRuler.currentContentForeground": UNSET,
        # "editorOverviewRuler.incomingContentForeground": UNSET,
        # "editorOverviewRuler.commonContentForeground": UNSET,
        # "editorOverviewRuler.commentForeground": UNSET,
        # "editorOverviewRuler.commentUnresolvedForeground": UNSET,
        # "mergeEditor.change.background": UNSET,
        # "mergeEditor.change.word.background": UNSET,
        # "mergeEditor.conflict.unhandledUnfocused.border": UNSET,
        # "mergeEditor.conflict.unhandledFocused.border": UNSET,
        # "mergeEditor.conflict.handledUnfocused.border": UNSET,
        # "mergeEditor.conflict.handledFocused.border": UNSET,
        # "mergeEditor.conflict.handled.minimapOverViewRuler": UNSET,
        # "mergeEditor.conflict.unhandled.minimapOverViewRuler": UNSET,
        # "mergeEditor.conflictingLines.background": UNSET,
        # "mergeEditor.changeBase.background": UNSET,
        # "mergeEditor.changeBase.word.background": UNSET,
        # "mergeEditor.conflict.input1.background": UNSET,
        # "mergeEditor.conflict.input2.background": UNSET,

        # # ── Panel colors ────────────────────────────────────────────────
        "panel.background": CT['terminal-background'],
        # "panel.border": UNSET,
        # "panel.dropBorder": UNSET,
        "panelTitle.activeBorder": ACT[color]['main-accent'],
        # "panelTitle.activeForeground": UNSET,
        # "panelTitle.inactiveForeground": UNSET,
        # "panelTitle.border": UNSET,
        # "panelTitleBadge.background": UNSET,
        # "panelTitleBadge.foreground": UNSET,
        # "panelInput.border": UNSET,
        # "panelSection.border": UNSET,
        # "panelSection.dropBackground": UNSET,
        # "panelSectionHeader.background": UNSET,
        # "panelSectionHeader.foreground": UNSET,
        # "panelStickyScroll.background": UNSET,
        # "panelStickyScroll.border": UNSET,
        # "panelStickyScroll.shadow": UNSET,
        # "panelSectionHeader.border": UNSET,
        # "outputView.background": UNSET,
        # "outputViewStickyScroll.background": UNSET,

        # # ── Status Bar colors ───────────────────────────────────────────
        "statusBar.background": CT[brightness]['panel-4'],
        # "statusBar.foreground": UNSET,
        # "statusBar.border": UNSET,
        "statusBar.debuggingBackground": CT[brightness]['panel-4'],
        # "statusBar.debuggingForeground": UNSET,
        # "statusBar.debuggingBorder": UNSET,
        # "statusBar.noFolderForeground": UNSET,
        "statusBar.noFolderBackground": CT[brightness]['panel-4'],
        # "statusBar.noFolderBorder": UNSET,
        "statusBarItem.activeBackground": CT[brightness]['panel-4'],
        # "statusBarItem.hoverForeground": UNSET,
        # "statusBarItem.hoverBackground": UNSET,
        # "statusBarItem.prominentForeground": UNSET,
        # "statusBarItem.prominentBackground": UNSET,
        # "statusBarItem.prominentHoverForeground": UNSET,
        # "statusBarItem.prominentHoverBackground": UNSET,
        # "statusBarItem.remoteBackground": UNSET,
        # "statusBarItem.remoteForeground": UNSET,
        # "statusBarItem.remoteHoverBackground": UNSET,
        # "statusBarItem.remoteHoverForeground": UNSET,
        # "statusBarItem.errorBackground": UNSET,
        # "statusBarItem.errorForeground": UNSET,
        # "statusBarItem.errorHoverBackground": UNSET,
        # "statusBarItem.errorHoverForeground": UNSET,
        # "statusBarItem.warningBackground": UNSET,
        # "statusBarItem.warningForeground": UNSET,
        # "statusBarItem.warningHoverBackground": UNSET,
        # "statusBarItem.warningHoverForeground": UNSET,
        # "statusBarItem.compactHoverBackground": UNSET,
        # "statusBarItem.focusBorder": UNSET,
        # "statusBar.focusBorder": UNSET,
        # "statusBarItem.offlineBackground": UNSET,
        # "statusBarItem.offlineForeground": UNSET,
        # "statusBarItem.offlineHoverForeground": UNSET,
        # "statusBarItem.offlineHoverBackground": UNSET,

        # # ── Title Bar colors ────────────────────────────────────────────
        "titleBar.activeBackground": CT[brightness]['panel-4'],
        # "titleBar.activeForeground": UNSET,
        # "titleBar.inactiveBackground": UNSET,
        # "titleBar.inactiveForeground": UNSET,
        # "titleBar.border": UNSET,

        # # ── Menu Bar colors ─────────────────────────────────────────────
        # "menubar.selectionForeground": UNSET,
        # "menubar.selectionBackground": UNSET,
        # "menubar.selectionBorder": UNSET,
        "menu.foreground": CT[brightness]['foreground-4'],
        "menu.background": CT[brightness]['panel-4'],
        # "menu.selectionForeground": UNSET,
        # "menu.selectionBackground": UNSET,
        # "menu.selectionBorder": UNSET,
        # "menu.separatorBackground": UNSET,
        # "menu.border": UNSET,

        # # ── Command Center colors ───────────────────────────────────────
        # "commandCenter.foreground": UNSET,
        # "commandCenter.activeForeground": UNSET,
        "commandCenter.background": CT[brightness]['panel-3'],
        "commandCenter.border": CT['transparent'],
        # "commandCenter.activeBackground": UNSET,
        "commandCenter.activeBorder": CT['transparent'],
        # "commandCenter.inactiveForeground": UNSET,
        "commandCenter.inactiveBorder": CT['transparent'],
        # "commandCenter.debuggingBackground": UNSET,

        # # ── Notification colors ─────────────────────────────────────────
        # "notificationCenter.border": UNSET,
        # "notificationCenterHeader.foreground": UNSET,
        # "notificationCenterHeader.background": UNSET,
        # "notificationToast.border": UNSET,
        # "notifications.foreground": UNSET,
        # "notifications.background": UNSET,
        # "notifications.border": UNSET,
        # "notificationLink.foreground": UNSET,
        # "notificationsErrorIcon.foreground": UNSET,
        # "notificationsWarningIcon.foreground": UNSET,
        # "notificationsInfoIcon.foreground": UNSET,

        # # ── Banner colors ───────────────────────────────────────────────
        # "banner.background": UNSET,
        # "banner.foreground": UNSET,
        # "banner.iconForeground": UNSET,

        # # ── Extensions colors ───────────────────────────────────────────
        # "extensionButton.prominentForeground": UNSET,
        # "extensionButton.prominentBackground": UNSET,
        # "extensionButton.prominentHoverBackground": UNSET,
        # "extensionButton.background": UNSET,
        # "extensionButton.foreground": UNSET,
        # "extensionButton.hoverBackground": UNSET,
        # "extensionButton.separator": UNSET,
        # "extensionButton.border": UNSET,
        # "extensionBadge.remoteBackground": UNSET,
        # "extensionBadge.remoteForeground": UNSET,
        # "extensionIcon.starForeground": UNSET,
        # "extensionIcon.verifiedForeground": UNSET,
        # "extensionIcon.preReleaseForeground": UNSET,
        # "extensionIcon.sponsorForeground": UNSET,
        # "extensionIcon.privateForeground": UNSET,
        # "mcpIcon.starForeground": UNSET,

        # # ── Quick picker colors ─────────────────────────────────────────
        # "pickerGroup.border": UNSET,
        # "pickerGroup.foreground": UNSET,
        "quickInput.background": CT[brightness]['panel-4'],
        # "quickInput.foreground": UNSET,
        # "quickInputList.focusBackground": UNSET,
        # "quickInputList.focusForeground": UNSET,
        # "quickInputList.focusIconForeground": UNSET,
        # "quickInputTitle.background": UNSET,

        # # ── Keybinding label colors ─────────────────────────────────────
        # "keybindingLabel.background": UNSET,
        # "keybindingLabel.foreground": UNSET,
        # "keybindingLabel.border": UNSET,
        # "keybindingLabel.bottomBorder": UNSET,

        # # ── Keyboard shortcut table colors ──────────────────────────────
        # "keybindingTable.headerBackground": UNSET,
        # "keybindingTable.rowsBackground": UNSET,

        # # ── Integrated Terminal colors ──────────────────────────────────
        # "terminal.background": UNSET,
        # "terminal.border": UNSET,
        # "terminal.foreground": UNSET,
        # "terminal.ansiBlack": UNSET,
        # "terminal.ansiBlue": UNSET,
        # "terminal.ansiBrightBlack": UNSET,
        # "terminal.ansiBrightBlue": UNSET,
        # "terminal.ansiBrightCyan": UNSET,
        # "terminal.ansiBrightGreen": UNSET,
        # "terminal.ansiBrightMagenta": UNSET,
        # "terminal.ansiBrightRed": UNSET,
        # "terminal.ansiBrightWhite": UNSET,
        # "terminal.ansiBrightYellow": UNSET,
        # "terminal.ansiCyan": UNSET,
        # "terminal.ansiGreen": UNSET,
        # "terminal.ansiMagenta": UNSET,
        # "terminal.ansiRed": UNSET,
        # "terminal.ansiWhite": UNSET,
        # "terminal.ansiYellow": UNSET,
        # "terminal.selectionBackground": UNSET,
        # "terminal.selectionForeground": UNSET,
        # "terminal.inactiveSelectionBackground": UNSET,
        # "terminal.findMatchBackground": UNSET,
        # "terminal.findMatchBorder": UNSET,
        # "terminal.findMatchHighlightBackground": UNSET,
        # "terminal.findMatchHighlightBorder": UNSET,
        # "terminal.hoverHighlightBackground": UNSET,
        # "terminalCursor.background": UNSET,
        # "terminalCursor.foreground": UNSET,
        # "terminal.dropBackground": UNSET,
        # "terminal.tab.activeBorder": UNSET,
        # "terminalCommandDecoration.defaultBackground": UNSET,
        # "terminalCommandDecoration.successBackground": UNSET,
        # "terminalCommandDecoration.errorBackground": UNSET,
        # "terminalOverviewRuler.cursorForeground": UNSET,
        # "terminalOverviewRuler.findMatchForeground": UNSET,
        # "terminalStickyScroll.background": UNSET,
        # "terminalStickyScroll.border": UNSET,
        # "terminalStickyScrollHover.background": UNSET,
        # "terminal.initialHintForeground": UNSET,
        # "terminalOverviewRuler.border": UNSET,
        # "terminalCommandGuide.foreground": UNSET,

        # # ── Debug colors ────────────────────────────────────────────────
        # "debugToolBar.background": UNSET,
        # "debugToolBar.border": UNSET,
        # "editor.stackFrameHighlightBackground": UNSET,
        # "editor.focusedStackFrameHighlightBackground": UNSET,
        # "editor.inlineValuesForeground": UNSET,
        # "editor.inlineValuesBackground": UNSET,
        # "debugView.exceptionLabelForeground": UNSET,
        # "debugView.exceptionLabelBackground": UNSET,
        # "debugView.stateLabelForeground": UNSET,
        # "debugView.stateLabelBackground": UNSET,
        # "debugView.valueChangedHighlight": UNSET,
        # "debugTokenExpression.name": UNSET,
        # "debugTokenExpression.value": UNSET,
        # "debugTokenExpression.string": UNSET,
        # "debugTokenExpression.boolean": UNSET,
        # "debugTokenExpression.number": UNSET,
        # "debugTokenExpression.error": UNSET,
        # "debugTokenExpression.type": UNSET,

        # # ── Testing colors ──────────────────────────────────────────────
        # "testing.runAction": UNSET,
        # "testing.iconErrored": UNSET,
        # "testing.iconFailed": UNSET,
        # "testing.iconPassed": UNSET,
        # "testing.iconQueued": UNSET,
        # "testing.iconUnset": UNSET,
        # "testing.iconSkipped": UNSET,
        # "testing.iconErrored.retired": UNSET,
        # "testing.iconFailed.retired": UNSET,
        # "testing.iconPassed.retired": UNSET,
        # "testing.iconQueued.retired": UNSET,
        # "testing.iconUnset.retired": UNSET,
        # "testing.iconSkipped.retired": UNSET,
        # "testing.peekBorder": UNSET,
        # "testing.peekHeaderBackground": UNSET,
        # "testing.message.error.lineBackground": UNSET,
        # "testing.message.info.decorationForeground": UNSET,
        # "testing.message.info.lineBackground": UNSET,
        # "testing.messagePeekBorder": UNSET,
        # "testing.messagePeekHeaderBackground": UNSET,
        # "testing.coveredBackground": UNSET,
        # "testing.coveredBorder": UNSET,
        # "testing.coveredGutterBackground": UNSET,
        # "testing.uncoveredBranchBackground": UNSET,
        # "testing.uncoveredBackground": UNSET,
        # "testing.uncoveredBorder": UNSET,
        # "testing.uncoveredGutterBackground": UNSET,
        # "testing.coverCountBadgeBackground": UNSET,
        # "testing.coverCountBadgeForeground": UNSET,
        # "testing.message.error.badgeBackground": UNSET,
        # "testing.message.error.badgeBorder": UNSET,
        # "testing.message.error.badgeForeground": UNSET,

        # # ── Welcome page colors ─────────────────────────────────────────
        # "welcomePage.background": UNSET,
        # "welcomePage.progress.background": UNSET,
        # "welcomePage.progress.foreground": UNSET,
        # "welcomePage.tileBackground": UNSET,
        # "welcomePage.tileHoverBackground": UNSET,
        # "welcomePage.tileBorder": UNSET,
        # "walkThrough.embeddedEditorBackground": UNSET,
        # "walkthrough.stepTitle.foreground": UNSET,

        # # ── Git colors ──────────────────────────────────────────────────
        # "gitDecoration.addedResourceForeground": UNSET,
        # "gitDecoration.modifiedResourceForeground": UNSET,
        # "gitDecoration.deletedResourceForeground": UNSET,
        # "gitDecoration.renamedResourceForeground": UNSET,
        # "gitDecoration.stageModifiedResourceForeground": UNSET,
        # "gitDecoration.stageDeletedResourceForeground": UNSET,
        # "gitDecoration.untrackedResourceForeground": UNSET,
        # "gitDecoration.ignoredResourceForeground": UNSET,
        # "gitDecoration.conflictingResourceForeground": UNSET,
        # "gitDecoration.submoduleResourceForeground": UNSET,
        # "git.blame.editorDecorationForeground": UNSET,

        # # ── Source Control Graph colors ──────────────────────────────────
        # "scmGraph.historyItemHoverLabelForeground": UNSET,
        # "scmGraph.foreground1": UNSET,
        # "scmGraph.foreground2": UNSET,
        # "scmGraph.foreground3": UNSET,
        # "scmGraph.foreground4": UNSET,
        # "scmGraph.foreground5": UNSET,
        # "scmGraph.historyItemHoverAdditionsForeground": UNSET,
        # "scmGraph.historyItemHoverDeletionsForeground": UNSET,
        # "scmGraph.historyItemRefColor": UNSET,
        # "scmGraph.historyItemRemoteRefColor": UNSET,
        # "scmGraph.historyItemBaseRefColor": UNSET,
        # "scmGraph.historyItemHoverDefaultLabelForeground": UNSET,
        # "scmGraph.historyItemHoverDefaultLabelBackground": UNSET,

        # # ── Settings Editor colors ──────────────────────────────────────
        # "settings.headerForeground": UNSET,
        # "settings.modifiedItemIndicator": UNSET,
        # "settings.dropdownBackground": UNSET,
        # "settings.dropdownForeground": UNSET,
        # "settings.dropdownBorder": UNSET,
        # "settings.dropdownListBorder": UNSET,
        # "settings.checkboxBackground": UNSET,
        # "settings.checkboxForeground": UNSET,
        # "settings.checkboxBorder": UNSET,
        # "settings.rowHoverBackground": UNSET,
        # "settings.textInputBackground": UNSET,
        # "settings.textInputForeground": UNSET,
        # "settings.textInputBorder": UNSET,
        # "settings.numberInputBackground": UNSET,
        # "settings.numberInputForeground": UNSET,
        # "settings.numberInputBorder": UNSET,
        # "settings.focusedRowBackground": UNSET,
        # "settings.focusedRowBorder": UNSET,
        # "settings.headerBorder": UNSET,
        # "settings.sashBorder": UNSET,
        # "settings.settingsHeaderHoverForeground": UNSET,

        # # ── Breadcrumbs colors ──────────────────────────────────────────
        # "breadcrumb.foreground": UNSET,
        # "breadcrumb.background": UNSET,
        # "breadcrumb.focusForeground": UNSET,
        # "breadcrumb.activeSelectionForeground": UNSET,
        # "breadcrumbPicker.background": UNSET,

        # # ── Snippets colors ─────────────────────────────────────────────
        # "editor.snippetTabstopHighlightBackground": UNSET,
        # "editor.snippetTabstopHighlightBorder": UNSET,
        # "editor.snippetFinalTabstopHighlightBackground": UNSET,
        # "editor.snippetFinalTabstopHighlightBorder": UNSET,

        # # ── Symbol Icons colors ─────────────────────────────────────────
        # "symbolIcon.arrayForeground": UNSET,
        # "symbolIcon.booleanForeground": UNSET,
        # "symbolIcon.classForeground": UNSET,
        # "symbolIcon.colorForeground": UNSET,
        # "symbolIcon.constantForeground": UNSET,
        # "symbolIcon.constructorForeground": UNSET,
        # "symbolIcon.enumeratorForeground": UNSET,
        # "symbolIcon.enumeratorMemberForeground": UNSET,
        # "symbolIcon.eventForeground": UNSET,
        # "symbolIcon.fieldForeground": UNSET,
        # "symbolIcon.fileForeground": UNSET,
        # "symbolIcon.folderForeground": UNSET,
        # "symbolIcon.functionForeground": UNSET,
        # "symbolIcon.interfaceForeground": UNSET,
        # "symbolIcon.keyForeground": UNSET,
        # "symbolIcon.keywordForeground": UNSET,
        # "symbolIcon.methodForeground": UNSET,
        # "symbolIcon.moduleForeground": UNSET,
        # "symbolIcon.namespaceForeground": UNSET,
        # "symbolIcon.nullForeground": UNSET,
        # "symbolIcon.numberForeground": UNSET,
        # "symbolIcon.objectForeground": UNSET,
        # "symbolIcon.operatorForeground": UNSET,
        # "symbolIcon.packageForeground": UNSET,
        # "symbolIcon.propertyForeground": UNSET,
        # "symbolIcon.referenceForeground": UNSET,
        # "symbolIcon.snippetForeground": UNSET,
        # "symbolIcon.stringForeground": UNSET,
        # "symbolIcon.structForeground": UNSET,
        # "symbolIcon.textForeground": UNSET,
        # "symbolIcon.typeParameterForeground": UNSET,
        # "symbolIcon.unitForeground": UNSET,
        # "symbolIcon.variableForeground": UNSET,

        # # ── Debug Icons colors ──────────────────────────────────────────
        # "debugIcon.breakpointForeground": UNSET,
        # "debugIcon.breakpointDisabledForeground": UNSET,
        # "debugIcon.breakpointUnverifiedForeground": UNSET,
        # "debugIcon.breakpointCurrentStackframeForeground": UNSET,
        # "debugIcon.breakpointStackframeForeground": UNSET,
        # "debugIcon.startForeground": UNSET,
        # "debugIcon.pauseForeground": UNSET,
        # "debugIcon.stopForeground": UNSET,
        # "debugIcon.disconnectForeground": UNSET,
        # "debugIcon.restartForeground": UNSET,
        # "debugIcon.stepOverForeground": UNSET,
        # "debugIcon.stepIntoForeground": UNSET,
        # "debugIcon.stepOutForeground": UNSET,
        # "debugIcon.continueForeground": UNSET,
        # "debugIcon.stepBackForeground": UNSET,
        # "debugConsole.infoForeground": UNSET,
        # "debugConsole.warningForeground": UNSET,
        # "debugConsole.errorForeground": UNSET,
        # "debugConsole.sourceForeground": UNSET,
        # "debugConsoleInputIcon.foreground": UNSET,

        # # ── Notebook colors ─────────────────────────────────────────────
        # "notebook.editorBackground": UNSET,
        # "notebook.cellBorderColor": UNSET,
        # "notebook.cellHoverBackground": UNSET,
        # "notebook.cellInsertionIndicator": UNSET,
        # "notebook.cellStatusBarItemHoverBackground": UNSET,
        # "notebook.cellToolbarSeparator": UNSET,
        # "notebook.cellEditorBackground": UNSET,
        # "notebook.focusedCellBackground": UNSET,
        # "notebook.focusedCellBorder": UNSET,
        # "notebook.focusedEditorBorder": UNSET,
        # "notebook.inactiveFocusedCellBorder": UNSET,
        # "notebook.inactiveSelectedCellBorder": UNSET,
        # "notebook.outputContainerBackgroundColor": UNSET,
        # "notebook.outputContainerBorderColor": UNSET,
        # "notebook.selectedCellBackground": UNSET,
        # "notebook.selectedCellBorder": UNSET,
        # "notebook.symbolHighlightBackground": UNSET,
        # "notebookScrollbarSlider.activeBackground": UNSET,
        # "notebookScrollbarSlider.background": UNSET,
        # "notebookScrollbarSlider.hoverBackground": UNSET,
        # "notebookStatusErrorIcon.foreground": UNSET,
        # "notebookStatusRunningIcon.foreground": UNSET,
        # "notebookStatusSuccessIcon.foreground": UNSET,
        # "notebookEditorOverviewRuler.runningCellForeground": UNSET,

        # # ── Chart colors ────────────────────────────────────────────────
        # "charts.foreground": UNSET,
        # "charts.lines": UNSET,
        # "charts.red": UNSET,
        # "charts.blue": UNSET,
        # "charts.yellow": UNSET,
        # "charts.orange": UNSET,
        # "charts.green": UNSET,
        # "charts.purple": UNSET,
        # "chart.line": UNSET,
        # "chart.axis": UNSET,
        # "chart.guide": UNSET,

        # # ── Ports colors ────────────────────────────────────────────────
        # "ports.iconRunningProcessForeground": UNSET,

        # # ── Comments View colors ────────────────────────────────────────
        # "commentsView.resolvedIcon": UNSET,
        # "commentsView.unresolvedIcon": UNSET,

        # # ── Action Bar colors ───────────────────────────────────────────
        # "actionBar.toggledBackground": UNSET,

        # # ── Simple Find Widget colors ───────────────────────────────────
        # "simpleFindWidget.sashBorder": UNSET,

        # # ── Gauge colors ────────────────────────────────────────────────
        # "gauge.background": UNSET,
        # "gauge.foreground": UNSET,
        # "gauge.border": UNSET,
        # "gauge.warningBackground": UNSET,
        # "gauge.warningForeground": UNSET,
        # "gauge.errorBackground": UNSET,
        # "gauge.errorForeground": UNSET,

        # # ── Markdown colors ─────────────────────────────────────────────
        # "markdownAlert.note.foreground": UNSET,
        # "markdownAlert.tip.foreground": UNSET,
        # "markdownAlert.important.foreground": UNSET,
        # "markdownAlert.warning.foreground": UNSET,
        # "markdownAlert.caution.foreground": UNSET,

        # # ── Agent Session colors ────────────────────────────────────────
        # "agentSessionReadIndicator.foreground": UNSET,
        # "agentSessionSelectedBadge.border": UNSET,
        # "agentSessionSelectedUnfocusedBadge.border": UNSET,
        # "agentStatusIndicator.background": UNSET,
        # "aiCustomizationManagement.sashBorder": UNSET,
    }

    # Syntax highlighting via TextMate scopes
    token_colors = [
        {
            "name": "Comment",
            "scope": [
                "comment",
                "punctuation.definition.comment",
            ],
            "settings": {
                "fontStyle": "italic",
                "foreground": ACT[color]['main-accent'],
            },
        },
    ]

    return {
        "$schema": "vscode://schemas/color-theme",
        "name": f"fag-{color}-color-theme",  # fixed: was using $ instead of braces
        "type": brightness,
        "colors": colors,
        "tokenColors": token_colors,
    }


def build() -> None:
    """Generate theme JSON files and print the package.json contribution snippet."""

    output_dir = Path(__file__).resolve().parent.parent / "themes"
    output_dir.mkdir(parents=True, exist_ok=True)

    themes_entry: list[dict] = []

    for color in ACT:
        for brightness in ("dark", "light"):
            theme = build_color_theme(brightness, color, ACT[color])

            file_name = f"fag-{color}-{brightness}-color-theme.json"
            output_path = output_dir / file_name

            with open(output_path, "w", encoding="utf-8") as fh:
                json.dump(theme, fh, indent=2, ensure_ascii=False)

            themes_entry.append({
                "label": f"FAG-{color} {brightness} color theme",
                "uiTheme": "vs-dark" if brightness == "dark" else "vs",
                "path": f"./themes/{file_name}",
            })

    # Print a ready-to-paste package.json fragment
    package_fragment = {"contributes": {"themes": themes_entry}}
    print("Suggested package.json entry:")
    # Strip the outer braces so it can be merged into an existing file
    print(json.dumps(package_fragment, indent=2)[2:-2])


if __name__ == "__main__":
    build()
