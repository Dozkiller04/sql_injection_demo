from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # ❌ VULNERABLE query (no protection)
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        #Fix Recommendation (Ethical Practice)
        #query = "SELECT * FROM users WHERE username = ? AND password = ?"
        #cursor.execute(query, (username, password))


        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()

        if result:
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html", message="❌ Invalid credentials!")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
