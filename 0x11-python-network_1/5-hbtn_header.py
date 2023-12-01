#!/usr/bin/python3
"""get header value"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    header = r.headers.get("X-Request-Id")
    print(header)
