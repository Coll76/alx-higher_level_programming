#!/usr/bin/python3
"""
hfkhjkrkvj
"""


def append_after(filename="", search_string="", new_string=""):
    """
    gtydfjhf
    """
    with open(filename, 'r') as file, open('temp_file', 'w') as temp_file:
        for line in file:
            temp_file.write(line)
            if search_string in line:
                temp_file.write(new_string + '\n')
    with open('temp_file', 'r') as temp_file, open(filename, 'w') as final_file:
        for line in temp_file:
            final_file.write(line)
