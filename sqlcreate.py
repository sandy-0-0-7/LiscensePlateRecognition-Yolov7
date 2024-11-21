import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# cursor.execute('''
# INSERT INTO users (name, age, email)
# VALUES (?, ?, ?)
# ''', ('Alice', 30, 'alice@example.com'))

# cursor.execute('''
# INSERT INTO users (name, age, email)
# VALUES (?, ?, ?)
# ''', ('Madhu', 21, 'madhu@gmail.com'))

connection.commit()

cursor.execute('SELECT * FROM users WHERE name = "Alice"')
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()