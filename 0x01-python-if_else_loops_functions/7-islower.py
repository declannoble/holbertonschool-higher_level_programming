#!/usr/bin/python3
def islower(c):
    result = ord(c)
    if result > 96 and result < 123:
        return 1
    else:
        return 0
