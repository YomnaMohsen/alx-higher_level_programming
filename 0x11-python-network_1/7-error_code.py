#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response.
If the HTTP status code is >=400, print: Error code: by the value of the
HTTP status code"""

if __name__ == "__main__":
    import requests
    import sys
    res = requests.get(sys.argv[1])
    if (res.status_code >= 400):
        print("Error code: ", res.status_code)
    else:
        print(res.text)
