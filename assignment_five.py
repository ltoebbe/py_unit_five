# Liam Toebbe
# Nov. 6 2023

import random
import math


def generate_number():                                                                      # determines the number the user has to guess
    random_number = random.randint(1, 100)
    return int(random_number)


def user_guess():                                                                           # asks user to input a guess between 1 and 100
    guess = input("guess a number between 1 and 100: ")
    return guess


print("let's play a game of hot and cold!")
print("Try to guess a number between 1 and 100. I'll give you hints after each guess.")
print("'Warmer' means you're closer, 'colder' means you're farther away.")


def main():
    random_number = generate_number()
    counter = 0
    while True:
        guess = user_guess()
        absolute_value = abs(int(guess) - random_number)                                    # determines how far away the guess is from the answer
        counter = counter + 1                                                               # keeps track of every try by adding 1 each loop
        if int(guess) == random_number:                                                     # if the guess is correct, print a win statement
            print("you got it!")
            break                                                                           # if the guess is correct stop the loop
        elif 0 < absolute_value and absolute_value <= 5:                                    # if the guess is within 5 of the answer, print appropriate hint
            print("your blood is boiling and your hair is on fire")
        elif 5 < absolute_value and absolute_value <= 25:                                   # if the guess is within 6-25 of the answer, print appropriate hint
            print("you have a pretty bad sunburn")
        elif 25 < absolute_value and absolute_value <= 50:                                  # if the guess is within 26-50 of the answer, print appropriate hint
            print("you are the exact average temperature of a healthy human at rest")
        elif 50 < absolute_value and absolute_value <= 75:                                  # if the guess is within 51-75 of the answer, print the appropriate hint
            print("your teeth are chattering and you can't feel your toes")
        elif 75 < absolute_value and absolute_value <= 100:                                 # if the guess is within 76-100 of the answer, print the appropriate hint
            print("you have stage 3 hypothermia")
    print("it took you", counter, "tries to guess the number.")                             # once the answer is guessed, print how many guesses it took


main()
