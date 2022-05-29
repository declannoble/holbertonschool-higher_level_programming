#!/usr/bin/python3
"A module that defines a class named MyList"


class MyList(list):
    """A class named MyList
    """
    def print_sorted(self):
        """Prints instance"""
        print(sorted(self))
