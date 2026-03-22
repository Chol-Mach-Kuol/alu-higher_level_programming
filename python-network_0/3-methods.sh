#!/bin/bash
# Sends an OPTIONS request and displays all HTTP methods the server will accept
curl -s -X OPTIONS "$1" -I | grep "Allow:" | cut -d' ' -f2-
