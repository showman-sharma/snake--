# Development Process for SNAKE++

The project was created by sequential prompt engineering on ChatGPT 4.0, with some minor human intervention and changes. This document outlines the step-by-step prompting and development process for creating SNAKE++, featuring detailed rats, hedgehogs, and moles.

## 1. Initial Snake Game Creation

**Prompt:**
Create a simple snake game using Python and Pygame.

- Set up a basic snake game on a 2D plane with standard gameplay mechanics (movement, eating apples, and growing).

## 2. 3D Look and Realistic Shadows

**Prompt:**
Make the snake look like a real 3D snake, and add realistic shadows and lighting.

- Added visual elements to give the snake a 3D appearance with shadows and lighting effects.

## 3. Adding Snake Features (Eyes and Fangs)

**Prompt:**
Give the snake eyes and fangs.

- Enhanced the snake's visual details to make it more lifelike.

## 4. Adding Apple Features

**Prompt:**
Make the apple look like a real apple with a leaf on top, and give it a shadow.

- Added details to the apple to improve its visual appeal.

## 5. Background Enhancement

**Prompt:**
Make the background look like grass with appropriate shadows and lighting.

- Further enhanced the game’s visual elements by adding a grass texture to the background.

## 6. Brick Fencing

**Prompt:**
Draw brick fencing on the outer boundaries of the game.

- Added a boundary to the game area to create a confined playing field.

## 7. Collision and Death Mechanics

**Prompt:**
The snake should die as soon as it touches the wall.

- Added collision detection and game-over mechanics when the snake hits the wall.

## 8. Blood Splatter Effects

**Prompt:**
Create a blood splatter effect when and where the snake hits the wall.

- Introduced visual effects to indicate the snake's death.

## 9. Introducing Rats

**Prompt:**
Introduce the concept of rats that randomly emerge from the edges of the walls, walk perpendicularly to the opposite wall, and make holes there.

- Added another dynamic element to the game where rats move across the screen.

## 10. Detailed Rat Features

**Prompt:**
Give the rat a shadow, eyes, ears, 2 tiny teeth, and a thin long wavy tail.

- Enhanced the rat's visual details to make them more realistic.

## 11. Introducing Holes for Rats

**Prompt:**
Give the effect of making holes in the walls when the rat enters and exits.

- Added visual effects for rat entries and exits.

## 12. Adding Hedgehogs

**Prompt:**
Introduce the concept of hedgehogs that are spiky blobs with two cute eyes. They move like rats, and when the snake eats them, it stops and blinks in red, slows down for 5 seconds, and then vanishes.

- Added another dynamic element with specific interactions with the snake.

## 13. Modularizing the Code

**Prompt:**
Break the code into modular segments with game.py, config.py, utils.py, snake.py, rat.py, and hedgehog.py.

- Organized the code into separate modules for better maintainability and readability.

## 14. Adding Sound Effects

**Prompt:**
Add sound effects for various actions: crunching sound when eating an apple, squishing sound when eating a rat, and a warning buzzer when eating a hedgehog.

- Enhanced the game with auditory feedback for different actions.

## 15. Enhancing Mole Features

**Prompt:**
Introduce moles that dig holes, move towards the apple, eat it, and then vanish by digging another hole.

- Added another interactive element to the game with unique behaviors.

## 16. Adding Additional Features

**Prompt:**
Play rat_squeak.mp3 when a rat is spawned, and hedgehog_squeak.mp3 when a hedgehog is spawned.

- Further enhanced the game's auditory experience by adding spawn sounds for rats and hedgehogs.

## 17. Visual Feedback on Death

**Prompt:**
Draw a wooden textured board at the center of the screen with a 'You Lost! Press Enter to replay or Esc to quit' message when the snake dies.

- Added a visual element to indicate the game over state.

## 18. High Score Tracking

**Prompt:**
Add high score tracking by saving names and scores into a CSV file and displaying high scores on the screen.

- Implemented high score tracking and display.

## 19. User Input for Name

**Prompt:**
Before the game begins, on the wooden_texture board, take the user name as input.

- Added functionality to capture the user's name before starting the game.

## 20. Instruction Screen

**Prompt:**
Create an instruction screen that explains the game mechanics and controls.

- Implemented an instruction screen with detailed descriptions and images of the game elements.

## 21. Difficulty Level Selection

**Prompt:**
Add a difficulty level selection screen after the user name screen. Easy, medium, difficult. On easy, everything is at 50% speed. On medium, 75% speed. On difficult, 100% speed. On the wooden board, just like user name screen, Add text "SELECT DIFFICULTY" And then below it, Give 3 buttons (easy, medium, difficult) in a horizontal arrangement, and proceed to game once selected. Easy button is green. Medium is yellow. Difficult is red.

- Implemented a difficulty selection screen to set game speed based on the chosen difficulty level.

## Summary

1. **Initialize Project:** Create a basic snake game.
2. **Enhance Visuals:** Add 3D effects, shadows, detailed features for the snake, apple, and background.
3. **Introduce New Elements:** Add rats, hedgehogs, and moles with specific behaviors and interactions.
4. **Add Sound Effects:** Enhance the game with sounds for different actions and events.
5. **Modularize Code:** Split the code into meaningful modules for better structure.
6. **Add High Score Tracking:** Implement high score tracking and display.
7. **User Input and Instructions:** Add user input for the name, create an instruction screen, and implement difficulty level selection.
8. **Documentation:** Create a comprehensive README for the project.

By following these steps and prompts, the game evolved from a simple snake game to a feature-rich, visually appealing, and interactive project.