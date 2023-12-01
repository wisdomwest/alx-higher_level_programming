#!/usr/bin/python3
"""search in jsson"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    search = {"q": letter}
    r = requests.post("http://0.0.0.0:5000/search_user", data=search)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
