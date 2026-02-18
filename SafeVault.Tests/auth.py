import hashlib
import secrets

# Dummy in-memory user store (passwords are hashed)
users = {
    "admin": {
        "password": hashlib.sha256(b"admin123").hexdigest(),
        "role": "admin"
    },
    "user": {
        "password": hashlib.sha256(b"user123").hexdigest(),
        "role": "user"
    }
}

# Temporary token storage for authenticated sessions
tokens = {}

def authenticate_user(username, password):
    """
    Authenticates a user by:
    - Hashing the input password
    - Comparing it with the stored hashed password
    - Generating a secure token on successful login
    """
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username]["password"] == hashed:
        token = secrets.token_hex(16)
        tokens[token] = users[username]["role"]
        return token
    return None

def authorize_user(token, required_role):
    """
    Authorizes a user using role-based access control (RBAC)
    """
    role = tokens.get(token)
    return role == required_role
