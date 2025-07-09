# events/maildelivery.py

from scheduler import every_day_at
from game_state import state
from utils import log

def try_deliver_mail():
    state.rooms.mail_checked = False
    log("Mail has been delivered", level="info")

@every_day_at(hour=9, minute=0)
def mail_delivery():
    try_deliver_mail()

def register():
    pass
