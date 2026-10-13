# Brake'Em 🌈

A classic **Breakout** arcade game clone built in Python using the `pygame` library. Featuring a vibrant rainbow-colored brick layout arranged in a unique triangular shape!

---

## Features

* **Classic Arcade Action:** Control a paddle to bounce a ball and clear out the bricks.
* **Unique Brick Layout:** Bricks are arranged in an inverted triangular formation for an extra gameplay challenge.
* **Rainbow Palette:** Visually appealing row-based rainbow coloring scheme.
* **Simple & Lightweight:** Built entirely in a single file with minimal dependencies.

---

## Requirements

* Python 3.x
* Pygame

---

## Installation & Running

1. **Clone the repository** (or save the code as `main.py`):
```bash
git clone https://github.com/your-username/rainbow-breakout.git
cd rainbow-breakout

```


2. **Install Pygame:**
```bash
pip install pygame

```


3. **Run the game:**
```bash
python main.py

```



---

## Controls

| Key | Action |
| --- | --- |
| **Left Arrow** (`←`) | Move Paddle Left |
| **Right Arrow** (`→`) | Move Paddle Right |
| **Close Window** (`X`) | Quit Game |

---

## Code Structure

The game runs within a straightforward game loop handled by `pygame`:

* **Initialization:** Sets up an 800x600 display window, defines game constants, colors, and creates the rect objects for the paddle, ball, and triangular brick formation.
* **Game Loop:** Handles user keyboard input, updates ball physics and collision detection (walls, paddle, and bricks), and redraws all elements onto the screen at ~30 FPS.