#!/usr/bin/python3
"""Fetch employee todo list and expoet to csv"""
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetch employee todo list details and display the TODO
    list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Check if the user exists
    if not user_data:
        print(f"No employee found with ID {employee_id}")
        return

    # Fetch todos for the employee
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(url)
    todos_data = todos_response.json()

    # Calculate the total number of tasks and completed tasks
    tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    num_of_done_tasks = len(completed_tasks)

    # Display the employee's TODOlist progress
    name = user_data['name']
    print(f"Employee {name} is done with tasks({num_of_done_tasks}/{tasks}): ")

    # Display the titles of the completed tasks
    for task in completed_tasks:
        print(f"\t {task['title']}")


# Accept employee ID as a command-line argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
