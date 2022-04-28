#!/usr/bin/python3

import sys
if __name__ == "__main__":

    result = 0
    ac = len(sys.argv)

    for i in range(1, ac):
        result = result + int(sys.argv[i])

        print(result)
