# Word Guessing Game Consolidation

import random

print("Hello Player! Welcome to the Word Guessing Game!")
print("Let's get started! ")
print("------------------------------------------------")
guesses_list = []

# function to choose a secret word
def choose_word():
    secret_word_bank = ["glowworm", "pneumonia", "jukebox", "zodiac", "espionage", "rhubarb"]
    return random.choice(secret_word_bank)

# function to count the number of times a guess is in the word
def count_guess_occurences(word, letter):
    '''
    This function counts the occurences of a letter guess in the secret word.
    Returns: 
    The number of times the letter is in the word
    '''
    return word.count(letter)

# function that runs the actual game
def game_time():
    secret_word = choose_word()
    letter_guesses = 0
    word_guesses = 0

    print ("The super secret word has been chosen!")
    print("------------------------------------------------")

    while True:
        guess = input("Guess a letter or a word if you are feeling bold: ")
        guess = guess.lower()
    # adding user's guesses to empty list to display what they have guessed
        guesses_list.append(guess)
    # if statement for if they guess a letter
        if len(guess) == 1:
            letter_guesses += 1
            occurences = count_guess_occurences(secret_word, guess)
            if occurences == 0:
                print("------------------------------------------------")
                print(f"Sorry, the letter {guess} is not in the secret word")
                print("So far you have guessed:")
                print(*guesses_list)
                print("------------------------------------------------")

            else:
                print("------------------------------------------------")
                print(f"Yay!!! The letter {guess} shows up {occurences} time(s) in the word")
                print("So far you have guessed:")
                print(*guesses_list)
    # elif they guessed a word
        elif guess == secret_word:
            word_guesses += 1
            print("------------------------------------------------")
            print(f"Congrats!!! You guessed the word in {letter_guesses + word_guesses} turn(s)")
            break
        else:
            word_guesses += 1
            print("------------------------------------------------")
            print("Sorry, but you guessed a wrong word :( ")
            print("So far you have guessed:")
            print(*guesses_list)
            if word_guesses == 3:
                print("------------------------------------------------")
                print(f"Sorry to break it to you but you have used up all your word guesses. The secret word was {secret_word}")
                break

game_time()