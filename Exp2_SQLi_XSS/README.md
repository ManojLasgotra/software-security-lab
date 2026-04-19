# Experiment 2: SQL Injection and XSS

## Objective
To perform SQL Injection and XSS attacks and apply security fixes.

## SQL Injection

### Vulnerable
Uses string concatenation → login bypass possible

### Attack
' OR '1'='1

### Fixed
Uses parameterized query → secure

---

## XSS

### Vulnerable
Uses innerHTML → script executes

### Attack
<script>alert('Hacked')</script>

### Fixed
Uses innerText → safe

---

## Output

SQL Injection:
- Vulnerable → Login Successful
- Secure → Login Failed

XSS:
- Vulnerable → Alert popup
- Secure → Text shown only
