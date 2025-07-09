# automations/temp.py

from automations import automation
from game_state import state
import math

@automation
def update_outside_temperature():
    hour = state.time.hour + state.time.minute / 60
    state.env.outside_temp = round(65 + 15 * math.sin((hour - 4) * math.pi / 12), 1)

@automation
def update_inside_temperature():
    """
    Simulates passive drift toward outside temperature and A/C influence.
    """
    env = state.env
    drift_rate = 0.05  # degrees per tick toward outside temp
    influence = 0.3    # A/C heating or cooling per tick

    # Drift naturally toward outside temp
    delta = env.outside_temp - env.inside_temp
    env.inside_temp += drift_rate * delta

    # Apply A/C effect
    if env.ac_state == "cooling":
        env.inside_temp -= influence
    elif env.ac_state == "heating":
        env.inside_temp += influence

    env.inside_temp = round(env.inside_temp, 1)

@automation
def control_air_conditioning():
    """
    Decides when A/C should activate based on mode and hysteresis.
    """
    env = state.env

    if env.ac_mode == "off":
        env.ac_state = "off"
        return

    if env.ac_mode == "on":
        if env.inside_temp > env.ac_target:
            env.ac_state = "cooling"
        elif env.inside_temp < env.ac_target:
            env.ac_state = "heating"
        else:
            env.ac_state = "off"
        return

    # Auto mode (hysteresis)
    buffer = 1.5  # degrees
    if env.inside_temp > env.ac_target + buffer:
        env.ac_state = "cooling"
    elif env.inside_temp < env.ac_target - buffer:
        env.ac_state = "heating"
    elif env.ac_state in ["cooling", "heating"]:
        # Hold state until crossing back into comfort zone
        if (env.ac_state == "cooling" and env.inside_temp <= env.ac_target):
            env.ac_state = "off"
        elif (env.ac_state == "heating" and env.inside_temp >= env.ac_target):
            env.ac_state = "off"
