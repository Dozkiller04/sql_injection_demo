# 🛡️ SQL Injection Demonstration Project (Flask + SQLite)

This project is created to **demonstrate SQL Injection vulnerabilities** in web applications and show **how to prevent them** using secure coding practices.

## 📌 Project Description

A simple login system built using **Python Flask** and **SQLite** that first simulates a **vulnerable login** mechanism and then demonstrates how to **secure it using parameterized queries**.

---

## 🧱 Project Structure
sql_injection_demo/
├── app.py # Flask app (vulnerable and secure version)
├── db_setup.py # Script to create the SQLite database
├── templates/
│ └── login.html # Frontend login form
└── users.db # SQLite database (auto-generated)


---

## 🛠️ How to Run

### 🔹 Step 1: Install Dependencies
```bash
pip install flask


---

## 🛠️ How to Run

### 🔹 Step 1: Install Dependencies
```bash
pip install flask

🔹 Step 3: Run the Flask App
bash
Copy code
python app.py
Go to http://127.0.0.1:5000 in your browser.

💉 Test SQL Injection
Try logging in with:

Username: ' OR '1'='1

Password: anything

👉 In the vulnerable version, this will bypass authentication due to SQL Injection.

🔐 Fix: Secure Version
python
Copy code
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
✅ This uses parameterized queries and blocks SQL Injection completely.

📚 Awareness Material (Optional)
Overview of SQL Injection

Real-world examples

Secure coding best practices

Input validation tips

🧑‍💻 Author
Soham Pramod Tayade
GitHub: Dozkiller04

📃 License
This project is for educational and awareness purposes only.

yaml
Copy code

---

### ✅ How to Add This to Your Project

1. Open your project folder.
2. Create a file: `README.md`
3. Copy-paste the above content into that file.
4. Save and then run:
```bash
git add README.md
git commit -m "Added README.md"
git push

