#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if (number < 0):
    number = number * -1
    print(f"Last digit of -{number} is -{number % 10} and is less than 6 and not 0")
    pass
elif ((number % 10) > 5):
    print(f"Last digit of {number} is {number % 10} and is greater than 5")
elif ((number % 10) == 0):
    print(f"Last digit of {number} is {number % 10} and is 0")
elif (((number % 10) < 6) and ((number % 10) != 0)):
    print(f"Last digit of {number} is {number % 10} and is less than 6 and not 0")
