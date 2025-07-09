from dataclasses import dataclass
from typing import Callable
from engine.game_state import state

@dataclass
class UIButton:
    label: str
    type: str  # "toggle" or "action"
    enabled: Callable[[], bool]
    get: Callable[[], bool]
    action: Callable[[], None]

def show_modal(message: str, on_dismiss: Callable[[], None] = lambda: None):
    state.modal.visible = True
    state.modal.message = message
    state.modal.on_dismiss = on_dismiss
