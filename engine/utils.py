# utils.py
# Provides a basic logging function and shake utility using predefined profiles.

import math
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

def pulse_brightness(color, frame_count, speed=6, scale_range=(0.5, 1.0)):
    """
    Returns a pulsing version of a given color.

    Parameters:
        color (tuple): Base (R, G, B)
        frame_count (int): The current frame or tick count
        speed (int): How fast the pulse oscillates (lower = faster)
        scale_range (tuple): Min/max brightness scale
    """
    min_scale, max_scale = scale_range
    wave = math.sin(frame_count / speed)
    scale = min_scale + (max_scale - min_scale) * ((wave + 1) / 2)  # Normalize to 0–1
    return tuple(min(255, max(0, int(c * scale))) for c in color)