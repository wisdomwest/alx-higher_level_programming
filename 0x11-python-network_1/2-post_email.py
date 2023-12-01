#!/usr/bin/python3
"""send post req with email"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        page = res.read().decode("utf-8")
        print(page)
