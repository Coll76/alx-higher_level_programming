#!/usr/bin/python3
for numbers in range(0, 99 + 1):
    if (numbers < 10):
        print("0{}, ".format(numbers), end='')
        pass
    elif (numbers >= 10):
        print("{}".format(numbers), end=(', ' if numbers < 99 else "\n"))
