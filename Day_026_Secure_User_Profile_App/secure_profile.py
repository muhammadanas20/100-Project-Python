# Libraries for hashing data, working with JSON files, and generating secure random numbers
import hashlib, json, secrets
# Library to hide the password while the user is typing it in the terminal
from getpass import getpass

# Get inputs: strip extra spaces from username, and convert password into bytes for hashing
username = input("Username: ").strip()
password = getpass("Password: ").encode()

# Generate 16 random unique bytes (salt) to make the password hash unpredictable
salt = secrets.token_bytes(16)
# Securely scramble the password using the salt and 200,000 rounds of computation (stretching)
digest = hashlib.pbkdf2_hmac("sha256", password, salt, 200000)

# Bundle user data together, converting raw bytes into readable hex text strings
profile = { 
    "username": username,
    "salt": salt.hex(),
    "password_hash": digest.hex()
}

# Open a text file named 'profile.json' and write the bundled data inside it cleanly
with open("profile.json", "w") as file:
    json.dump(profile, file, indent=2)

print("Profile saved without the plain password.")
