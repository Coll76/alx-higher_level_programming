#!/usr/bin/python3
def no_c(my_string):
    modified_str = ''
    for ch in my_string:
        if ch.lower() != 'c':
            modified_str += ch
    return modified_str
