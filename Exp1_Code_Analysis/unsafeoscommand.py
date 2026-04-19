import os
import subprocess

# ----------- VULNERABLE CODE -----------
print("Vulnerable Command Execution")

user_input = input("Enter filename: ")

# ❌ Directly user input ko system command me use karna (dangerous)
os.system("cat " + user_input)


# ----------- FIXED CODE -----------
print("\nSecure Command Execution")

user_input = input("Enter filename: ")

# ✅ Safe way (no command injection)
subprocess.run(["cat", user_input])
