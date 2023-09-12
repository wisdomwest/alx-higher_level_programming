#!/usr/bin/python3
"""
adds arguments to Python list and save to file
"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

f = "add_item.json"

try:
    jlist = load_from_json_file(f)
except FileNotFoundError:
    jlist = []

for arg in argv[1:]:
    jlist.append(arg)

save_to_json_file(jlist, f)
