#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly
JSON formatted and not empty, display the
id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty"""

if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    res = requests.post(url, data={"q": q})
    try:
        response_json = res.json()
        if (response_json):
            print("[{}] {}".format(response_json.get("id"),
                                   response_json.get("name")))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
