# Liam Toebbe
# Nov. 6 2023

# generate number between 1 and 100
# prompt user for guess
# print hint after each guess
# if they get it, print win statement
# repeat for 3 total games
# report on regularity of success

import random
import math


def generate_number():
    random_number = random.randint(1, 100)
    return int(random_number)


def user_guess():
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
        counter = counter + 1
        if int(guess) == random_number:
            print("you got it!")
            break
        elif 1 < (abs(int(guess)) - random_number) <= 5:
            print("your blood is boiling and your hair is on fire")
        elif 5 < (abs(int(guess)) - random_number) <= 25:
            print("you have a pretty bad sunburn")
        elif 25 < (abs(int(guess)) - random_number) <= 50:
            print("you are the exact average temperature of a healthy human at rest")
        elif 50 < (abs(int(guess)) - random_number) <= 75:
            print("your teeth are chattering and you can't feel your toes")
        elif 75 < (abs(int(guess)) - random_number) <= 100:
            print("you have stage 3 hypothermia")
    print("it took you", counter, "tries to guess the number.")


main()
