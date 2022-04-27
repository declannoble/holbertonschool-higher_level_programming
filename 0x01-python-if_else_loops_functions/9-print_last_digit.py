#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = int(repr(number)[-1])
    print(lastdigit, end="")
    return(lastdigit)
