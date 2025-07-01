from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    message = ''
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # ✅ FIXED: Using parameterized query (prevents SQL Injection)
        query = "SELECT * FROM users WHERE username = ? AND password = ?"

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            message = "✅ Login successful!"
        else:
            message = "❌ Invalid credentials!"

    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)


#❌ Old (vulnerable):query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
#cursor.execute(query)
