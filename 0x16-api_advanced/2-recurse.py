#!/usr/bin/python3
"""
Module that interacts with the python API
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Makes recursive call to reddit API
    Returns list containing title of 
    all hot articles of a subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/new.json"
    headers = {
        "User-Agent": "Custom User"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        return None