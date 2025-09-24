import subprocess
import json

# Define sample tasks and workflows
tasks = [
    {"id": 0, "task_type": "primitive"},
    {"id": 1, "tasks": [0], "task_type": "workflow"},
]

executions = [
    {"workflow_id": 1, "input": "Ma liberté de penser"},
]

# Convert tasks and executions to JSON strings
tasks_json = json.dumps(tasks)
executions_json = json.dumps(executions)

# Execute the Python script with sample inputs
process = subprocess.Popen(['/usr/bin/python3', 'flowrent_pagny.py', tasks_json, executions_json], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()

# Print the output and error (if any)
print("Output:")
print(output.decode())
print("Error:")
print(error.decode())