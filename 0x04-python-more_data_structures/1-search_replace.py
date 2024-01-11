#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ne_list = [replace if i == search else i for i in my_list]
    return ne_list
