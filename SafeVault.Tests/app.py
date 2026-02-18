from flask import Flask, request, jsonify
from auth import authenticate_user, authorize_user
from security import sanitize_input
from database import execute_query

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Sanitize input to prevent SQL injection and XSS attacks
    username = sanitize_input(request.json.get('username'))
    password = sanitize_input(request.json.get('password'))

    # Authenticate user and generate token
    token = authenticate_user(username, password)
    if token:
        return jsonify({"message": "Login successful", "token": token}), 200

    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/data', methods=['GET'])
def get_data():
    # Extract token from request header
    token = request.headers.get('Authorization')

    # Authorize user using role-based access control (RBAC)
    if not authorize_user(token, 'admin'):
        return jsonify({"message": "Access denied"}), 403

    # Execute parameterized database query
    result = execute_query("SELECT * FROM vault;")
    return jsonify({"data": result}), 200

if __name__ == "__main__":
    # Debug mode enabled only for development/testing
    app.run(debug=True)
