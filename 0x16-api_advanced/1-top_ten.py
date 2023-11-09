#!/usr/bin/python3
"""
Module that interacts with the reddit api
"""

import requests


def top_ten(subreddit):
    """
    prints titles of the first 10 hot posts
    """

    url = f"https://www.reddit.com/r/{subreddit}/new.json"
    headers = {
        "User-Agent": "Custom User"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 404:
        print(None)

    hot_posts = res.json().get("data").get("children")

    for item in hot_posts:
        print(item.get("data").get("title"))
