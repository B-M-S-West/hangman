# Hangman

## Table of Contents
1. Project Description
2. Installation Instructions
3. Usage Instructions
4. File Structure
5. License Information

## Project Description
Hangman is a classic word guessing game. This project is a Python implementation of the game. The aim of this project is to provide a fun and interactive way to play Hangman in the console. The game starts with a default number of lives and a random word from a provided list. The user guesses one letter at a time, with the goal of guessing the entire word. This project helped me learn about handling user input, working with strings and lists, and structuring a program using classes and methods.

## Installation Instructions
To install and run this project:

1. Clone the repository or download the files.
2. Ensure you have Python installed on your machine.
3. Run the script using a Python interpreter.
4. To run the script write 'python milestone_5.py' in the command line

## Usage Instructions
To play the game:

1. Run the script.
2. When prompted, enter a single letter to guess a letter in the word.
3. Continue guessing letters until you've guessed the entire word or you've run out of lives.

## File Structure
The project has the following structure:
- `README.md`: This is the readme file that explains everything to do with this repo
- `milestone_2.py`: Initial script that looked at picking a word randomly from a list and taking a user input for the letter
- `milestone_3.py`: This script moved on to creating the functions for the user guess and establishing if it was correct, a single letter. It also included the first version of the function for checking the guess.
- `milestone_4.py`: This script moved on to then set up the class and include the function to set up the attributes for the game.
- `milestone_5.py`: This is the main Python script that you run to play the game. It contains the Hangman class and the logic for running the game. It builds on the previous milestones to combine functions in the `Hangman` class. This includes `__init__` which sets up the attributes for the gam, `check_guess` to see if the letter that has been guessed is in the word, `ask_for_input` this asks for the users input and checks it is a single letter. The function `play_game` is then set which runs the game and will determine if the player loses or wins. The final if statement allows the game to run when the `milestone_5.py`  is run in the command line. The `word_list` parameter can be adjust before playing to change the words that might be selected in the game.

## License Information
This project is licensed under the MIT License. See the LICENSE file for details.
