#!/usr/bin/python3
"""Sends a request and displays the X-Request-Id header value using requests"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
