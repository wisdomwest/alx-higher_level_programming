#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = []
    for item in my_list:
        if item == search:
            n_list.append(replace)
        else:
            n_list.append(item)
    return n_list
