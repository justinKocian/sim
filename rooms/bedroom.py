# bedroom.py
# Defines buttons and info panel data for the "Bedroom" room/tab.

from game_state import state
from utils import log
from ui_components import UIButton

# --- Action Helpers ---

def try_toggle_light():
    setattr(state.lights, "bedroom", not state.lights.bedroom)
    log("Toggled bedroom light", level="info")

# --- Button Definitions ---

def get_buttons():
    return [
        UIButton(
            label="Toggle Light",
            type="toggle",
            enabled=lambda: True,
            get=lambda: state.lights.bedroom,
            action=try_toggle_light
        )
    ]

# --- Info Panel ---

def get_info():
    return [("Light", "ON" if state.lights.bedroom else "OFF")]
