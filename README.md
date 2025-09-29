# 🚀 Space Adventure Game

This project is an **interactive space-themed game** I built for my **Introduction to Computer Science class**.  
It was written entirely in **Python**, using the `Draw` graphics library, and showcases my ability to combine **programming fundamentals, game design, and user interaction** into a fun, playable experience.

---

## How to Play

- **Movement:** Use **↑ Up** and **↓ Down** arrow keys to move your ship.  
- **Shield:** Press **Space** to activate a shield (if available) — makes you temporarily invincible.  
- **Laser:** Press **→ Right** arrow to fire a laser and destroy monsters.  

### Objective
- Avoid asteroids and monsters.  
- Collect **gold hearts** to gain extra lives (max 5).  
- Collect **shields** to add more shield charges (max 3).  
- Survive until the end of the strip and **rack up the highest score you can!**  

---

## Project Structure

| File | Description |
|------|-------------|
| **`finalProject.py`** | Contains the full game logic. I wrote this entirely on my own as part of my Intro to CS course, before AI-assisted coding was common. |
| **`Draw.py`** | Graphics library provided by my professor to simplify UI rendering for beginners. Must be in the same folder for the game to run. |
| **`.gif files`** | Custom sprite assets (spaceship, asteroids, monsters, effects) created in Canva. These must also be in the same folder for the game to work. |

---

## Key Features & Technical Highlights

- **Structured Game Design:**  
  Represented game objects (stars, asteroids, monsters, shields, gold) as **lists of lists** with attributes like type, position, and state (hit/not hit).  

- **Collision Detection:**  
  Implemented **pixel-accurate collision checks** between the ship and other objects to handle hits, pickups, and laser strikes.  

- **Dynamic Graphics & Animation:**  
  - Continuously redraws the canvas to simulate smooth motion.  
  - Implements **parallax scrolling stars** for depth.  
  - Real-time animations for explosions, lasers, and character movement.  

- **Game State Management:**  
  - Tracks score, lives, shields, and power-up usage.  
  - Handles shield timers, laser cooldowns, and increasing game speed as the player progresses.  

- **User Interaction:**  
  - Intuitive keyboard controls.  
  - Start screen, character selection menu, and replayable end screen.  
  - Name input for high-score tracking.  

- **Difficulty Scaling:**  
  The game becomes faster and more challenging the longer you survive.  

- **Readable Code Structure:**  
  Code organized into **modular functions** for drawing, collisions, game loop updates, and event handling — improving maintainability.  

---

## Technologies Used

- **Language:** Python  
- **Graphics:** `Draw` library (provided for CS course)  
- **Assets:** Custom `.gif` files created with Canva  

---

## Learning Outcomes

Building this game taught me:
- How to think in **game loops** and handle frame-by-frame updates.
- Practical problem-solving while implementing **collision detection** and **timing mechanics**.
- Organizing code into **modular, reusable functions**.
- Debugging interactive programs with moving elements and animations.

---

## Running the Game

1. Clone this repository:  
   ```bash
   git clone https://github.com/elianaweinstein01/Space-Adventure-Game.git
   cd Space-Adventure-Game
2. Ensure Draw.py and all .gif files are in the same folder as finalProject.py.
3. Run the game:
   ```bash
   python3 finalProject.py

