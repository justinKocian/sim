# laundry.py
# Defines buttons and info panel data for the "Laundry" room/tab.

from game_state import state
from utils import log
from ui_components import UIButton

def try_start_laundry():
    state.rooms.laundry_running = True
    log("Started laundry", level="info")

def try_stop_laundry():
    state.rooms.laundry_running = False
    log("Stopped laundry", level="info")

def get_buttons():
    return [
        UIButton(
            label="Start Laundry",
            type="action",
            enabled=lambda: not state.rooms.laundry_running,
            get=lambda: state.rooms.laundry_running,
            action=try_start_laundry
        ),
        UIButton(
            label="Stop Laundry",
            type="action",
            enabled=lambda: state.rooms.laundry_running,
            get=lambda: state.rooms.laundry_running,
            action=try_stop_laundry
        )
    ]

def get_info():
    return [
        ("Laundry", "RUNNING" if state.rooms.laundry_running else "IDLE"),
        ("Basket", "Full" if state.rooms.progress > 0 else "Empty")  # placeholder logic
    ]
