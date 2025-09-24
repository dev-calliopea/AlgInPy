from typing import List, Dict, Union
import json
import sys
import hashlib

def encode_input_bytes(input_bytes: bytes) -> bytes:
    """
    Encode the input bytes using MD5 hash.

    Args:
    - input_bytes: A bytes object representing the input data.

    Returns:
    - A bytes object representing the MD5 hash of the input data.
    """
    return hashlib.md5(input_bytes).digest()


def execute_task(task: Union[Dict[str, Union[int, str, List[int]]]], input_bytes: bytes, tasks: Dict[int, Union[Dict[str, Union[int, str]], Dict[str, Union[int, str, List[int]]]]]) -> bytes:
    """
    Execute a task.

    Args:
    - task: A dictionary representing a task, containing 'id', 'task_type', and 'tasks' keys.
    - input_bytes: A bytes object representing the input data.
    - tasks: A dictionary containing task information with task ID as keys.

    Returns:
    - A bytes object representing the result of executing the task.
    """
    if 'tasks' in task:
        return execute_workflow(task, input_bytes, tasks)
    else:
        return encode_input_bytes(input_bytes)


def execute_workflow(workflow: Dict[str, Union[int, str, List[int]]], input_bytes: bytes, tasks: Dict[int, Union[Dict[str, Union[int, str]], Dict[str, Union[int, str, List[int]]]]]) -> bytes:
    """
    Execute a workflow.

    Args:
    - workflow: A dictionary representing a workflow task.
    - input_bytes: A bytes object representing the input data.
    - tasks: A dictionary containing task information with task ID as keys.

    Returns:
    - A bytes object representing the result of executing the workflow.
    """
    if not workflow['tasks']:
        return encode_input_bytes(b"")

    results = bytearray()
    for task_id in workflow['tasks']:
        task = tasks[task_id]
        task_result = execute_task(task, input_bytes, tasks)
        results.extend(task_result)

    return encode_input_bytes(results)


def main():
    """
    Main function to execute the workflow.

    Parses task and executable information from command line arguments,
    executes the workflow, and prints the results.
    """
    tasks = json.loads(sys.argv[1])
    executables = json.loads(sys.argv[2])

    parsed_tasks = {}
    for task in tasks:
        parsed_tasks[task['id']] = task

    executables_results = []
    for executable in executables:
        target_task = parsed_tasks[executable['workflow_id']]
        workflow_result = execute_workflow(
            target_task, executable['input'].encode(), parsed_tasks)
        executables_results.append(workflow_result.hex())

    print(json.dumps(executables_results))


if __name__ == "__main__":
    main()
