#!/usr/bin/python3
"""Module contains read_file function"""


def read_file(filename=""):
    """""reads file prints to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
