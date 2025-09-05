from flask import Flask, request, jsonify
from auth import authenticate_user, authorize_user
from security import sanitize_input
from database import execute_query

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = sanitize_input(request.json.get('username'))
    password = sanitize_input(request.json.get('password'))
    token = authenticate_user(username, password)
    if token:
        return jsonify({"message": "Login successful", "token": token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/data', methods=['GET'])
def get_data():
    token = request.headers.get('Authorization')
    if not authorize_user(token, 'admin'):
        return jsonify({"message": "Access denied"}), 403
    result = execute_query("SELECT * FROM vault;")
    return jsonify({"data": result}), 200

if __name__ == "__main__":
    app.run(debug=True)
