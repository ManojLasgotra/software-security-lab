import hashlib

# ----------- VULNERABLE CODE -----------
print("Vulnerable Login")
username = "admin"
password = "admin123"

user = input("Username: ")
pwd = input("Password: ")

if user == username and pwd == password:
    print("Login Success (Vulnerable)")
else:
    print("Login Failed")

# ----------- FIXED CODE -----------
print("\nSecure Login")

stored_password = hashlib.sha256("admin123".encode()).hexdigest()

user_pwd = input("Password: ")
hashed_input = hashlib.sha256(user_pwd.encode()).hexdigest()

if hashed_input == stored_password:
    print("Login Success (Secure)")
else:
    print("Login Failed")
