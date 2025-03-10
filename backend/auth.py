import json
import os
import hashlib

USER_DB = "users.json"

def hash_password(password):
    """Returns a hashed version of the password."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """Loads users from the JSON file."""
    if not os.path.exists(USER_DB):
        return {}
    with open(USER_DB, "r") as file:
        return json.load(file)

def save_users(users):
    """Saves the users to the JSON file."""
    with open(USER_DB, "w") as file:
        json.dump(users, file, indent=4)

def sign_up(username, password):
    """Handles user sign-up."""
    users = load_users()
    if username in users:
        return False, "Username already exists!"
    
    users[username] = hash_password(password)
    save_users(users)
    return True, "Sign-up successful! You can now log in."

def log_in(username, password):
    """Handles user login."""
    users = load_users()
    if username not in users:
        return False, "User does not exist!"
    
    if users[username] != hash_password(password):
        return False, "Incorrect password!"
    
    return True, "Login successful!"
