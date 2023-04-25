#!/usr/bin/python3
"""I documented you"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = sys.argv[2]
    res = requests.post(url, data={"email": value})
    print("{}".format(res.text))
