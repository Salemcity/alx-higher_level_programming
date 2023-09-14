#!/usr/bin/python3
"""Defining a Json file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using json representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

