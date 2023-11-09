#!/usr/bin/python3
"""
Module that interacts with the Reddit Api
"""


import requests


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers of a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Custom User"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    return res.json().get("data").get("subscribers")
