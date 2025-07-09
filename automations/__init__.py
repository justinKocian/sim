# automations/__init__.py

from typing import Callable, List

_tick_automations: List[Callable] = []
_named_triggers: dict[str, Callable] = {}

def automation(func: Callable):
    """
    Decorator to register a function to run every tick.
    """
    _tick_automations.append(func)
    return func

def on_trigger(name: str):
    """
    Decorator to register a named automation that can be called manually.
    """
    def wrapper(func: Callable):
        _named_triggers[name] = func
        return func
    return wrapper

def run_automations():
    """
    Call all registered tick-based automations once per tick.
    """
    for func in _tick_automations:
        func()

def trigger(name: str):
    """
    Call a named automation manually (e.g. from a button).
    """
    if name in _named_triggers:
        _named_triggers[name]()

def register_all_automations():
    """
    Import all automation modules to register decorators.
    """
    from . import temp  # ← add additional modules as needed
