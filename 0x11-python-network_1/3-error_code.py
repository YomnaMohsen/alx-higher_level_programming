#!/usr/bin/python3
"""managed error HTTPERROR exception when send request to URL"""

if __name__ == "__main__":
    import urllib.request as req
    import sys
    from urllib.error import HTTPError
    try:
        with req.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code:", e.code)
