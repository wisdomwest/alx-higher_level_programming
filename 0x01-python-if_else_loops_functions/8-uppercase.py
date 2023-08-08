#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            up = chr(ord(ch) - 32)
          print("{:s}".format(up), end='')
    print('\n', end="")
