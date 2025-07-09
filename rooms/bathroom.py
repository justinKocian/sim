# bathroom.py
# Defines buttons and info panel data for the "Bathroom" room/tab.

from engine.game_state import state
from engine.utils import log
from engine.ui_components import UIButton

# --- Action Helpers ---

def try_toggle_light():
    setattr(state.lights, "bathroom", not state.lights.bathroom)
    log("Toggled bathroom light", level="info")

def try_use_sink():
    log("Used the sink", level="info")

def try_flush_toilet():
    log("Flushed the toilet", level="info")

def try_take_shower():
    log("Took a shower", level="info")

# --- Button Definitions ---

def get_buttons():
    return [
        UIButton(
            label="Toggle Light",
            type="toggle",
            enabled=lambda: True,
            get=lambda: state.lights.bathroom,
            action=try_toggle_light
        ),
        UIButton(
            label="Use Sink",
            type="action",
            enabled=lambda: True,
            get=lambda: False,
            action=try_use_sink
        ),
        UIButton(
            label="Flush Toilet",
            type="action",
            enabled=lambda: True,
            get=lambda: False,
            action=try_flush_toilet
        ),
        UIButton(
            label="Take Shower",
            type="action",
            enabled=lambda: True,
            get=lambda: False,
            action=try_take_shower
        )
    ]

# --- Info Panel ---

def get_info():
    return [
        ("Light", "ON" if state.lights.bathroom else "OFF")
    ]
