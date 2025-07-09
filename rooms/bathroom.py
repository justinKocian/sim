# bathroom.py
# Defines buttons and info panel data for the "Bathroom" room/tab.

from game_state import state
from utils import log
from ui_components import UIButton

# --- Action Helpers ---

def try_toggle_light():
    setattr(state.lights, "bathroom", not state.lights.bathroom)
    log("Toggled bathroom light", level="info")

def try_use_sink():
    setattr(state.resources, "water_count", state.resources.water_count - 1)
    log("Used the sink", level="info")

def try_flush_toilet():
    log("Flushed the toilet", level="info")

def try_take_shower():
    setattr(state.resources, "water_count", state.resources.water_count - 2)
    log("Took a shower", level="info")
    setattr(state.rooms, "cleanliness", min(100, state.rooms.cleanliness + 30))

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
            enabled=lambda: state.resources.water_count > 0,
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
            enabled=lambda: state.resources.water_count >= 2,
            get=lambda: False,
            action=try_take_shower
        )
    ]

# --- Info Panel ---

def get_info():
    cleanliness = state.rooms.cleanliness
    level = (
        "Dirty" if cleanliness < 30 else
        "OK" if cleanliness < 70 else
        "Clean"
    )
    return [
        ("Light", "ON" if state.lights.bathroom else "OFF"),
        ("Water", str(state.resources.water_count)),
        ("Cleanliness", level)
    ]
