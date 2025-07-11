# game_state.py
# Refactored to use dataclasses for structured game state management

from dataclasses import dataclass, field
from typing import Dict, List, Callable
from engine.screen_shake import ScreenShake

@dataclass
class Environment:
    outside_temp: float = 65.0
    inside_temp: float = 72.0
    ac_mode: str = "auto"     # "off", "on", or "auto"
    ac_state: str = "off"     # "off", "cooling", or "heating"
    ac_target: float = 72.0   # Desired temp in auto mode

@dataclass
class Needs:
    hunger: int = 10
    thirst: int = 10
    fatigue: int = 0

@dataclass
class Resources:
    food_count: int = 10
    water_count: int = 2
    dish_count: int = 0
    dish_max: int = 100
    trash_level: int = 0
    trash_max: int = 100
    ingredients: int = 5
    money: int = 100

@dataclass
class Lights:
    kitchen: bool = False
    office: bool = False
    laundry: bool = False
    outside: bool = False
    bathroom: bool = False
    bedroom: bool = False

@dataclass
class RoomStates:
    door_locked: bool = True
    laundry_running: bool = False
    mail_checked: bool = False

@dataclass
class InfoPageState:
    pages: Dict[str, int] = field(default_factory=lambda: {
        "outside": 0,
        "kitchen": 0,
        "bathroom": 0,
        "laundry": 0,
        "office": 0,
        "log": 0,
        "bedroom": 0
    })

@dataclass
class TimeState:
    minute: int = 0
    hour: int = 0
    day: int = 13
    month: int = 9
    year: int = 2000
    time_accumulator: float = 0.0

@dataclass
class ModalState:
    visible: bool = False
    message: str = ""
    on_dismiss: Callable[[], None] = lambda: None

@dataclass
class GameState:
    game_started: bool = False
    tab_index: int = 0
    sel_index: int = 0
    needs_redraw: bool = True
    modal: ModalState = field(default_factory=ModalState)

    env: Environment = field(default_factory=Environment)
    resources: Resources = field(default_factory=Resources)
    lights: Lights = field(default_factory=Lights)
    rooms: RoomStates = field(default_factory=RoomStates)
    info_page: InfoPageState = field(default_factory=InfoPageState)
    time: TimeState = field(default_factory=TimeState)
    needs: Needs = field(default_factory=Needs)
    screen_shake: ScreenShake = field(default_factory=ScreenShake)

    log_entries: List[str] = field(default_factory=list)
    debug_mode: bool = False

# Singleton instance
state = GameState()
