#!/usr/bin/python3
"""
Classs to show inheritance
"""
class MyList(list):
    """
    subclass that inherits from list
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
