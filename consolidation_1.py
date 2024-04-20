# Word Guessing Game Consolidation

import random

print("Hello Player! Welcome to the Word Guessing Game!")
print("Let's get started: ")
print("------------------------------------------------")

# function to choose a secret word
def choose_word():
    secret_word_bank = ["glowworm", "pneumonia", "jukebox", "zodiac", "espionage", "rhubarb"]
    return random.choice(secret_word_bank)

# function to count the number of times a guess is in the word
def count_guess_occurences(word, letter):
    return word.count(letter)

# function that runs the actual game
def game_time():
    secret_word = choose_word()
    letter_guesses = 0
    word_guesses = 0

    print ("The super secret word has been chosen!")

    while True:
        guess = input("Guess a letter or a word if you are feeling bold: ")
        guess = guess.lower()