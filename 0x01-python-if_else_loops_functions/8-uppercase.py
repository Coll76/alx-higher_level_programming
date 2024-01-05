#!/usr/bin/python3
def uppercase(str):
    for upper in str:
        if upper >= 'a' and upper <= 'z':
            upper = chr(ord(upper) - 32)
            print("{}".format(upper), end='')
        else:
            print("{}".format(upper), end='')
    print("\n", end='')
