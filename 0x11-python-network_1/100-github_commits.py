#!/usr/bin/python3
"""list the latest 10 commits by certain user and repository"""


if __name__ == "__main__":
    import requests
    import sys
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    res = requests.get(url)
    # res.json() is a list of dictionaries
    for commit in res.json()[:10]:
        print(commit.get("sha"), end=": ")
        print(commit.get("commit").get("author").get("name"))
