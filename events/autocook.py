# events/autocook.py

from scheduler import every_day_at
from rooms.kitchen import try_cook  # ← Import the shared logic

@every_day_at(hour=9, minute=0, label="Auto-Cook at 9AM")
def auto_cook():
    try_cook()

def register():
    pass
