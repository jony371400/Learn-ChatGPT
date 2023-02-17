from flask import Flask, jsonify, request
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL)')
    conn.close()

create_table()

@app.route('/register', methods=['POST'])
def register():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify registration information'}), 401

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (auth.username,))
    user = cursor.fetchone()
    if user:
        return jsonify({'message': 'Username already exists'}), 400

    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (auth.username, auth.password))
    conn.commit()
    conn.close()

    print("/register Success !")

    return jsonify({'message': 'Registration successful'}), 201

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify login information'}), 401

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (auth.username, auth.password))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({'message': 'Incorrect login credentials'}), 401

    print("/login Success !")

    return jsonify({'message': 'Login successful'}), 200

@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()

    if not user:
        return jsonify({'message': 'User does not exist'}), 404

    cursor.execute('DELETE FROM users WHERE username = ?', (username,))
    conn.commit()
    conn.close()

    print("/delete Success !")
    
    return jsonify({'message': 'User deleted successfully'}), 200

if __name__ == '__main__':
    app.run()