#!/usr/bin/python3
"""mangaed error HTTPERROR exception when send request to URL"""

if __name__ == "__main__":
    import urllib.request as req
    import sys
    import urllib.error.HTTPError as err
    try:
        with req.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except err:
        print("Error code: {}".format(err.code))
