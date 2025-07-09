# kitchen.py
# Defines buttons and info panel data for the "Kitchen" room/tab.

from engine.game_state import state
from engine.utils import log
from engine.ui_components import UIButton, show_modal

# --- Action Helpers ---

def set_ac_mode(mode):
    if state.env.ac_mode != mode:
        state.env.ac_mode = mode
        if mode == "off":
            state.env.ac_state = "off"

def try_order_food():
    cost = 10
    if state.resources.money >= cost:
        state.resources.money -= cost
        state.resources.ingredients += 10
        log("Ordered food delivery (10 ingredients)", level="info")
        return True
    else:
        show_modal("Not enough money to order food.")
        log("Tried to order food, but not enough money.", level="info")
        return False

# --- Button Definitions ---

def get_buttons():
    return [
        UIButton(
            label="Order Food",
            type="action",
            enabled=lambda: state.resources.money >= 10,
            get=lambda: False,
            action=try_order_food
        ),
        UIButton(
            label="A/C: Off",
            type="action",
            enabled=lambda: state.env.ac_mode != "off",
            get=lambda: state.env.ac_mode == "off",
            action=lambda: set_ac_mode("off")
        ),
        UIButton(
            label="A/C: On",
            type="action",
            enabled=lambda: state.env.ac_mode != "on",
            get=lambda: state.env.ac_mode == "on",
            action=lambda: set_ac_mode("on")
        ),
        UIButton(
            label="A/C: Auto",
            type="action",
            enabled=lambda: state.env.ac_mode != "auto",
            get=lambda: state.env.ac_mode == "auto",
            action=lambda: set_ac_mode("auto")
        ),
    ]

# --- Info Panel ---

def get_info():
    return [
        ("Inside Temp", f"{state.env.inside_temp:.1f}°F"),
        ("A/C Mode", state.env.ac_mode.upper()),
        ("A/C Status", state.env.ac_state.upper()),
    ]
