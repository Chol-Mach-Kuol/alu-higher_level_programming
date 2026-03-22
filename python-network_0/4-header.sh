#!/bin/bash
# Sends a GET request with header X-HolbertonSchool-User-Id set to 98 and displays the body
curl -s -H "X-School-User-Id: 98" "$1"
