# main.py
# Main entry point for the Retro Home Sim game.
# Handles setup, main loop, input processing, and rendering.

import pygame
import sys
from engine.config import *
from engine.game_state import state
from engine.audio import AudioController
from engine.ui import (
    draw_main_menu,
    draw_button_grid,
    draw_info_panel,
    draw_tabs,
    draw_borders,
    draw_key_hints,
    draw_time_panel,
    draw_modal
)
from engine.timekeeper import advance_time
from engine.scheduler import setup_events, check_events
from automations import register_all_automations, run_automations
from engine.room_manager import get_info_panel, get_buttons

# Schedule all predefined game events
setup_events()

# Register all automation modules and their decorators
register_all_automations()

# Initialize Pygame and setup window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro Home Sim")
clock = pygame.time.Clock()

tick_accumulator = 0  # For controlling time progression by config-defined ticks

# Ensure first frame renders
state.needs_redraw = True

def current_tab():
    """Returns the name of the currently selected tab."""
    return TABS[state.tab_index]

def handle_game_input(event):
    """
    Handles key input during active gameplay.
    If a modal is visible, only handles ENTER to dismiss it.
    Otherwise, handles navigation, tab switching, and actions.
    """
    if state.modal.visible:
        if event.key == pygame.K_RETURN:
            state.modal.visible = False
            state.modal.on_dismiss()
        return

    state.needs_redraw = True
    buttons = get_buttons(current_tab())

    # Navigation (arrow keys or WASD)
    if event.key in (pygame.K_LEFT, pygame.K_a):
        state.sel_index = (state.sel_index - 1) % len(buttons)

    elif event.key in (pygame.K_RIGHT, pygame.K_d):
        state.sel_index = (state.sel_index + 1) % len(buttons)

    elif event.key in (pygame.K_UP, pygame.K_w):
        state.sel_index = (state.sel_index - COLS) % len(buttons)

    elif event.key in (pygame.K_DOWN, pygame.K_s):
        state.sel_index = (state.sel_index + COLS) % len(buttons)

    # Confirm / activate
    elif event.key == pygame.K_RETURN:
        if buttons:
            btn = buttons[state.sel_index]
            if btn.enabled():
                btn.action()

    # Tab navigation (TAB forward, SHIFT+TAB back)
    elif event.key == pygame.K_TAB:
        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
            state.tab_index = (state.tab_index - 1) % len(TABS)
        else:
            state.tab_index = (state.tab_index + 1) % len(TABS)
        state.sel_index = 0

    # Info page cycling (Q = prev, E = next)
    elif event.key == pygame.K_q or event.key == pygame.K_PAGEUP:
        tab = current_tab()
        current = state.info_page.pages.get(tab, 0)
        total = max(1, (len(get_info_panel(tab)) + INFO_LINES_PER_PAGE - 1) // INFO_LINES_PER_PAGE)
        state.info_page.pages[tab] = (current - 1) % total

    elif event.key == pygame.K_e or event.key == pygame.K_PAGEDOWN:
        tab = current_tab()
        current = state.info_page.pages.get(tab, 0)
        total = max(1, (len(get_info_panel(tab)) + INFO_LINES_PER_PAGE - 1) // INFO_LINES_PER_PAGE)
        state.info_page.pages[tab] = (current + 1) % total

def main():
    global tick_accumulator

    # Initialize audio system
    #audio = AudioController()
    #audio.play_music("assets\music\music_bleepinblooper.ogg")

    while True:
        delta_ms = clock.tick(FPS)
        delta_sec = delta_ms / 1000.0
        tick_accumulator += delta_sec

        # Process input first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if not state.game_started:
                    if event.key == pygame.K_RETURN:
                        state.game_started = True
                        state.needs_redraw = True
                else:
                    handle_game_input(event)

        # Advance game time regardless of input
        if state.game_started:
            while tick_accumulator >= REAL_SECONDS_PER_TICK:
                advance_time(REAL_SECONDS_PER_TICK)
                check_events()
                run_automations()
                state.needs_redraw = True
                tick_accumulator -= REAL_SECONDS_PER_TICK

        # Draw main menu or game screen
        if not state.game_started:
            draw_main_menu(screen)
            pygame.display.flip()
            continue

        if getattr(state, "needs_redraw", True):  # ← key change to ensure default True
            screen.fill(BG_COLOR)
            draw_time_panel(screen)
            draw_borders(screen)
            draw_tabs(screen)
            draw_button_grid(screen)
            draw_info_panel(screen)
            draw_key_hints(screen)
            draw_modal(screen)
            pygame.display.flip()
            state.needs_redraw = False

# Entry point
if __name__ == "__main__":
    main()
