#!/usr/bin/python3

"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

response = requests.get("http://intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
