# ui_layout.py
# Handles layout and resolution scaling

from engine.config import BASE_WIDTH, BASE_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, FONT_SIZE

scale_x = SCREEN_WIDTH / BASE_WIDTH
scale_y = SCREEN_HEIGHT / BASE_HEIGHT

# Scaled dimensions
BTN_WIDTH = int(140 * scale_x)
BTN_HEIGHT = int(35 * scale_y)
PADDING = int(24 * scale_x)
BORDER_PAD = int(8 * scale_x)
SECTION_MARGIN = int(20 * scale_x)
FONT_SIZE_SCALED = int(FONT_SIZE * scale_y)

# Layout anchors
TAB_ROW_HEIGHT = FONT_SIZE_SCALED + 10
MAX_TAB_ROWS = 2
TAB_AREA_HEIGHT = 60 + MAX_TAB_ROWS * TAB_ROW_HEIGHT
BUTTON_GRID_TOP = TAB_AREA_HEIGHT + 20
INFO_PANEL_TOP = TAB_AREA_HEIGHT + 250
COLS = 3

def scale(value, axis='x'):
    return int(value * (scale_x if axis == 'x' else scale_y))

def get_button_position(row, col):
    total_width = COLS * BTN_WIDTH + (COLS - 1) * PADDING
    start_x = (SCREEN_WIDTH - total_width) // 2
    x = start_x + col * (BTN_WIDTH + PADDING)
    y = BUTTON_GRID_TOP + row * (BTN_HEIGHT + PADDING)
    return x, y
