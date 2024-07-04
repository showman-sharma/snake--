# SNAKE++
## Overview

This project is a modern take on the classic Snake game, featuring 3D-looking snakes, detailed rats, hedgehogs, and moles. The game includes additional features such as blood splatter effects, collision detection with walls, and sound effects for various events. The game is developed using Pygame.

## Features

- **3D Look Snake**: The snake is rendered with realistic shadows, eyes, and fangs to give a 3D appearance.
- **Detailed Rats**: Rats randomly emerge from the edges of the walls, can eat the apple, and have shadows, eyes, ears, teeth, and tails. When the snake eats a rat, the rat makes a squeak sound, and blood splatter is generated.
- **Hedgehogs**: Hedgehogs also emerge from the edges of the walls, and when eaten by the snake, they cause the snake to blink in red and green, slow down for 5 seconds, and generate blood splatter.
- **Moles**: Moles spawn randomly on the green surface, move towards the apple to eat it, and create holes when they enter and exit the ground.
- **Realistic Shadows and Lighting**: Objects like the snake, rats, hedgehogs, moles, and apples have realistic shadows.
- **Sound Effects**: Various sound effects for eating apples, rats, hedgehogs, and self-collision. Background music for different game states.
- **Blood Splatter Effects**: Blood splatters are generated when the snake eats a rat, hedgehog, or mole, or crashes into a wall.
- **Collision Detection**: The snake dies when it collides with the wall or itself, with appropriate sound effects and visual feedback.
- **High Score Tracking**: The game tracks and displays high scores, storing them in a CSV file.

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
│   │   ├── snake_crunch.mp3
│   │   ├── mole_squeak.mp3
│   │   ├── buzzer.mp3
│   │   ├── snake_slither.mp3
│   │   └── welcome_music.mp3
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

   - Place all sound files (`crunch.mp3`, `rat_squish.mp3`, `snake_squish.mp3`, `rat_squeak.mp3`, `hedgehog_squeak.mp3`, `snake_crunch.mp3`, `mole_squeak.mp3`, `buzzer.mp3`, `snake_slither.mp3`, and `welcome_music.mp3`) in the `assets/sounds/` directory.
   - Place the wood texture image (`wood_texture.png`) in the `assets/images/` directory.
   - Ensure the `high_scores.csv` file is in the `data/` directory.

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
   - **Moles**: Moles spawn randomly, move towards the apple to eat it, and create holes when they enter and exit the ground. Blood splatter is generated when the snake eats a mole.
   - **Blood Splatter**: Blood splatters are generated when the snake eats a rat, hedgehog, or mole, or crashes into a wall.
   - **Game Over**: The game ends when the snake collides with the wall or itself. A wooden textured board with a "SCORE" message is displayed, and you can press `Replay` to play again or `Quit` to exit.

## Code Explanation

### `config.py`

This file contains all the configuration settings, including screen dimensions, colors, game variables, and sound files.

### `utils.py`

This file contains utility functions for drawing the grass, brick fencing, apple, blood splatter, wall holes, the wooden board, rings, getting the high score, saving the score, and handling the welcome screen and user name input.

### `game.py`

This is the main game file. It handles the game loop, event handling, drawing objects on the screen, playing sound effects, and managing game states.

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

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the Apache 2.0 License.

