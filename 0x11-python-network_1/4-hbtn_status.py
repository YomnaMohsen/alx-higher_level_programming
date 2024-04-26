#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status 
using requests package"""

if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status "
    resp = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
