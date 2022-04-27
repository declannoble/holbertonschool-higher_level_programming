#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
            convert = ord(i) - 32
            i = chr(convert)
        print(i, end="")

    print()
