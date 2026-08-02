import secrets
import string

length = int(input("Password length, at least 10: "))

if length < 10:
    print("Choose 10 character or more.")
else:
    alphabet = string.ascii_letters + string.digits + "!@#$%"
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    print(f"Generated Password: {password}")