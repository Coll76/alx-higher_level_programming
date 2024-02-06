#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    parameter:
        filename = stands for the name of the file
    """
    with open(filename, 'r', encoding='UTF-8') as file_n:
        fil = file_n.read()
        print(fil, end='')
