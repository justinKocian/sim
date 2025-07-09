# events/daily_message.py
from engine.scheduler import get_weekday_index

from engine.scheduler import every_day_at
from engine.utils import log
from engine.game_state import state
from engine.config import DAYS

@every_day_at(hour=0, minute=0, label="Daily Greeting")
def daily_greeting():
    weekday_index = get_weekday_index()
    weekday_name = DAYS[weekday_index]
    log(f"A new day begins! It is {weekday_name}.")

def register():
    pass
