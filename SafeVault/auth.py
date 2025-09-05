import hashlib
import secrets

# Dummy user store
users = {
    "admin": {"password": hashlib.sha256(b"admin123").hexdigest(), "role": "admin"},
    "user": {"password": hashlib.sha256(b"user123").hexdigest(), "role": "user"}
}

# Simple token storage (for demo)
tokens = {}

def authenticate_user(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username]["password"] == hashed:
        token = secrets.token_hex(16)
        tokens[token] = users[username]["role"]
        return token
    return None

def authorize_user(token, required_role):
    role = tokens.get(token)
    return role == required_role
