from datetime import date
from pathlib import Path

journel = Path("journel.txt")
print("Write today's entry. Entry a blank line to finish")

lines = []

while True:
    line = input()
    if not line: break
    lines.append(line)

with journel.open("a",encoding="utf-8") as file:
    file.write(f"\n## {date.today()}\n")
    file.write("\n".join(lines) + "\n")
print("journel entry saved.")
    