#!/usr/bin/python3
"""I documented you"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print("{}".format(res.text))
