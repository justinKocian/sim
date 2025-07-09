# config.py
# Global configuration constants for Retro Home Sim

# Time system
REAL_SECONDS_PER_TICK = 1                         # How many real seconds per game tick
INGAME_MINUTES_PER_TICK = 60                      # Game time progression rate (minutes per real second) - max of 60 otherwise it breaks

# Screen and layout settings
SCREEN_WIDTH = 720                                                                  # Window width in pixels
SCREEN_HEIGHT = 720                                                                 # Window height in pixels
BTN_WIDTH = 140                                                                     # Button width in pixels
BTN_HEIGHT = 35                                                                     # Button height in pixels
PADDING = 24                                                                        # Padding between buttons/components
COLS = 3                                                                            # Number of columns in button grid
TABS = ["outside", "kitchen", "bathroom", "laundry", "office", "log", "bedroom"]    # Tab labels
FPS = 60                                                                            # Target frames per second

# Font settings
FONT_NAME = "Courier New"                          # Retro-style font name
FONT_SIZE = 16                                     # Font size in points

# Info/log panel configuration
INFO_LINES_PER_PAGE = 8                            # Number of info lines per page in info panel
LOG_LINES = 8                                      # Number of log lines shown at once

# UI style and colors
BORDER_PAD = 8                                     # Border padding between UI elements
SECTION_MARGIN = 20                                # Margin between major sections
SECTION_BORDER_COLOR = (90, 90, 90)                # Color of section borders (RGB)
BG_COLOR = (10, 10, 20)                            # Background color of the screen (RGB)

# Calendar and date system
DAYS = [                                           # Days of the week
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

MONTHS = [                                         # Months and their corresponding day counts
    ("January", 31), ("February", 28), ("March", 31), ("April", 30),
    ("May", 31), ("June", 30), ("July", 31), ("August", 31),
    ("September", 30), ("October", 31), ("November", 30), ("December", 31)
]