# Experiment 1: Code Vulnerability Analysis

## Objective
To identify common security vulnerabilities in code and implement their secure (fixed) versions.

---

## Vulnerabilities Covered

1. Buffer Overflow
2. Hardcoded Credentials
3. Format String Vulnerability
4. Command Injection

---

## 1. Buffer Overflow

### Description
Buffer overflow occurs when input exceeds the allocated memory size.

### Vulnerable Code
- Uses unsafe function like `gets()`
- Can overwrite memory and crash program

### Fixed Code
- Uses safe function like `fgets()`
- Limits input size to prevent overflow

---

## 2. Hardcoded Credentials

### Description
Sensitive information like usernames and passwords are directly written in code.

### Vulnerable Code
- Username and password stored in plain text
- Easy to access and misuse

### Fixed Code
- Uses hashing (SHA-256)
- Password is not stored in plain text

---

## 3. Format String Vulnerability

### Description
Occurs when user input is directly passed to functions like `printf()`.

### Vulnerable Code
- `printf(input);`
- Allows attacker to manipulate memory

### Fixed Code
- `printf("%s", input);`
- Proper format specifier used

---

## 4. Command Injection

### Description
User input is executed as a system command.

### Vulnerable Code
- Uses `os.system()` with user input
- Allows execution of malicious commands

### Fixed Code
- Uses `subprocess.run()` with arguments
- Prevents command injection

---

## Conclusion

This experiment demonstrates how common vulnerabilities can be exploited and how secure coding practices can prevent them.

---

## Learning Outcome

- Understanding of basic security flaws
- Ability to identify vulnerable code
- Implementation of secure coding techniques
