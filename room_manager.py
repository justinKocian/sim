# room_manager.py
# Provides unified access to button and info panel functions for each room/tab.

# Import button and info panel functions from each room module
from rooms.outside import get_buttons as get_outside_buttons, get_info as get_outside_info
from rooms.kitchen import get_buttons as get_kitchen_buttons, get_info as get_kitchen_info
from rooms.bathroom import get_buttons as get_bathroom_buttons, get_info as get_bathroom_info
from rooms.laundry import get_buttons as get_laundry_buttons, get_info as get_laundry_info
from rooms.office import get_buttons as get_office_buttons, get_info as get_office_info
from rooms.log import get_buttons as get_log_buttons, get_info as get_log_info
from rooms.bedroom import get_buttons as get_bedroom_buttons, get_info as get_bedroom_info
from rooms.bob import get_buttons as get_bob_buttons, get_info as get_bob_info
from rooms.home import get_buttons as get_home_buttons, get_info as get_home_info

# Mapping of tab names to their corresponding button generation functions
BUTTON_GETTERS = {
    "outside": get_outside_buttons,
    "kitchen": get_kitchen_buttons,
    "bathroom": get_bathroom_buttons,
    "laundry": get_laundry_buttons,
    "office": get_office_buttons,
    "log": get_log_buttons,
    "bedroom": get_bedroom_buttons,
    "bob": get_bob_buttons,
    "home": get_home_buttons
}

# Mapping of tab names to their corresponding info panel data functions
INFO_GETTERS = {
    "outside": get_outside_info,
    "kitchen": get_kitchen_info,
    "bathroom": get_bathroom_info,
    "laundry": get_laundry_info,
    "office": get_office_info,
    "log": get_log_info,
    "bedroom": get_bedroom_info,
    "bob": get_bob_info,
    "home": get_home_info
}

def get_buttons(tab):
    """
    Returns a list of buttons for the given tab/room.
    Defaults to empty list if the tab is not recognized.
    """
    return BUTTON_GETTERS.get(tab, lambda: [])()

def get_info_panel(tab=None):
    """
    Returns the info panel data for the given tab/room.
    Defaults to 'outside' tab if none is specified.
    """
    tab = tab or "outside"
    return INFO_GETTERS.get(tab, lambda: [])()
