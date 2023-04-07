#!/usr/bin/python3
"""I documented you"""

from urllib.request import urlopen, Request
import urllib.parse
import sys

if __name__ == '__main__':
    """"Documented"""
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as res:
        content = res.read()
        print("{}".format(content.decode("utf-8")))
