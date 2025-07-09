# ui_components.py
from dataclasses import dataclass
from typing import Callable

@dataclass
class UIButton:
    label: str
    type: str  # "toggle" or "action"
    enabled: Callable[[], bool]
    get: Callable[[], bool]
    action: Callable[[], None]
