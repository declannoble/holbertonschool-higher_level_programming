#!/usr/bin/python3
"""script to display value of variable in header"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as r:
        r = r.headers.get('X-Request-Id')
        print(r)
