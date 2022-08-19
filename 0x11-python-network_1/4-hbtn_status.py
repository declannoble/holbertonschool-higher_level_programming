#!/usr/bin/python3
"""script to fetch url and display response body """
import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t content: {}".format(r.text))
