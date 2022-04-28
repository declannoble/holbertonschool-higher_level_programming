#!/usr/bin/python3
import sys

if __name__ == "__main__":

    ac = len(sys.argv)
    result = 0

    for i in range(1, ac):
        result += int(sys.argv[i])

    print(result)
