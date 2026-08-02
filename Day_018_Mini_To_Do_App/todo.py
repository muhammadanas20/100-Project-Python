import json
from pathlib import Path

file = Path("task.json")

# FIX 1: Changed json.load to json.loads because file.read_text() returns a string
tasks = json.loads(file.read_text()) if file.exists() else []

action = input("add, list, or done: ").lower()

if action == "add":
    tasks.append({"text": input("Task: "), "done": False})
    
elif action == "list":
    for index, task in enumerate(tasks, 1):
        mark = "DONE" if task["done"] else "."
        print(f"{index}. [{mark}] {task['text']}")
        
elif action == "done":
    number = int(input("Task number: "))
    # FIX 2: Changed 'task[number]' to 'tasks[number - 1]' to use the list and adjust for 1-based indexing
    tasks[number - 1]["done"] = True

# FIX 3: Outdent this line so it saves your changes after any action is taken
file.write_text(json.dumps(tasks, indent=2))
