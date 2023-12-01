#!/usr/bin/python3
""""get commits and names"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    data = r.json()
    for i in range(10):
        print("{}: {}".format(
            data[i].get("sha"),
            data[i].get("commit").get("author").get("name")))
