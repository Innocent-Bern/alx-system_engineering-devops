#!/usr/bin/python3
"""
module that interacts with JSON server
"""


import json
import requests
from sys import argv


if __name__ == '__main__':
    todos_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos'
    todos_res = requests.get(todos_url)
    user_url = f'https://jsonplaceholder.typicode.com/users/{argv[1]}/'
    user_res = requests.get(user_url)

    user = json.loads(user_res.content)
    todos = json.loads(todos_res.content)

    uid = user.get('id')
    u_name = user.get('username')
    t_array = []

    for item in todos:
        title = item.get('title')
        status = item.get('completed')
        t_array.append({"task": title, "completed": status, "username": u_name})

    with open(f"{uid}.json", "w") as outfile:
        json.dump({uid: t_array}, outfile)
