# scheduler.py
# Handles time-based scheduling and execution of in-game events

from engine.game_state import state
from engine.config import MONTHS
from engine.utils import log
from typing import Callable

event_queue = []

def schedule_event(day_of_week: int, hour: int, minute: int, callback: Callable, *, label=None, repeat=True):
    """
    Registers a scheduled event to trigger at a specific day/time.
    """
    event = {
        "day_of_week": day_of_week,
        "hour": hour,
        "minute": minute,
        "callback": callback,
        "repeat": repeat,
        "label": label or callback.__name__
    }
    event_queue.append(event)

def scheduled_event(day_of_week: int, hour: int, minute: int, *, label=None, repeat=True):
    """
    Decorator to schedule a function at a specific weekday/time.
    """
    def wrapper(func: Callable):
        schedule_event(day_of_week, hour, minute, func, label=label, repeat=repeat)
        return func
    return wrapper

def every_day_at(hour: int, minute: int, *, label=None, repeat=True):
    """
    Decorator to schedule a function at the same time every day.
    """
    def wrapper(func: Callable):
        for dow in range(7):
            schedule_event(dow, hour, minute, func, label=label, repeat=repeat)
        return func
    return wrapper

def weekly_on(day_of_week: int, hour: int, minute: int, *, label=None):
    """
    Decorator to schedule a function once per week.
    """
    return scheduled_event(day_of_week, hour, minute, label=label, repeat=True)

def weekdays_at(hour: int, minute: int, *, label=None, repeat=True):
    """
    Decorator to schedule a function on weekdays (Monday to Friday).
    """
    def wrapper(func: Callable):
        for dow in range(0, 5):  # Monday to Friday
            schedule_event(dow, hour, minute, func, label=label, repeat=repeat)
        return func
    return wrapper

def weekends_at(hour: int, minute: int, *, label=None, repeat=True):
    """
    Decorator to schedule a function on weekends (Saturday and Sunday).
    """
    def wrapper(func: Callable):
        for dow in (5, 6):  # Saturday and Sunday
            schedule_event(dow, hour, minute, func, label=label, repeat=repeat)
        return func
    return wrapper

def check_events():
    """
    Called every tick to evaluate and trigger matching scheduled events.
    """
    now_hour = state.time.hour
    now_minute = state.time.minute
    weekday_index = get_weekday_index()

    for event in event_queue[:]:
        if (event["day_of_week"] == weekday_index and
            event["hour"] == now_hour and
            event["minute"] == now_minute):
            event["callback"]()
            if not event["repeat"]:
                event_queue.remove(event)

def get_weekday_index():
    """
    Returns 0-6 (Monday to Sunday) based on in-game date.
    Jan 1, 2000 is treated as Saturday (index 6).
    """
    total_days = state.time.day - 1
    for m in range(state.time.month):
        total_days += MONTHS[m][1]
    return (6 + total_days) % 7  # Jan 1, 2000 was Saturday

def setup_events():
    """
    Imports all event modules and registers decorated functions.
    """
    from events import register_all_events
    register_all_events()
