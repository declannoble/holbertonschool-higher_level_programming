#!/usr/bin/python3
"""script to take in URL as an arg and display value of variable in response"""
import requests
from sys import argv
if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get('X-request-id'))
