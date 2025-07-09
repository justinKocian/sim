# events/__init__.py

from . import trash
from . import daily_message
from . import autocook
from . import maildelivery

def register_all_events():
    trash.register()
    daily_message.register()
    autocook.register()
    maildelivery.register()
