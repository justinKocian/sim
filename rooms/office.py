# office.py
# Defines buttons and info panel data for the "Office" room/tab.

from engine.game_state import state
from engine.utils import log
from engine.ui_components import UIButton

def try_toggle_light():
    state.lights.office = not state.lights.office
    log("Toggled kitchen light", level="info")

def get_buttons():
    return [
        UIButton(
            label="Toggle Light",
            type="toggle",
            enabled=lambda: True,
            get=lambda: state.lights.office,
            action=try_toggle_light
        )
    ]

def get_info():
    return [
        ("Light", "ON" if state.lights.office else "OFF")
    ]
