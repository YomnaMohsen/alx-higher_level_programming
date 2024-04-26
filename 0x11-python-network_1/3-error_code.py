#!/usr/bin/python3
"""mangaed error HTTPERROR exception when send request to URL"""

if __name__ == "__main__":
    import urllib.request as req
    import sys
    from urllib import error
    try:
        with req.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code:", e.code)
