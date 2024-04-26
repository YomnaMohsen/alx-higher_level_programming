#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

if __name__ == "__main__":
    import urllib.request as req
    import sys
    import urllib.parse
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode('ascii')
    query = req.Request(url, data)
    with req.urlopen(query) as response:
        print(response.read().decode("utf-8"))
