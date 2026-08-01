contact = {}

while True:
    action = input("add, find, list, delete, quit: ").lower()
    
    if action == "add":
        name = input("Name: ").title()
        contact[name] = input("Phone: ").strip()
    elif action =="find":
        name = input("Name: ").title()
        print(contact.get(name, "Contact not found"))
    elif action == "list":
        for name,phone in sorted(contact.items()):
            print(f"{name}: {phone}")
    elif action == "delete":
        contact.pop(input("Name: ").title(),None)
    elif action == "quit": 
        print("Thank you for choosing us!")
        break
    else:
        print("Oops worng action cmd! Try Again")