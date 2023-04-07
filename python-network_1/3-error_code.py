#!/usr/bin/python3
"""I documented you"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import sys

if __name__ == '__main__':
    """"Documented"""
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as res:
            content = res.read()
            print("{}".format(content.decode("utf-8")))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
    except URLError as e:
        print(e.reason)
