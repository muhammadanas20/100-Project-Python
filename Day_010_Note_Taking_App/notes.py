from datetime import datetime
from pathlib import Path

file = Path("notes.txt")

action = input("write or read? ").lower()

if action == "write" :
    note = input("your note: ").strip()
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with file.open("a",encoding="utf-8") as handle:
        handle.write(f"[{stamp}] {note}\n")
elif action == "read":
    print(file.read_text() if file.exists() else "No notes yet. ")