import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

# Database setup- id_number added as secondary key
def setup_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            id_number INTEGER NOT NULL, 
            name TEXT NOT NULL,
            tel TEXT NOT NULL,
            address TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert user data
def insert_user(id_number, name, tel, address, email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (id_number, name, tel, address, email) VALUES (?, ?, ?, ?, ?)', 
                   (id_number, name, tel, address, email))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "User registered successfully!")

# Function to search for a user by name
def search_user(name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    user = cursor.fetchone()
    conn.close()
    return user

# Function to search for a user by id_number
def search_user(id_number):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE name = ?', (id_number,))
    user = cursor.fetchone()
    conn.close()
    return user

# Function to count total users
def count_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    conn.close()
    return count

# Function to show user summary chart
def show_summary_chart():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM users')
    users = cursor.fetchall()
    conn.close()

    user_names = [user[0] for user in users]
    user_count = len(user_names)

    plt.figure(figsize=(8, 4))
    plt.bar(user_names, [1] * user_count, color='skyblue')
    plt.title('User Registration Summary')
    plt.xlabel('User Names')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()