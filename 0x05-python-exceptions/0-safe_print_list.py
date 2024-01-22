#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list[:x]:
            print("{}".format(i), end='')
        print()
        return x
    except Exception as e:
        print("An error occurred")
