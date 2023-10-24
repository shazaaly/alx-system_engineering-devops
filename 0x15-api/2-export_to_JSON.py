#!/usr/bin/python3
"""
A Python script that, using the JSONPlaceholder REST API,
returns information about an employee's TODO
list progress and saves it in a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main":

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    params = {'userId': employee_id}

    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(f"{base_url}/todos", params=params).json()

    # Create a dictionary with the employee's ID as the key
    employee_data = {employee_id: []}

    for task in todos:
        employee_data[employee_id].append({
            "task": task.get("title"),
            "completed": task.get("commpleted"),
            "username": user.get("username")})

    # Define the filename based on the employee's ID
    filename = f"{employee_id}.json"

    # Save the employee data to a JSON file
    with open(filename, "w") as file:
        json.dump(employee_data, file, indent=4)
