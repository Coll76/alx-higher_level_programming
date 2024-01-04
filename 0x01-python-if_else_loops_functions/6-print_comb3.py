#!/usr/bin/python3
for num1 in range(0, 9 + 1):
    for num2 in range(0, 8 + 1):
        if (num2 == 0):
            print("{}{}, ".format(num2, num1), end='')
            pass
        elif (num2 > 0):
            print("{}{}".format(num2, num1), end=(", " if num2 < 8 else "\n"))
