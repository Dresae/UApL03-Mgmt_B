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

# GUI setup
def submit():
    id_number = id_number_entry.get()
    name = name_entry.get()
    tel = tel_entry.get()
    address = address_entry.get()
    email = email_entry.get()
    insert_user(id_number, name, tel, address, email) 
    clear_entries()
 
def search():
    name = search_entry.get()
    user = search_user(name)
    if user:
        messagebox.showinfo("User Found", f"id_number: {user[1]}, Name: {user[2]}, Tel: {user[3]}, Address: {user[4]}, Email: {user[5]}")
    else:
        messagebox.showwarning("Not Found", "User not found.")

def show_summary():
    count = count_users()
    messagebox.showinfo("User Summary", f"Total registered users: {count}")

def clear_entries():
    id_number_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    tel_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)


# Main application
setup_database()

app = tk.Tk()
app.title("User Registration")

# Registration Form
tk.Label(app, text="ID Number").grid(row=0, column=0)
id_number_entry = tk.Entry(app)
id_number_entry.grid(row=0, column=1)

tk.Label(app, text="Name").grid(row=1, column=0)
name_entry = tk.Entry(app)
name_entry.grid(row=1, column=1)

tk.Label(app, text="Telephone").grid(row=2, column=0)
tel_entry = tk.Entry(app)
tel_entry.grid(row=2, column=1)

tk.Label(app, text="Address").grid(row=3, column=0)
address_entry = tk.Entry(app)
address_entry.grid(row=3, column=1)

tk.Label(app, text="Email").grid(row=4, column=0)
email_entry = tk.Entry(app)
email_entry.grid(row=4, column=1)

tk.Button(app, text="Submit", command=submit).grid(row=5, columnspan=2)