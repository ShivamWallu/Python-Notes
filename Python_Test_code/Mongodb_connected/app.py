# app.py

from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['user_database']
users_collection = db['users']

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    # Check if user already exists
    if users_collection.find_one({"email": email}):
        return jsonify({"error": "Email already registered"}), 400
    
    # Insert new user
    user = {
        "username": username,
        "email": email,
        "password": password  # Note: In a real app, hash this password
    }
    users_collection.insert_one(user)
    
    return jsonify({"message": "Registration successful"}), 201

if __name__ == '__main__':
    app.run(debug=True)






# from flask import Flask, request, render_template, jsonify
# from pymongo import MongoClient
# from werkzeug.security import generate_password_hash

# app = Flask(__name__)

# # MongoDB setup
# client = MongoClient('mongodb://localhost:27017/')
# db = client['user_database']
# users_collection = db['users']

# @app.route('/')
# def home():
#     return render_template('register.html')

# @app.route('/register', methods=['POST'])
# def register():
#     user_data = {
#         "username": request.form['username'],
#         "email": request.form['email'],
#         "password": generate_password_hash(request.form['password'])  # Hash password
#     }
    
#     if users_collection.find_one({"email": user_data['email']}):
#         return jsonify({"error": "Email already registered"}), 400
    
#     users_collection.insert_one(user_data)
#     return jsonify({"message": "Registration successful"}), 201

# if __name__ == '__main__':
#     app.run(debug=True)
