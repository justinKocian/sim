# events/__init__.py

from . import trash
from . import daily_message
from . import autocook

def register_all_events():
    trash.register()
    daily_message.register()
    autocook.register()
