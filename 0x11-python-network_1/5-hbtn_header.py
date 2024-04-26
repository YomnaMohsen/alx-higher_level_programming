#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable
found in the header of the response."""

if __name__ == "__main__":
    import requests
    import sys
    print(requests.get(sys.argv[1]).headers["X-Request-Id"])
