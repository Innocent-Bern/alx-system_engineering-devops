#!/usr/bin/python3
"""
module that interacts with JSON server
"""


import json
import requests


if __name__ == '__main__':
    user_dict = {}

    def add_to_dict(uid, name):
        """add items to a dictionary"""
        todos_url = f'https://jsonplaceholder.typicode.com/users/{uid}/todos'
        todos_res = requests.get(todos_url)
        user_url = f'https://jsonplaceholder.typicode.com/users/{uid}/'
        user_res = requests.get(user_url)

        user = json.loads(user_res.content)
        todos = json.loads(todos_res.content)

        arr = []
        for item in todos:
            title = item.get('title')
            status = item.get('completed')
            arr.append({"username": name, "task": title, "completed": status})

        user_dict.update({uid: arr})

    users_url = "https://jsonplaceholder.typicode.com/users/"
    users_res = requests.get(users_url)
    users = json.loads(users_res.content)

    for item in users:
        add_to_dict(item.get('id'), item.get('username'))

    with open(f"todo_all_employees.json", "w") as outfile:
        json.dump(user_dict, outfile)
