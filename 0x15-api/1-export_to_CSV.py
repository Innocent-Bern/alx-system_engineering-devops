#!/usr/bin/python3
"""
module that interacts with JSON server
"""


import csv
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

    name = user.get('username')
    uid = user.get('id')
    with open(f'{uid}.csv', 'w', newline='') as csvfile:
        c_w = csv.writer(csvfile, delimiter=',', quotechar='"',
                         quoting=csv.QUOTE_ALL)
        for item in todos:
            c_w.writerow([uid, name, item.get('completed'), item.get('title')])
