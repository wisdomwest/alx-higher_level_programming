#!/usr/bin/python3
"""display value of x-request-id"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        print(res.headers.get("X-Request-Id"))
