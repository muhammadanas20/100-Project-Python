scores = []

while True:
    entry =  input("Score,or done: ").strip().lower()
    if entry == "done": break
    scores.append(float(entry))

for score in scores:
    if score >= 90: letter = "A"
    elif score >= 80: letter = "B"
    elif score >= 70: letter = "C"
    elif score >= 60: letter = "D"
    else: letter = "F"
    print(f"{score:.2f}: {letter}")

if scores:
    print(f"Class Average: {sum(scores) / len(scores):.2f}")