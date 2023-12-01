#!/usr/bin/python3
"""use github api to show github id"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    r = requests.get("https://api.github.com/user", auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get("id"))
