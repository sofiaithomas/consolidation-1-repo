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
