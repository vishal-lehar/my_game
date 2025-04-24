# My Bowling Game

This project implements a **Bowling Game** scoring system in Python. It includes a `BowlingGame` class to calculate scores based on rolls and a comprehensive test suite to ensure correctness of the implementation logic.

## Features

The challenge is to implement a **BowlingGame module** that calculates the score of a bowling game according to standard bowling rules:

- A game consists of 10 frames
- In each frame, a player has up to two rolls to knock down 10 pins
- If a player knocks down all 10 pins in two rolls, it's a spare (/)
- If a player knocks down all 10 pins on the first roll, it's a strike (X)
- The score for a frame is the total pins knocked down plus bonuses for strikes and spares
- A spare bonus adds the value of the next roll
- A strike bonus adds the value of the next two rolls
- In the 10th frame, a player can roll up to 3 times if they get a strike or spare

## Project Structure
```
my_game/
├── README.md
├── bowling_game.py
└── test_bowling_game.py
```
## Requirements
- Python 3.7 or higher
- `unittest` (built-in Python module)

## Usage

### Running the Tests

To run the test suite, follow the steps below: 
1. clone the Repo
2. go to the project directory
3. run the unittests
4. Verify results on console

Execute the following commands in the terminal:

```bash
git clone <repository-url>
cd my_game
python -m unittest test_bowling_game.py
```

## Tests Included
The test suite `test_bowling_game.py` includes the following test cases:

1. Gutter Game: All rolls knock down 0 pins.
2. All Ones: All rolls knock down 1 pin.
3. One Spare: A spare followed by a roll.
4. One Strike: A strike followed by two rolls.
5. Perfect Game: All rolls are strikes.
6. Incomplete Game: Ensures an error is raised for incomplete games.
7. Invalid Pins: Ensures an error is raised for invalid pin counts.
8. Example Score Card: Tests a sample scorecard with mixed rolls.