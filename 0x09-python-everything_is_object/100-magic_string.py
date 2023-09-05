#!/usr/bin/python3
def magic_string():
    magic_string.n = 0
    magic_string.n += 1
    return "BestSchool" + ", BestSchool" * (magic_string.n - 1) + "\n"
