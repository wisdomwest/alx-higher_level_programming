#!/usr/bin/python3
import sys

if __name__ == "__main__":
    number = sys.argv[1:]
    sum = 0

    for i in number:
        sum += int(i)

    print(sum)
