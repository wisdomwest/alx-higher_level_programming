#!/usr/bin/python3
module = __import__("add_0")

a = 1
b = 2
print("{} + {} = {}".format(a, b, module.add(a, b)))
