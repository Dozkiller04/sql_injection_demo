import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

# Drop old table (if any)
c.execute('DROP TABLE IF EXISTS users')

# Create a new users table
c.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
''')

# Insert dummy users
c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
c.execute("INSERT INTO users (username, password) VALUES ('soham', 'pass123')")

conn.commit()
conn.close()
print("Database setup complete.")
