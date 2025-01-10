import mysql.connector
import random
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="",  
    database="banking_system"
)
cursor = db.cursor()


def generate_account_number():
    return random.randint(10**9, 10**10 - 1)

# Add user
def add_user():
    name = input("Enter name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    city = input("Enter city: ")
    password = input("Enter password: ")
    contact_number = input("Enter contact number: ")
    email = input("Enter email ID: ")
    address = input("Enter address: ")
    initial_balance = 2000

    account_number = generate_account_number()

    cursor.execute(
        "INSERT INTO users (name, account_number, dob, city, password, balance, contact_number, email, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (name, account_number, dob, city, password, initial_balance, contact_number, email, address),
    )
    db.commit()
    print(f"User added successfully! Account Number: {account_number}")

def show_users():
    cursor.execute("SELECT name, account_number, city, balance FROM users")
    users = cursor.fetchall()
    for user in users:
        print(f"Name: {user[0]}, Account Number: {user[1]}, City: {user[2]}, Balance: {user[3]}")

# Login
def login():
    acc_number = int(input("Enter account number: "))
    password = input("Enter password: ")

    cursor.execute("SELECT * FROM users WHERE account_number = %s AND password = %s", (acc_number, password))
    user = cursor.fetchone()

    if user:
        print("Login successful!")
        while True:
            print("""
            1. Show Balance
            2. Credit Amount
            3. Debit Amount
            4. Logout
            """)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print(f"Your balance is: {user[5]}")
            elif choice == 2:
                credit_amount(acc_number)
            elif choice == 3:
                debit_amount(acc_number)
            elif choice == 4:
                print("Logged out successfully!")
                break
            else:
                print("Invalid choice!")
    else:
        print("Invalid account number or password.")

# Credit amount
def credit_amount(acc_number):
    amount = float(input("Enter amount to credit: "))
    cursor.execute("UPDATE users SET balance = balance + %s WHERE account_number = %s", (amount, acc_number))
    cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, 'Credit', %s)", (acc_number, amount))
    db.commit()
    print("Amount credited successfully.")

# Debit amount
def debit_amount(acc_number):
    amount = float(input("Enter amount to debit: "))
    cursor.execute("SELECT balance FROM users WHERE account_number = %s", (acc_number,))
    balance = cursor.fetchone()[0]

    if balance >= amount:
        cursor.execute("UPDATE users SET balance = balance - %s WHERE account_number = %s", (amount, acc_number))
        cursor.execute("INSERT INTO transactions (account_number, transaction_type, amount) VALUES (%s, 'Debit', %s)", (acc_number, amount))
        db.commit()
        print("Amount debited successfully.")
    else:
        print("Insufficient balance.")

def main_menu():
    while True:
        print("""
        1. Add User
        2. Show Users
        3. Login
        4. Exit
        """)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_user()
        elif choice == 2:
            show_users()
        elif choice == 3:
            login()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main_menu()
          
