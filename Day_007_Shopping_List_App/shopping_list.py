items = []

while True:
    action = input("Enter action(add,view,remove,quit)").lower().strip()
    
    if action == "add":
        item = input("Enter item:").strip()
        items.append(item)
    elif action == "view":
        for number,item in enumerate(items,start = 1):
            print(f"{number}. {item}")
    elif action == "remove":
        item = input("Enter item to remove:").strip()
        if item in items:
            items.remove(item)
            print("Item removed sucessfully")
        else:
            print("Item is in list")
    elif action == "quit":
        print("Happy to Assist you! Thank You.")
        break
        