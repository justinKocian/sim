Here’s a simple and professional `README.md` for your game, ready to accompany your screenshot:

---

# Retro Home Sim

**Retro Home Sim** is a Python-based simulation game where you manage daily tasks and resources in a nostalgic, pixel-style home interface. Play progresses in real-time with in-game time advancing on a custom calendar system.

## Features

* **Multi-Room Simulation**: Interact with various rooms including Kitchen, Bathroom, Laundry, Office, and Outside.
* **Time-Based Events**: In-game time advances with each tick. Scheduled events like trash pickup occur automatically.
* **Resource Management**: Cook food, use water, take showers, wash dishes, and keep your environment clean.
* **Retro UI**: Styled with a grid-based interface, tab navigation, and a Courier-inspired font.
* **System Log**: Tracks your actions and environment changes for feedback and debugging.

## Controls

* **Arrow Keys**: Navigate between buttons
* **Enter**: Perform the selected action
* **Z**: Switch to the next room/tab
* **Space**: Scroll info panel pages

## Screenshot
![Screenshot](screenshots\image.png)

## Requirements

* Python 3.8+
* [pygame](https://www.pygame.org/) (install via `pip install pygame`)

## Running the Game

```bash
python main.py
```

## Folder Structure

```
.
├── main.py            # Game entry point
├── config.py          # Global settings and constants
├── game_state.py      # Mutable in-game state
├── ui.py              # Rendering logic for UI
├── timekeeper.py      # In-game clock and calendar
├── scheduler.py       # Time-based event system
├── room_manager.py    # Room-level UI integration
├── rooms/             # Room-specific logic (kitchen, bathroom, etc.)
└── utils.py           # Logging utilities
```

## License

MIT License

---

Let me know if you'd like a version tailored for GitHub, itch.io, or other distribution platforms.
