#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id, must use Basic Authentication
with a personal access token as password to access to
your information (only read:user permission is needed)
"""

if __name__ == "__main__":
    import requests
    import sys
    # we can use HTTPBasicAuth from requests.auth
    head = {"Accept": "application/vnd.github+json",
            "Authorization": "Bearer {}".format(sys.argv[2]),
            "X-GitHub-Api-Version": "2022-11-28"
            }
    url = "https://api.github.com/user"
    res = requests.get(url, headers=head)
    print(res.json().get("id"))
