#!/usr/bin/python3
"""I documented you"""
import requests
import requests.auth
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    res = requests.get(
        url="https://api.github.com/user",
        auth=(requests.auth.HTTPBasicAuth(
            username,
            password
        )))
    try:
        json_response = res.json()
        print("{}".format(json_response["id"]))
    except:
        print(None)
