#!/usr/bin/python3
"""Fetches https://alu-intranet.hbtn.io/status using urllib"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://alu-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as r:
        body = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
