import json 
from pathlib import Path

file = Path("inventory.json")
stock = json.loads(file.read_text()) if file.exists() else {}
action = input("add,sell,or list: ").lower()
if action == "add":
    item = input("Product: ").lower()
    stock[item] = stock.get(item,0) + int(input("Quantity: "))
elif action == "sell":
    item = input("Product: ").lower()
    quantity = int(input("Quantity: "))
    if stock.get(item,0) >= quantity:
        stock[item] -= quantity
elif action == "list":
    for item,quantity in sorted(stock.items()):
        print(f"{item}: {quantity}")

file.write_text(json.dumps(stock,indent=2))