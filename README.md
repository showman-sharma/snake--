# SNAKE++

This project is a modern take on the classic Snake game, featuring 3D-looking snakes, detailed rats, hedgehogs, and moles. The game includes additional features such as blood splatter effects, collision detection with walls, sound effects for various events, and high score tracking. The game is developed using Pygame.

## Features

- **3D Look Snake**: The snake is rendered with realistic shadows, eyes, and fangs to give a 3D appearance.
- **Detailed Rats**: Rats randomly emerge from the edges of the walls, can eat the apple, and have shadows, eyes, ears, teeth, and tails. When the snake eats a rat, the rat makes a squeak sound, and blood splatter is generated.
- **Hedgehogs**: Hedgehogs also emerge from the edges of the walls, and when eaten by the snake, they cause the snake to blink in red and green, slow down for 5 seconds, and generate blood splatter.
- **Moles**: Moles dig holes, move towards the apple, eat it, and then vanish by digging another hole. When the snake eats a mole, it gains length and points.
- **Realistic Shadows and Lighting**: Objects like the snake, rats, hedgehogs, and apples have realistic shadows.
- **Sound Effects**: Various sound effects for eating apples, rats, crashing into walls, and warnings when eating hedgehogs.
- **Blood Splatter Effects**: Blood splatters are generated when the snake eats a rat or hedgehog, or crashes into a wall.
- **Collision Detection**: The snake dies when it collides with the wall or itself, with appropriate sound effects and visual feedback.
- **High Score Tracking**: High scores are saved and displayed.

## Directory Structure

```
snake_plus_plus/
├── assets/
│   ├── sounds/
│   │   ├── crunch.mp3
│   │   ├── rat_squish.mp3
│   │   ├── snake_squish.mp3
│   │   ├── rat_squeak.mp3
│   │   ├── hedgehog_squeak.mp3
│   │   ├── snake_crunch.mp3
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
   git clone https://github.com/showman-sharma/snake_plus_plus.git
   cd snake_plus_plus
   ```

2. **Install the required dependencies:**

   ```sh
   pip install pygame pandas
   ```

3. **Ensure the assets are in the correct directories:**

   - Place all sound files (`crunch.mp3`, `rat_squish.mp3`, `snake_squish.mp3`, `rat_squeak.mp3`, `hedgehog_squeak.mp3`, `snake_crunch.mp3`, `snake_slither.mp3`, and `welcome_music.mp3`) in the `assets/sounds/` directory.
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

3. **Game Mechanics:**
   - **Rats**: Rats appear randomly and can eat the apple. If the snake eats a rat, the rat makes a squeak sound, and blood splatter is generated.
   - **Hedgehogs**: Hedgehogs appear randomly, and when eaten by the snake, they cause the snake to blink in red and green, slow down for 5 seconds, and generate blood splatter.
   - **Moles**: Moles move towards apples, eat them, and dig holes to vanish. If the snake eats a mole, it gains points and length.
   - **Blood Splatter**: Blood splatters are generated when the snake eats a rat or hedgehog, or crashes into a wall.
   - **Game Over**: The game ends when the snake collides with the wall or itself. A wooden textured board with a "You Lost!" message is displayed, and you can press `Enter` to replay or `Esc` to quit.

## Future Improvements

- Add more obstacles and power-ups.
- Implement different game levels with increasing difficulty.
- Add a high score feature.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the Apache 2.0 License.