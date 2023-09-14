#!/usr/bin/python3
"""contains the class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure 
    (list, dictionary, string, integer and boolean."""
    return obj.__dict__
