# **Snake Game in Python with Turtle Graphics**

## **Introduction**
This project is a classic Snake game implemented in Python using the Turtle graphics library. The Snake game is a simple yet entertaining game where the player controls a snake, trying to eat food and grow in length while avoiding collisions with the boundaries of the game and the snake's own tail. The game keeps track of the player's score and their high score.

## **Features**
1. **Snake Movement:** The snake can be controlled using the arrow keys: Up, Down, Left, and Right. The snake moves in the direction specified by the player.

2. **Food:** Food items appear on the screen as blue circles. The player's goal is to guide the snake to eat the food. When the snake eats food, it grows in length, and the player's score increases.

3. **Collision Detection:** The game detects collisions in three ways:
   - Collision with the wall boundaries: If the snake hits the wall, the game resets, and the player's score is reset.
   - Collision with the snake's own tail: If the snake collides with its own body, the game resets, and the player's score is reset.
   - Collision with food: When the snake eats food, the player's score increases, and new food spawns in a random location.

4. **Score Tracking:** The game keeps track of the player's score and their high score. The current score is displayed on the screen along with the high score.

## **High Score Persistence**
The game keeps track of the player's high score, ensuring that it is saved even if the program is closed and run again later. When you achieve a new high score, it will be stored and loaded the next time you play the game. This feature adds an extra layer of motivation for players to beat their previous high scores and provides a sense of accomplishment.

## **How to Play**
1. Use the arrow keys (Up, Down, Left, Right) to control the snake's movement.
2. Guide the snake to eat the blue food items that appear on the screen.
3. Avoid colliding with the wall boundaries and the snake's own tail.
4. Try to achieve the highest score possible.

## **Files**
- `main.py`: Contains the game's main logic, including the game loop and user input handling.
- `snake.py`: Defines the Snake class and its methods for managing the snake's behavior.
- `food.py`: Defines the Food class responsible for the appearance and refreshment of food items.
- `scoreboard.py`: Implements the Scoreboard class for tracking and displaying the player's score.
- `high_score.txt`: A text file used to store the player's high score.
- `README.md`: This documentation file.

## **Installation**
1. Make sure you have Python installed on your system.
2. Clone the repository to your local machine.
3. Run `main.py` to start the Snake game.

## **Acknowledgments**
- This project uses the Turtle graphics library for Python, which is a standard library for drawing graphics and creating simple games.
- Inspired by classic Snake games and various online tutorials.

## **Contributions**
Contributions to this project are welcome. Feel free to fork the repository, make improvements, and submit pull requests.

Enjoy playing the Snake game! If you encounter any issues or have suggestions for improvements, please don't hesitate to create an issue or contribute.
