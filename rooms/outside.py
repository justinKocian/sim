# outside.py
# Defines buttons and info panel data for the "Outside" room/tab.

from game_state import state
from utils import log
from ui_components import UIButton

def try_lock_door():
    state.rooms.door_locked = not state.rooms.door_locked
    log("Toggled door lock", level="info")

def try_check_mail():
    state.rooms.mail_checked = True
    log("Checked the mailbox", level="info")

def get_buttons():
    return [
        UIButton(
            label="Lock Door",
            type="toggle",
            enabled=lambda: True,
            get=lambda: state.rooms.door_locked,
            action=try_lock_door
        ),
        UIButton(
            label="Check Mail",
            type="action",
            enabled=lambda: not state.rooms.mail_checked,
            get=lambda: False,
            action=try_check_mail
        )
    ]

def get_info():
    return [
        ("Door", "LOCKED" if state.rooms.door_locked else "UNLOCKED"),
        ("Light", "ON" if state.lights.outside else "OFF"),
        ("Mail", "Collected" if state.rooms.mail_checked else "Uncollected"),
        ("Temp", f"{state.env.outside_temp:.1f}°F")
    ]
