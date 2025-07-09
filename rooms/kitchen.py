# kitchen.py
# Defines buttons and info panel data for the "Kitchen" room/tab.

from engine.game_state import state
from engine.utils import log
from engine.ui_components import UIButton, show_modal

# --- Action Helpers ---

def toggle_light():
    state.lights.kitchen = not state.lights.kitchen
    log("Toggled kitchen light", level="info")

def try_cook():
    if state.resources.trash_level >= state.resources.trash_max:
        show_modal("The trash is full! Empty it before cooking.")
        log("Tried to cook, but trash is full.", level="info")
        return False
    if (state.resources.dish_count / state.resources.dish_max) >= 1.0:
        show_modal("The sink is full of dirty dishes! Wash them first.")
        log("Tried to cook, but the sink is full.", level="info")
        return False
    if state.resources.ingredients > 0:
        state.resources.ingredients -= 1
        state.resources.food_count += 1
        state.resources.trash_level = min(
            state.resources.trash_level + 5, state.resources.trash_max
        )
        state.resources.dish_count = min(
            state.resources.dish_count + int(state.resources.dish_max * 0.05),  # +5% of max
            state.resources.dish_max
        )
        log("Cooked food", level="info")
        return True
    else:
        show_modal("You don't have any ingredients to cook.")
        log("Tried to cook, but no ingredients available.", level="info")
        return False

def try_eat():
    if state.resources.trash_level >= state.resources.trash_max:
        show_modal("The trash is full! Empty it before eating.")
        log("Tried to eat, but trash is full.", level="info")
        return False
    if (state.resources.dish_count / state.resources.dish_max) >= 1.0:
        show_modal("The sink is full of dirty dishes!\nWash them first.")
        log("Tried to eat, but the sink is full.", level="info")
        return False
    if state.resources.food_count > 0:
        state.resources.food_count -= 1
        state.resources.trash_level = min(
            state.resources.trash_level + 10, state.resources.trash_max
        )
        state.resources.dish_count = min(
            state.resources.dish_count + int(state.resources.dish_max * 0.10),  # +10% of max
            state.resources.dish_max
        )
        state.needs.hunger = max(state.needs.hunger - 5, 0)
        log("Ate food", level="info")
        return True
    else:
        show_modal("You're out of food to eat.")
        log("Tried to eat, but no food available.", level="info")
        return False

def try_drink():
    if state.resources.water_count > 0:
        state.resources.water_count -= 1
        state.needs.thirst = 0
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
        )
    ]

# --- Info Panel ---

def get_info():
    return [
        ("Light", "ON" if state.lights.kitchen else "OFF"),
        ("Ingredients", state.resources.ingredients),
        ("Food", str(state.resources.food_count)),
        ("Trash", f'{int((state.resources.trash_level / state.resources.trash_max) * 100)}%'),
        ("Dishes", f'{int((state.resources.dish_count / state.resources.dish_max) * 100)}%')
    ]
