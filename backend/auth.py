import json
from werkzeug.security import generate_password_hash, check_password_hash

USERS_FILE = "users.json"

def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def add_user(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = generate_password_hash(password)
    save_users(users)
    return True

def verify_user(username, password):
    users = load_users()
    pw_hash = users.get(username)
    return pw_hash and check_password_hash(pw_hash, password)
