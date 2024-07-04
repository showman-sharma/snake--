# 3D Look Snake Game with Detailed Rats, Hedgehogs, and Moles

## Overview

This project is a modern take on the classic Snake game, featuring 3D-looking snakes, detailed rats, hedgehogs, and moles. The game includes additional features such as blood splatter effects, collision detection with walls, and sound effects for various events. The game is developed using Pygame.

## Features

- **3D Look Snake**: The snake is rendered with realistic shadows, eyes, and fangs to give a 3D appearance.
- **Detailed Rats**: Rats randomly emerge from the edges of the walls, can eat the apple, and have shadows, eyes, ears, teeth, and tails. When the snake eats a rat, the rat makes a squeak sound, and blood splatter is generated.
- **Hedgehogs**: Hedgehogs also emerge from the edges of the walls, and when eaten by the snake, they cause the snake to blink in red and green, slow down for 5 seconds, and generate blood splatter.
- **Moles**: Moles spawn randomly, move towards the apple to eat it, and leave the screen by digging holes. They have shadows, eyes, hands, and a snout. When the snake eats a mole, blood splatter is generated.
- **Realistic Shadows and Lighting**: Objects like the snake, rats, hedgehogs, and apples have realistic shadows.
- **Sound Effects**: Various sound effects for eating apples, rats, crashing into walls, and warnings when eating hedgehogs.
- **Blood Splatter Effects**: Blood splatters are generated when the snake eats a rat, hedgehog, or mole, or crashes into a wall.
- **Collision Detection**: The snake dies when it collides with the wall or itself, with appropriate sound effects and visual feedback.
- **Scorecard**: Displays the current score and high score on the top left corner of the screen.
- **Name Input**: Takes the user's name as input before starting the game.
- **Save Scores**: Saves names and scores into a CSV file using pandas and uses it to track high scores.
- **Buttons**: Provides "Replay" and "Quit" buttons when the game is over.

## Directory Structure

```
snake_game/
├── assets/
│   ├── sounds/
│   │   ├── crunch.mp3
│   │   ├── rat_squish.mp3
│   │   ├── snake_squish.mp3
│   │   ├── rat_squeak.mp3
│   │   ├── hedgehog_squeak.mp3
│   │   ├── mole_squeak.mp3
│   │   └── snake_crunch.mp3
│   └── images/
│       └── wood_texture.png
├── data/
│   └── high_scores.csv
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── game.py
│   ├── snake.py
│   ├── rat.py
│   ├── hedgehog.py
│   ├── mole.py
│   └── utils.py
└── README.md
```

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/showman-sharma/snake_plus.git
   cd snake_game
   ```

2. **Install the required dependencies:**

   ```sh
   pip install pygame pandas
   ```

3. **Ensure the assets are in the correct directories:**

   - Place all sound files (`crunch.mp3`, `rat_squish.mp3`, `snake_squish.mp3`, `rat_squeak.mp3`, `hedgehog_squeak.mp3`, `mole_squeak.mp3`, and `snake_crunch.mp3`) in the `assets/sounds/` directory.
   - Place the wood texture image (`wood_texture.png`) in the `assets/images/` directory.

## How to Play

1. **Run the game:**

   ```sh
   python src/game.py
   ```

2. **Controls:**
   - Use the arrow keys to move the snake.
   - The objective is to eat the apples to grow the snake.
   - Avoid running into the walls or the snake itself.

3. **Additional Game Mechanics:**
   - **Rats**: Rats appear randomly and can eat the apple. If the snake eats a rat, the rat makes a squeak sound, and blood splatter is generated.
   - **Hedgehogs**: Hedgehogs appear randomly, and when eaten by the snake, they cause the snake to blink in red and green, slow down for 5 seconds, and generate blood splatter.
   - **Moles**: Moles spawn randomly and move towards the apple to eat it. They leave the screen by digging holes. When the snake eats a mole, blood splatter is generated.
   - **Blood Splatter**: Blood splatters are generated when the snake eats a rat, hedgehog, or mole, or crashes into a wall.
   - **Game Over**: The game ends when the snake collides with the wall or itself. A wooden textured board with the score is displayed, and "Replay" and "Quit" buttons appear.
   - **Scorecard**: Displays the current score and high score on the top left corner of the screen.
   - **Name Input**: Takes the user's name as input before starting the game.
   - **Save Scores**: Saves names and scores into a CSV file using pandas and uses it to track high scores.

## Code Explanation

### `config.py`

This file contains all the configuration settings, including screen dimensions, colors, game variables, and file paths.

### `utils.py`

This file contains utility functions for drawing the grass, brick fencing, apple, blood splatter, wall holes, and the wooden board. It also includes the function `new_apple_position` to generate a new apple position, and functions to handle high scores and user name input using pandas.

### `game.py`

This is the main game file. It handles the game loop, event handling, drawing objects on the screen, and playing sound effects. It also initializes the Pygame module and sets up the game screen.

### `snake.py`

This file contains functions related to the snake, including drawing the snake.

### `rat.py`

This file contains functions for spawning, moving, and drawing rats, as well as playing the appropriate sound effects when a rat is spawned or eaten.

### `hedgehog.py`

This file contains functions for spawning, moving, and drawing hedgehogs, as well as playing the appropriate sound effects when a hedgehog is spawned or eaten.

### `mole.py`

This file contains functions for spawning, moving, and drawing moles, as well as playing the appropriate sound effects when a mole is spawned or eaten.

## Future Improvements

- Add more obstacles and power-ups.
- Implement different game levels with increasing difficulty.
- Add a high score feature.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the Apache 2.0 License.