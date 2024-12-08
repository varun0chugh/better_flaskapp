import datetime
import jwt
from flask import Blueprint, jsonify, request, make_response, current_app
auth_blueprint = Blueprint('auth', __name__)

users = {
    "admin": "password123", 
    "user": "mypassword"
}

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username] == password:
        
        token = jwt.encode(
            {
                "username": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            },
            current_app.config['SECRET_KEY'],
            algorithm="HS256"
        )
        return jsonify({"token": token}), 200
    return jsonify({"message": "Invalid username or password"}), 401
@auth_blueprint.route('/protected', methods=['GET'])
def protected():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"message": "Token is missing!"}), 401
    try:
        token = auth_header.split(" ")[1]  # Format: "Bearer <token>"
        decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
        return jsonify({"message": f"Welcome {decoded_token['username']}!"}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired!"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token!"}), 401
