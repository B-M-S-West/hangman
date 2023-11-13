import random


class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__ (self, word_list, num_lives=5):
        '''
        This initialises the atrributes 
        '''
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.word_list = word_list    
        self.num_lives = num_lives
        self.list_of_guesses = []
    
     
    def check_guess(self, guess):
        '''
        This checks to see if the letter that has been guessed is in the word.
        If the letter is a correct guess then '_' is replaced by the letter in the word_guessed list.
        If not, the number of lives is reduced to reflect this.

        Parameters:
        ----------
        guess: str
            The letter that has been guessed to be checked.
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} lives left')
    

    def ask_for_input(self):
        '''
        Asks a letter to be input by the user and then performs the following two checks:
        1 - If the character entered is a single character
        2 - If the letter has already been guessed
        If both of these checks are passed, it calls the check_guess method.
        '''
        while True:
            guess = input('Guess a single letter: ')
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.word_guessed)
            if self.num_lives == 0 or self.num_letters == 0:
                break
    

def play_game(word_list):
    '''
    This initialises the game with the word_list that has been created and sets the number of lives.
    Once the first guess has been had it will then keep checking to see if the game continues or if it has been won or lost.
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break


if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
