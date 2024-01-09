#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > len(my_list):
        return my_list.copy()
    if idx < len(my_list):
        if idx < 0:
            return my_list.copy()
        else:
            modified_list = my_list.copy()
            modified_list[idx] = element
            return modified_list
