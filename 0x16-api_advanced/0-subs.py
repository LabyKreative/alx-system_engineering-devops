#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.
"""
import requests
from requests import get


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers on a given subreddit."""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "Google Chrome Version 115.0.5790.171"}
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get("data").get("subscribers")

    except Exception:
        return 0
