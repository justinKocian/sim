# bob.py
# Defines info panel content for the Bob tab.

from engine.game_state import state

def get_buttons():
    """
    The bob tab has no interactive buttons.
    """
    return []

def get_info():
    return [
        ("Hunger", state.needs.hunger),
        ("Thirst", state.needs.thirst)
    ]
