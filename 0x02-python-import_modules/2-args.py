#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    ac = len(sys.argv)

    if ac == 1:
        print("0 arguments.")

    elif ac == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))

    else:
        print("{} arguments:".format(ac - 1))

        for ac in range(1, ac):
            print("{}: {}".format(ac, sys.argv[ac]))
