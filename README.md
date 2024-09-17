# Rock, Paper, Scissors Game

## Overview

This Rock, Paper, Scissors game is a simple command-line application written in Python. It allows you to play against the computer following the classic rules of the game. The game features input validation, displays results, and provides an option to play multiple rounds.

## Features

- Play against the computer
- Classic Rock, Paper, Scissors rules
- Validates user input to ensure only valid choices (Rock, Paper, Scissors) are accepted
- Provides feedback on the game result and allows replay

## Installation

To run this game, you need to have Python installed on your computer. Follow these steps to set up and run the game:

## Code Overview

- **`print_welcome_message()`**: Displays the rules of the game.
- **`get_user_choice()`**: Prompts the user to choose Rock, Paper, or Scissors and validates the input to ensure it's a valid choice.
- **`get_choice_name(choice)`**: Converts the numeric choice to its string representation for display purposes.
- **`determine_winner(user_choice, comp_choice)`**: Determines the winner of the game based on the choices made by the user and the computer.
- **`play_game()`**: Manages the main game loop, handles user input, displays the results of each round, and prompts the user to play again or exit.

