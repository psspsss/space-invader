# Alien Space Invader

A classic arcade-style space shooter game built with Python and Pygame, inspired by the legendary Space Invaders game. This project was created as part of the Python Crash Course book by Eric Matthes.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-Latest-yellow.svg)

![image](/images/header.gif)
## Game Features

- Smooth ship movement with acceleration
- Dynamic bullet shooting mechanics
- Progressive difficulty scaling
- Score tracking system
- High score persistence
- Lives system with visual indicators
- Level progression
- Interactive play button
- Responsive alien fleet movement
- Dynamic scoring system

## Controls

- Move Left: `←` or `A` key
- Move Right: `→` or `D` key
- Shoot: `Spacebar`
- Start Game: `P` key or click Play button
- Quit Game: `Q` or `ESC` key

## Game Mechanics

- Player controls a spaceship at the bottom of the screen
- Shoot down aliens before they reach the bottom
- Each alien destroyed increases your score
- Game speed increases with each level
- You have 3 lives to start
- Score multiplier increases with level progression
- Maximum 10 bullets on screen at once
- Game ends if aliens reach the bottom or collide with the ship

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/psspsss/space-invader.git
   ```

2. Navigate to the project directory:
   ```bash
   cd space-invader
   ```

3. Install the required package:
   ```bash
   pip install pygame
   ```

4. Run the game:
   ```bash
   python3 alien_invasion.py
   ```

#  Game Flow

1. Start screen with Play button
2. Click Play or press P to start
3. Destroy alien fleet to progress
4. Speed increases with each level
5. Game ends when lives are depleted
6. High score is saved for future sessions

## Learning Highlights

- Game loop logic and event handling
- Object-oriented programming in game design
- Sprite movement and collision detection with Pygame
- Managing game state and scoring systems
## Project Structure

- `alien_invasion.py`: Main game file
- `settings.py`: Game configuration
- `ship.py`: Player ship class
- `alien.py`: Alien enemy class
- `bullet.py`: Projectile mechanics
- `game_stats.py`: Score and stats tracking
- `button.py`: Play button
- `scoreboard.py`: Score display
- `game_functions.py`: Core game mechanics

## Contributing

Feel free to fork the project and submit pull requests with improvements or bug fixes.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Eric Matthes for the Python Crash Course book
- The Pygame community
- Classic Space Invaders for inspiration

