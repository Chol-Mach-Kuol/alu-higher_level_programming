#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            result += "{:c}".format(ord(c) - 32)
        else:
            result += "{:c}".format(ord(c))
    print("{}".format(result))
