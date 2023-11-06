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


def guess():
    input("guess a number between 1 and 100: ")

print("let's play a game of hot and cold!"
          "Try to guess a number between 1 and 100. I'll give you hints after each guess."
          "'Warmer' means you're closer, 'colder' means you're farther away.")


def main():
    random_number = generate_number()
    counter = 0
    while True:
        guess()
        counter = counter + 1
        if int(guess()) == random_number:
            print("you got it!")
        elif int(guess()) ==
