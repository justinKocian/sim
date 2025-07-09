# timekeeper.py
# Handles in-game time progression and date/time formatting

from engine.config import INGAME_MINUTES_PER_TICK, MONTHS, DAYS
from engine.game_state import state

WEEKDAY_INDEX_FOR_JAN_1_2000 = 6

def advance_time(delta_seconds):
    """
    Advances the in-game clock by a fixed number of in-game minutes per tick.
    """
    state.time.minute += INGAME_MINUTES_PER_TICK

    if state.time.minute >= 60:
        state.time.minute -= 60
        state.time.hour += 1

        if state.time.hour >= 24:
            state.time.hour = 0
            state.time.day += 1

            days_in_month = MONTHS[state.time.month][1]
            if state.time.day > days_in_month:
                state.time.day = 1
                state.time.month += 1

                if state.time.month >= 12:
                    state.time.month = 0
                    state.time.year += 1

def get_time_string():
    """
    Returns the current in-game time as HH:MM (24-hour format).
    """
    return f"{state.time.hour:02}:{state.time.minute:02}"

def get_date_string():
    total_days = state.time.day - 1
    for m in range(state.time.month):
        total_days += MONTHS[m][1]

    weekday_index = (WEEKDAY_INDEX_FOR_JAN_1_2000 + total_days) % 7
    weekday = DAYS[weekday_index]
    month_name = MONTHS[state.time.month][0]

    return f"{weekday}, {month_name} {state.time.day}, {state.time.year}"

