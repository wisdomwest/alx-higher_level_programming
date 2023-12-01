#!/usr/bin/python3
"""use github api to show github id"""
import sys
import requests

if __name__ == "__main__":
    cred = (sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=cred)
    print(r.json().get("id"))
