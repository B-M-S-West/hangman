# test word
word ='apple'
# function that asks for the user input and checks its a single letter
def ask_for_input():
    while True:
        guess = input('Guess a single letter: ')
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
# function to check to see if user guess is in the word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')

ask_for_input()