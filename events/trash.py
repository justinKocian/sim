# events/trash.py

from scheduler import weekly_on
from utils import log
from game_state import state

@weekly_on(5, hour=8, minute=0, label="Trash Pickup Monday")    # Monday
@weekly_on(3, hour=8, minute=0, label="Trash Pickup Thursday")  # Thursday
def trash_pickup():
    log("Trash pickup occurred!")
    state.resources.trash_level = 0

def register():
    pass
