required = {"flour","sugar","eggs","milk"}

answer = input("Ingredients you have, seprated by commas: ")

available = {item.strip().lower() for item in answer.split(",")}

missing = required - available

if not missing:
    print("You have everythign for the recipe!")
else:
    print("You still need:")
    for item in sorted(missing):
        print((f" - {item}"))
        