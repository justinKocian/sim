# office.py
# Defines buttons and info panel data for the "Office" room/tab.

from engine.game_state import state
from engine.utils import log
from engine.ui_components import UIButton
from engine.ui_components import show_modal

def try_toggle_light():
    state.lights.office = not state.lights.office
    log("Toggled kitchen light", level="info")

def test_modal():
    show_modal("This is a test pop-up modal.")


def get_buttons():
    return [
        UIButton(
            label="Toggle Light",
            type="toggle",
            enabled=lambda: True,
            get=lambda: state.lights.office,
            action=try_toggle_light
        ),
        UIButton(
            label="Modal",
            type="action",
            enabled=lambda: True,
            get=lambda: False,
            action=test_modal
        )
    ]

def get_info():
    return [
        ("Light", "ON" if state.lights.office else "OFF")
    ]
