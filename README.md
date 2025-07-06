# 🛡️ SQL Injection Demo – RISE Internship Project

This project demonstrates how an insecure login form can be exploited using SQL Injection.

---

## 🚀 About the Project

- 🔧 Built using: **Python (Flask)** + **SQLite3**
- 🎯 Purpose: To show how attackers can bypass authentication using SQL Injection
- ✅ For educational and ethical use only

---

## 🧪 Demo

### 🔐 Vulnerable Login Form:
![Login Form](screenshot(Output)/Login_Live_Demo_Page.png)

### 💥 SQL Injection Payload:
Username: ' OR 1=1 --
Password: (blank)

yaml
Copy code

### ✅ Successful Login (Injection Bypass):
![SQL Injection Bypass](screenshot(Output)/Sql_injection_Admin_page.png)

---

## 🎥 Project Walkthrough (with Voice-over)

▶️ [Click to Watch Demo Video](https://drive.google.com/file/d/1nXOBfAxCDT5numdM8Z8ycsYAjl6GpyGD/view?usp=drive_link)

---

## 🧠 How It Works

The application is intentionally made vulnerable for demonstration:

```python
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
This allows attackers to manipulate the SQL query and bypass authentication.

🔐 Secure Version (To prevent SQL Injection)
In real-world applications, always use parameterized queries:

python
Copy code
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
This ensures that user input is safely handled.

📁 Project Structure
pgsql
Copy code
sql_injection_demo/
├── app.py
├── users.db
├── templates/
│   ├── login.html
│   └── dashboard.html
├── screenshots/
│   ├── login_form.png
│   └── sql_bypass_success.png
├── README.md
👨‍💻 Developed By
Name: Soham Tayade

Internship: RISE Cybersecurity & Ethical Hacking Internship – July 2025
