# import the random package
import random

# create word list containing 5 different fruits
word_list = ["apple", "banana", "orange", "lemon", "lime"]
# select one of the words at random from the list
word = random.choice(word_list)
# user input of 1 letter
guess = input('Enter a single letter: ')
# if statement to check if user input is correct
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input")

print(word_list)
print(word)