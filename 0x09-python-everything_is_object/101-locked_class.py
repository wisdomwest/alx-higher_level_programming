#!/usr/bin/python3
"""Defines locked class."""


class LockedClass:
    """Prevent the user from instantiating new LockedClass attributes"""

    __slots__ = ["first_name"]
