#!/usr/bin/python3
"""
script to take in url/email address as an arg and send POST
request with email as a parameter and display response body
"""
import requests
from sys import argv
if __name__ == "__main__":
    values = {'email': argv[2]}
    req = requests.post(argv[1], values)
    print(req.text)
