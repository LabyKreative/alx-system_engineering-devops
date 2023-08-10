#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts on a particular subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/LabyKreative)"
    }

    data = requests.get(url, headers=header, allow_redirects=False)

    if data.status_code == 200:
        data = data.json().get("data").get("children")
        for element in data:
            print(element.get("data").get("title"))
    else:
        print(None)
