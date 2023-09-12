#!/usr/bin/python3

"""
This Contains the lookup function that returs the attributes and methods 
of an object
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
