#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable
found in the header of the response."""

if __name__ == "__main__":
    import urllib.request as req
    import sys
    with req.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-ID"))
