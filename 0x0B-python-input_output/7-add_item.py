#!/usr/bin/python3
"""
script that adds args to a python list
and then saves into a  file
"""


from sys import argv

savejs = __import__('5-save_to_json_file').save_to_json_file
loadjs = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"

try:
    json_list = loadjs(filename)

except:
    json_list = []

for args in argv[1:]:
    json_list.append(args)

savejs(json_list, filename)
