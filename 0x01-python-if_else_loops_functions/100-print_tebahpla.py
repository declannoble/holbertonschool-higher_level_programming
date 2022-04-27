#!/usr/bin/python3

for result in reversed(range(97, 123)):
    if result % 2 != 0:
        result = result - 32
    print(chr(result), end="")
