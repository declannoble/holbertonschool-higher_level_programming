#!/usr/bin/python3
"""script to take take letter as arg and send POST request to url provided """
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_dict = req.json()
        if len(json_dict.keys()) > 0:
            print("[{:}] {:}".format(json_dict.get('id'), json_dict.get(
                'name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
