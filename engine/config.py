# config.py
# Global configuration constants for Retro Home Sim with resolution scaling support

# Time system
REAL_SECONDS_PER_TICK = 1                         # How many real seconds per game tick
INGAME_MINUTES_PER_TICK = 60                      # Game time progression rate (minutes per real second)

# Base resolution (design target)
BASE_WIDTH = 720
BASE_HEIGHT = 720

# Runtime screen resolution (can be updated by settings or UI)
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

# Layout and grid configuration
BTN_WIDTH = 140                                   # Base button width (scaled in layout)
BTN_HEIGHT = 35                                   # Base button height
PADDING = 24                                      # Padding between buttons/components
COLS = 3                                          # Number of columns in button grid

# Tab labels (used for tab layout and logic)
TABS = [
    # First Row
    "outside",
    "kitchen",
    "bathroom",
    "laundry",
    "office",
    "bedroom",

    # Second Row
    "home",
    "log",
    "bob"
]

# Target framerate
FPS = 60

# Font settings
FONT_NAME = "Courier New"                         # Retro-style font name
FONT_SIZE = 16                                     # Font size in points

# Info/log panel configuration
INFO_LINES_PER_PAGE = 12                          # Number of info lines per page in info panel
LOG_LINES = 8                                     # Number of log lines shown at once

# UI styling and colors
BORDER_PAD = 8                                    # Border padding between UI elements
SECTION_MARGIN = 20                               # Margin between major sections
SECTION_BORDER_COLOR = (90, 90, 90)               # Color of section borders (RGB)
BG_COLOR = (10, 10, 20)                           # Background color of the screen (RGB)

# Calendar and date system
DAYS = [                                          # Days of the week
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

MONTHS = [                                        # Months and their corresponding day counts
    ("January", 31), ("February", 28), ("March", 31), ("April", 30),
    ("May", 31), ("June", 30), ("July", 31), ("August", 31),
    ("September", 30), ("October", 31), ("November", 30), ("December", 31)
]

DEFAULT_RESOLUTIONS = [
    (720, 720),
    (1024, 768),
    (1280, 800),
    (1280, 1024),
    (1600, 900),
    (1920, 1080)
]
