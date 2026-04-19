import sqlite3

# -------- DATABASE SETUP --------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', '1234')")
conn.commit()

# -------- VULNERABLE CODE --------
print("---- Vulnerable Login ----")

username = input("Enter username: ")
password = input("Enter password: ")

query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
print("Query:", query)

cursor.execute(query)
result = cursor.fetchone()

if result:
    print("Login Successful (Vulnerable)")
else:
    print("Login Failed")

# -------- FIXED CODE --------
print("\n---- Secure Login ----")

username = input("Enter username: ")
password = input("Enter password: ")

query = "SELECT * FROM users WHERE username=? AND password=?"
cursor.execute(query, (username, password))

result = cursor.fetchone()

if result:
    print("Login Successful (Secure)")
else:
    print("Login Failed")

conn.close()
