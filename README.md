# snake-game
Customizable Python Snake is a modern take on the classic arcade game, developed using the pygame library.

# Customizable Python Snake Game

A classic Snake Game built with **Pygame** that allows users to define their own board dimensions and game speed. Features include real-time scoring, a pause system, and a responsive UI that centers itself regardless of screen size.

## 🚀 Features

* **Customizable Setup:** Choose your own width, height, and snake velocity via the console before starting.
* **Pause Functionality:** Press `P` at any time to freeze the game and take a break.
* **Dynamic UI:** Game messages and the "Game Over" screen are automatically centered based on your chosen resolution.
* **Score Tracking:** Real-time score display based on the length of the snake.
* **Collision Detection:** Standard rules apply—hitting the walls or your own tail results in a Game Over.

## 🛠️ Installation

### Prerequisites
* **Python 3.x**
* **Pygame library**

### Setup
1. Clone this repository or download the source code:
   ```bash
   git clone [https://github.com/yourusername/snake-game-pygame.git](https://github.com/yourusername/snake-game-pygame.git)
Navigate to the project folder:

2. Navigate to fole1
   cd snake-game-pygame

3. Install the required dependency:
   pip install pygame

## 🎮 How to Play
Run the script:

python snake.py
Follow the prompts in your terminal to set the Width, Height, and Speed.

Use the Arrow Keys to move the snake.

Eat the Green Blocks to grow and increase your score.

Controls
Key	Action
↑ ↓ ← →	Move Snake
P	Pause / Unpause
C	Play Again (after Game Over)
Q	Quit Game

## 🏗️ Code Structure
pygame.init(): Initializes all sub-modules (including font and sound).

gameLoop(): The core logic containing the event handler, movement updates, and collision checks.

message(): A smart centering function using get_rect() to position text perfectly.

clock.tick(): Controls the frame rate based on the user's speed input.

## 📜 License
This project is open-source and available under the MIT License.
