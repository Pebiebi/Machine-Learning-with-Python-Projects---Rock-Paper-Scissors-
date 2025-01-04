# Machine-Learning-with-Python-Projects---Rock-Paper-Scissors-

# Rock, Paper, Scissors - Machine Learning Project

## Project Overview
This project is a Python-based implementation of the **Rock, Paper, Scissors** game, where the goal is to create a program (Player 1) that can compete against four different bots and win at least **60% of the games** against each bot. The program utilizes a strategy to predict the opponent's next move and responds with the optimal counter-move to maximize the chances of winning.

## Project Objective
The objective of this project is to develop an intelligent strategy for **Player 1** (the program you create) to win a significant percentage of games (at least 60%) against each bot. The program must analyze the opponent’s previous moves and choose a move that will maximize its chances of winning.

## Requirements
- Python 3.x
- `RPS_game.py`: Contains the bot implementations and the main game logic.
- `RPS.py`: Where you implement the strategy for **Player 1**.
- `test_module.py`: Includes unit tests to verify the program’s correctness.

## Game Description
In the **Rock, Paper, Scissors** game, each player picks one of three moves:
- **Rock (R)**
- **Paper (P)**
- **Scissors (S)**

The rules of the game are:
- Rock beats Scissors.
- Scissors beats Paper.
- Paper beats Rock.

The objective is for **Player 1** to predict the opponent’s next move based on their previous moves and select the appropriate counter-move.

## How to Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/rock-paper-scissors.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rock-paper-scissors
   ```
3. Run the game by executing the following command:
   ```bash
   python main.py
   ```

This will simulate the game against the four bots and display the results.

## How the Program Works
### `RPS.py`
In this file, you need to implement the function `player(prev_play, opponent_history=[])`. This function:
- Tracks the opponent's previous moves.
- Chooses the best next move based on a strategy that tries to predict the opponent’s next move.
- The first move will not have an opponent history, so `prev_play` will be an empty string on the first turn.

### Strategy to Win
The strategy is to analyze the opponent's last moves and predict their next move based on observed patterns. The program then counters the predicted move:
- If the opponent played "R", then play "P" (Paper beats Rock).
- If the opponent played "P", then play "S" (Scissors beats Paper).
- If the opponent played "S", then play "R" (Rock beats Scissors).

### `main.py`
This file runs the game by importing the `player` function and the bots from `RPS_game.py`. It simulates the game between Player 1 and the bots.

### `RPS_game.py`
This file contains the bot definitions (Quincy, Abbey, Kris, Mrugesh) and the function `play()` which runs the game between two players.

### `test_module.py`
Unit tests are included in this file to ensure the correct behavior of the `player` function and the overall game logic.

## Results
After running the program, you should see the results of each match, including the number of games Player 1 won, the number of games the bot won, and the win rate. For example:

```
Final results: {'p1': 994, 'p2': 3, 'tie': 3}
Player 1 win rate: 99.7%
```

This means Player 1 (your program) won 99.7% of the games, which is well above the required **60% win rate**.

## Contribution
This project is part of a machine learning challenge, and all improvements or strategies are designed to meet the project requirements. Contributions are not necessary for submission, but improvements are welcome for future versions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

---

### Explanation:
- **Project Overview**: Briefly explains the goal of the project—creating a program that wins at least 60% of the games against four bots.
- **Project Objective**: Clarifies that the program must predict the opponent's moves and counter them effectively.
- **Requirements**: Lists dependencies and files involved in the project.
- **Game Description**: Describes how Rock, Paper, Scissors works and the rules.
- **How to Run the Project**: Provides clear instructions on how to clone the repo, navigate to the project directory, and run the game.
- **How the Program Works**: Explains how the game works, especially focusing on the `player` function and its strategy to win.
- **Strategy to Win**: Outlines the strategy for predicting and countering the opponent’s next move.
- **Results**: Describes the expected output and format after running the game.
- **Contribution**: States that contributions are not required for the task but would be appreciated in future versions.
- **License**: Indicates the licensing for the project.


