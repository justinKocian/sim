# ui.py
# Handles all screen rendering: buttons, info panels, borders, menus, and key hints.

import pygame
from dataclasses import dataclass
from typing import Callable
from engine.config import *
from engine.game_state import state
from engine.timekeeper import get_time_string, get_date_string
from engine.room_manager import get_buttons, get_info_panel

# --- UI Button Structure ---

@dataclass
class UIButton:
    label: str
    type: str  # "action" or "toggle"
    enabled: Callable[[], bool]
    get: Callable[[], bool]
    action: Callable[[], None]

# --- Font and Layout ---

pygame.font.init()
FONT = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

TAB_ROW_HEIGHT = FONT_SIZE + 10
MAX_TAB_ROWS = 2
TAB_AREA_HEIGHT = 60 + MAX_TAB_ROWS * TAB_ROW_HEIGHT
BUTTON_GRID_TOP = TAB_AREA_HEIGHT + 20
INFO_PANEL_TOP = TAB_AREA_HEIGHT + 250

# --- Basic Text Rendering Utilities ---

def draw_text(screen, text, x, y, color=(200, 200, 200)):
    surface = FONT.render(text, True, color)
    screen.blit(surface, (x, y))

def draw_centered(screen, text, y, color=(200, 200, 200)):
    surface = FONT.render(text, True, color)
    rect = surface.get_rect(center=(SCREEN_WIDTH // 2, y))
    screen.blit(surface, rect.topleft)

# --- Structural UI Drawing ---

def draw_borders(screen):
    pygame.draw.rect(
        screen, SECTION_BORDER_COLOR,
        (BORDER_PAD, BORDER_PAD, SCREEN_WIDTH - 2 * BORDER_PAD, SCREEN_HEIGHT - 2 * BORDER_PAD), 2)

    grid_box = pygame.Rect(
        SECTION_MARGIN, TAB_AREA_HEIGHT,
        SCREEN_WIDTH - 2 * SECTION_MARGIN, 220
    )
    pygame.draw.rect(screen, SECTION_BORDER_COLOR, grid_box, 2)

    info_box = pygame.Rect(
        SECTION_MARGIN, grid_box.bottom + 20,
        SCREEN_WIDTH - 2 * SECTION_MARGIN,
        SCREEN_HEIGHT - grid_box.bottom - 2 * SECTION_MARGIN - 40
    )
    pygame.draw.rect(screen, SECTION_BORDER_COLOR, info_box, 2)
    draw_text(screen, "Info", info_box.left + 8, info_box.top - 20)

# --- Time Panel ---

def draw_time_panel(screen):
    panel_rect = pygame.Rect(
        SECTION_MARGIN, BORDER_PAD + 8,
        SCREEN_WIDTH - 2 * SECTION_MARGIN,
        40
    )
    pygame.draw.rect(screen, SECTION_BORDER_COLOR, panel_rect, 2)
    text = f"{get_time_string()}   |   {get_date_string()}"
    draw_centered(screen, text, panel_rect.top + 15)

# --- Button Grid and Button Rendering ---

def draw_button_grid(screen):
    tab = current_tab()
    if tab == "log":
        draw_log_panel(screen)
    else:
        buttons = get_buttons(tab)
        total_width = COLS * BTN_WIDTH + (COLS - 1) * PADDING
        start_x = (SCREEN_WIDTH - total_width) // 2
        start_y = BUTTON_GRID_TOP

        for i, btn in enumerate(buttons):
            col = i % COLS
            row = i // COLS
            x = start_x + col * (BTN_WIDTH + PADDING)
            y = start_y + row * (BTN_HEIGHT + PADDING)
            draw_button(screen, i, x, y, btn)

def draw_button(screen, i, x, y, btn: UIButton):
    enabled = btn.enabled()
    active = btn.get()
    selected = i == state.sel_index

    COLORS = {
        "disabled_bg": (24, 24, 24),
        "disabled_fg": (80, 80, 80),
        "disabled_selected_bg": (40, 20, 20),
        "disabled_selected_fg": (120, 80, 80),

        "toggle_on_bg": (0, 60, 0),
        "toggle_on_fg": (160, 255, 160),
        "toggle_on_selected_bg": (0, 90, 0),
        "toggle_on_selected_fg": (255, 255, 220),

        "toggle_off_bg": (32, 32, 32),
        "toggle_off_fg": (140, 140, 140),
        "toggle_off_selected_bg": (50, 50, 80),
        "toggle_off_selected_fg": (200, 200, 255),

        "selected_bg": (40, 40, 80),
        "selected_fg": (240, 240, 255),

        "default_bg": (20, 20, 20),
        "default_fg": (200, 200, 200),

        "border": (80, 80, 80),
    }

    if not enabled and selected:
        bg = COLORS["disabled_selected_bg"]
        fg = COLORS["disabled_selected_fg"]
    elif not enabled:
        bg = COLORS["disabled_bg"]
        fg = COLORS["disabled_fg"]
    elif btn.type == "toggle" and active and selected:
        bg = COLORS["toggle_on_selected_bg"]
        fg = COLORS["toggle_on_selected_fg"]
    elif btn.type == "toggle" and not active and selected:
        bg = COLORS["toggle_off_selected_bg"]
        fg = COLORS["toggle_off_selected_fg"]
    elif btn.type == "toggle" and active:
        bg = COLORS["toggle_on_bg"]
        fg = COLORS["toggle_on_fg"]
    elif btn.type == "toggle" and not active:
        bg = COLORS["toggle_off_bg"]
        fg = COLORS["toggle_off_fg"]
    elif selected:
        bg = COLORS["selected_bg"]
        fg = COLORS["selected_fg"]
    else:
        bg = COLORS["default_bg"]
        fg = COLORS["default_fg"]

    pygame.draw.rect(screen, bg, (x, y, BTN_WIDTH, BTN_HEIGHT))
    pygame.draw.rect(screen, COLORS["border"], (x, y, BTN_WIDTH, BTN_HEIGHT), 2)

    label_surface = FONT.render(btn.label, True, fg)
    label_rect = label_surface.get_rect(center=(x + BTN_WIDTH // 2, y + BTN_HEIGHT // 2))
    screen.blit(label_surface, label_rect)

# --- Log Panel ---

def draw_log_panel(screen):
    log_lines = state.log_entries[-LOG_LINES:]
    x, y = 30, BUTTON_GRID_TOP
    for line in log_lines:
        draw_text(screen, line[:60], x, y)
        y += 24

# --- Info Panel ---

def draw_info_panel(screen):
    tab = current_tab()
    info = get_info_panel(tab)
    total_pages = max(1, (len(info) + INFO_LINES_PER_PAGE - 1) // INFO_LINES_PER_PAGE)
    current_page = state.info_page.pages.get(tab, 0)

    y = INFO_PANEL_TOP
    start = current_page * INFO_LINES_PER_PAGE
    for line in info[start:start + INFO_LINES_PER_PAGE]:
        draw_text(screen, f"{line[0]}: {line[1]}", 30, y)
        y += 24

    if total_pages > 1:
        draw_text(screen, f"[Page {current_page + 1}/{total_pages}]", 420, y)

# --- Tab Header ---

def draw_tabs(screen):
    tab_labels = [f"[{t.upper()}]" for t in TABS]
    label_surfaces = [FONT.render(label, True, (0, 0, 0)) for label in tab_labels]
    label_widths = [surf.get_width() for surf in label_surfaces]
    padding = 20
    max_row_width = SCREEN_WIDTH - 2 * SECTION_MARGIN

    rows = []
    current_row = []
    current_width = 0

    for label, surf, width in zip(tab_labels, label_surfaces, label_widths):
        if current_row and (current_width + width + padding > max_row_width):
            rows.append(current_row)
            current_row = []
            current_width = 0
        current_row.append((label, surf, width))
        current_width += width + padding

    if current_row:
        rows.append(current_row)

    start_y = 60
    for row in rows:
        row_width = sum(w for _, _, w in row) + padding * (len(row) - 1)
        x = (SCREEN_WIDTH - row_width) // 2
        for i, (label, surf, width) in enumerate(row):
            tab_index = tab_labels.index(label)
            color = (80, 160, 255) if tab_index == state.tab_index else (100, 100, 100)
            label_surface = FONT.render(label, True, color)
            screen.blit(label_surface, (x, start_y))
            x += width + padding
        start_y += TAB_ROW_HEIGHT

# --- Main Menu ---

def draw_main_menu(screen):
    screen.fill(BG_COLOR)
    draw_centered(screen, "HOUSE SIM", 240)
    draw_centered(screen, "Press ENTER to Start", 280)
    pygame.display.flip()

# --- Key Hint Overlay ---

def draw_key_hints(screen):
    y = SCREEN_HEIGHT - 55
    lines = [
        ["[←↑↓→] Move", "[ENTER] Select"],
        ["[Z] Switch Tab", "[SPACE] Info Page"]
    ]
    for row_i, row in enumerate(lines):
        x = 20
        for hint in row:
            draw_text(screen, hint, x, y + row_i * 18, (100, 100, 100))
            x += 180

# --- Utility ---

def current_tab():
    return TABS[state.tab_index]
