#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
        for keys, values in sorted(a_dictionary.items()):
            print("{}: {}".format(keys, values))
    if key not in a_dictionary:
        a_dictionary[key] = value
        for keys, values in sorted(a_dictionary.items()):
            print("{}: {}".format(keys, values))
