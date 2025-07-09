# events/autocook.py

from engine.scheduler import every_day_at
from rooms.kitchen import try_cook, try_eat

@every_day_at(hour=9, minute=0, label="Auto-Cook at 9AM")
def auto_cook():
    try_cook()
    try_eat()

def register():
    pass
