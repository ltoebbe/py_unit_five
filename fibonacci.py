
"""
Ex. fibonacci(5) returns "1 1 2 3 5 "
:param number: The number of Fibonacci terms to return
:return: A string consisting of a number of terms of the Fibonacci sequence.
"""


def fibonacci(number):
    test = ""
    number = input("how many digits of the fibonacci sequence would you like to calculate? ")
    for x in range(number):
        test += str(x)
    print()
