#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        element = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if a_dictionary[key] == element:
                return key