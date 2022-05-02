#!/usr/bin/python3

def no_c(my_string):
    result = ""
    for idx in my_string:
        if idx != 'c' and idx != 'C':
            result = result + idx
    return (result)
