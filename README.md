# Sim (Timekeeper)

A real-time, retro-inspired home simulation game built with Python and Pygame.

## Overview

Sim (also referred to as Timekeeper) is a minimalistic simulation game where players manage a daily routine across different rooms of a house. The game features a time-driven loop, contextual interactions, and dynamic resource and environment management.

## Features

* **Tick-Based Time System**

  * In-game time advances incrementally, influencing events and behaviors.

* **Room Navigation**

  * Navigate between rooms like Kitchen, Bathroom, and Outside, each with unique interactions.

* **Resource Management**

  * Manage food, trash, dirty dishes, and ingredients.

* **Temperature System**

  * Simulates indoor/outdoor temperature changes.
  * A/C system with manual and auto modes based on hysteresis control.

* **UI and Modal System**

  * Custom UI framework with interactive buttons and modal popups.

* **Scheduling System**

  * Simple event scheduler with support for recurring tasks.

* **Modular Architecture**

  * Designed using dataclasses for a clean, maintainable structure.

## Installation

### Requirements

* Python 3.10+
* Pygame

### Setup

```bash
pip install -r requirements.txt
python main.py
```

## Directory Structure

```
.
├── engine/              # Game state, config, and systems
├── rooms/               # Room-specific logic and buttons
├── automations/         # Background processes like temperature control
├── scheduler.py         # Time-based event scheduling
├── ui_components.py     # Reusable UI elements
├── main.py              # Game entry point
└── ...
```

## Screenshots

#### Main Menu
![Main Menu](screenshots\main_menu.png)

#### Kitchen Tab
![Kitchen Tab](screenshots\kitchen_tab.png)

#### Home Tab
![Home Tab](screenshots\home_tab.png)

#### Log Tab
![Log Tab](screenshots\log_tab.png)

## Roadmap

* Activity system (e.g. showering, sleeping)
* Character needs and mood
* Improved room variety and utility
* Saving and loading game state
* More automation hooks and UI polish

## Shout Out
Shout out to Elektrobear for the music
Check them out [here on itch](https://moonanagames.itch.io/)

## License

TBD
