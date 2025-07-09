# log.py
# Defines info panel content for the Log tab.
# This tab displays system messages but does not include interactive buttons.

from game_state import state

def get_buttons():
    """
    The log tab has no interactive buttons.
    """
    return []

def get_info():
    """
    Returns log tab info panel entries as a list of (label, value) tuples.
    Shows number of log entries and current log mode.
    """
    return [
        ("Logs", f"{len(state.log_entries)} entries"),
        ("Mode", "DEBUG" if state.debug_mode else "INFO"),
    ]
