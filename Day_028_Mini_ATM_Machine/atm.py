from getpass import getpass

pin = "5860"

balance = 6000.0

if getpass("Demo PIN: ") != pin:
    print("Access denied!")
else:
    while True:
        action = input("balance,deposit,withdraw,quit: ").lower()
        if action == "balance": print(f"Balance: {balance}")
        elif action == "deposit":
            balance += float(input("Amount: "))
        elif action == "withdraw":
            amount = float(input("Amount: "))
            if 0 < amount <= balance: 
                 balance -= amount
                 print("Amount sucessfully withdrawn!")
            else:
                print("Not enough balance!")
        elif action == "quit": break
        else: print("Enter a correct command!")