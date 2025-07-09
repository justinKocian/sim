# kitchen.py
# Defines buttons and info panel data for the "Kitchen" room/tab.

from game_state import state
from utils import log
from ui_components import UIButton

# --- Action Helpers ---

def toggle_light():
    state.lights.kitchen = not state.lights.kitchen
    log("Toggled kitchen light", level="info")

def try_cook():
    if state.resources.food_count > 0:
        state.resources.food_count -= 1
        state.resources.cooked_count += 1
        state.resources.trash_level = min(state.resources.trash_level + 10, state.resources.trash_max)
        state.resources.dish_count += 1
        log("Cooked food", level="info")
        return True
    else:
        log("Tried to cook, but no food available.", level="info")
        return False

def try_eat():
    if state.resources.cooked_count > 0:
        state.resources.cooked_count -= 1
        log("Ate food", level="info")
        return True
    else:
        log("Tried to eat, but no cooked food.", level="info")
        return False

def try_drink():
    if state.resources.water_count > 0:
        state.resources.water_count -= 1
        log("Drank water", level="info")
        return True
    else:
        log("Tried to drink, but no water.", level="info")
        return False

def try_empty_trash():
    if state.resources.trash_level > 0:
        state.resources.trash_level = 0
        log("Emptied trash", level="info")
        return True
    else:
        log("Trash already empty.", level="info")
        return False

def try_wash_dishes():
    if state.resources.dish_count > 0:
        state.resources.dish_count = 0
        log("Washed dishes", level="info")
        return True
    else:
        log("No dishes to wash.", level="info")
        return False

def set_ac_mode(mode):
    if state.env.ac_mode != mode:
        state.env.ac_mode = mode
        if mode == "off":
            state.env.ac_state = "off"

# --- Button Definitions ---

def get_buttons():
    return [
        UIButton(
            label="Toggle Light",
            type="toggle",
            enabled=lambda: True,
            get=lambda: state.lights.kitchen,
            action=toggle_light
        ),
        UIButton(
            label="Cook",
            type="action",
            enabled=lambda: True,
            get=lambda: False,
            action=try_cook
        ),
        UIButton(
            label="Eat",
            type="action",
            enabled=lambda: True,
            get=lambda: False,
            action=try_eat
        ),
        UIButton(
            label="Drink",
            type="action",
            enabled=lambda: True,
            get=lambda: False,
            action=try_drink
        ),
        UIButton(
            label="Empty Trash",
            type="action",
            enabled=lambda: True,
            get=lambda: False,
            action=try_empty_trash
        ),
        UIButton(
            label="Wash Dishes",
            type="action",
            enabled=lambda: True,
            get=lambda: False,
            action=try_wash_dishes
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
        ("Ingredients", "Available" if state.resources.food_count > 0 else "Missing"),
        ("Food", str(state.resources.cooked_count)),
        ("Trash", f'{int((state.resources.trash_level / state.resources.trash_max) * 100)}%'),
        ("Dishes", str(state.resources.dish_count)),
        ("Light", "ON" if state.lights.kitchen else "OFF"),
        ("Inside Temp", f"{state.env.inside_temp:.1f}°F"),
        ("A/C Mode", state.env.ac_mode.upper()),
        ("A/C Status", state.env.ac_state.upper())
    ]
