#!/usr/bin/python3
"""
.Using what you did in the task #0, extend your Python script to export
data in the JSON format.
Requirements:
Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
"TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID":
[ {"username": "USERNAME", "task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json.
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(
            {
                user.get("id"): [
                    {
                        "task": tsk.get("title"),
                        "completed": tsk.get("completed"),
                        "username": user.get("username")
                    }
                    for tsk in requests.get(
                        url + "todos",
                        params={"userId": user.get("id")}
                    ).json()
                ]
                for user in users
            },
            jsonfile
        )
