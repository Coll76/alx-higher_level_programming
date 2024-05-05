#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
"""


def find_peak(list_of_integers):
    """
    Parameters:
        list_of_integers - represents the list containing
        integers
    """
    lists = []
    """
    if not list_of_integers:
        print("None")
    """

    for n in range(len(list_of_integers)):
        if list_of_integers[n] > list_of_integers[n + 1] and list_of_integers[n] > list_of_integers[n - 1]:
            a_list = lists.append(list_of_integers[n])
            return a_list
        if list_of_integers[n] == 0 and list_of_integers[n] > list_of_integers[n + 1]:
            a_list = lists.append(list_of_integers[n])
            return a_list
