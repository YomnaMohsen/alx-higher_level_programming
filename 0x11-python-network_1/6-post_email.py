#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response"""

if __name__ == "__main__":
    import requests
    import sys
    email = sys.argv[2]
    r = requests.post(sys.argv[1], email)
    