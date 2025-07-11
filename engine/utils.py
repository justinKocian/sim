# utils.py
# Provides a basic logging function and shake utility using predefined profiles.

from engine.game_state import state

# Supported log levels
LOG_LEVELS = ["info", "debug"]

def log(message, level="info"):
    """
    Adds a log message to the global log_entries list in game state.

    Parameters:
        message (str): The message to log.
        level (str): Either "info" or "debug". Debug logs are shown only if debug_mode is enabled.
    """
    # Skip debug messages if debug_mode is disabled
    if level == "debug" and not state.debug_mode:
        return

    # Format and store the log entry
    entry = f"[{level.upper()}] {message}"
    state.log_entries.append(entry)

    # Cap log history to 100 messages
    if len(state.log_entries) > 100:
        state.log_entries.pop(0)

# Predefined shake profiles
SHAKE_PROFILES = {
    "light": {"duration": 0.2, "intensity": 3},
    "medium": {"duration": 0.4, "intensity": 6},
    "strong": {"duration": 0.6, "intensity": 10},
}

def trigger_shake(profile="medium"):
    """
    Triggers a screen shake using a predefined profile.
    Available profiles: light, medium, strong.
    """
    p = SHAKE_PROFILES.get(profile, SHAKE_PROFILES["medium"])
    state.screen_shake.trigger(duration=p["duration"], intensity=p["intensity"])
    log(f"Triggered screen shake: {profile}", level="debug")
