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
    done = 0
    for item in todos:
        if item.get('completed') is True:
            done += 1

    name = user.get('name')
    print(f"Employee {name} is done with tasks({done}/{len(todos)}):")
    for item in todos:
        if item.get('completed') is True:
            print(f"\t {item.get('title')}")
