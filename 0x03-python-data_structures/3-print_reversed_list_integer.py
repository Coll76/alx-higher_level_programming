#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    sortedList = sorted(my_list, reverse=True)
    for num in sortedList:
        print("{}".format(num))
