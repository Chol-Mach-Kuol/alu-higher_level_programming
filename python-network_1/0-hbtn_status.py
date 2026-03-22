#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status and displays body"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as r:
        body = r.read()
        print("Body response:")
        print("    - type: {}".format(type(body)))
        print("    - content: {}".format(body))
        print("    - utf8 content: {}".format(body.decode('utf-8')))
