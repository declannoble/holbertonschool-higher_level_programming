#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [idx if idx != search else replace for idx in my_list]
    return new_list
