#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = len(sys.argv)

    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{count - 1} arguments:")
        for i in range(1, count):
            print(f"{i}: {sys.argv[i]}")
