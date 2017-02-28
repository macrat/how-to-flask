import sqlite3


db = sqlite3.connect('database.db')

db.execute('CREATE TABLE tbl (id, text)')

db.execute('INSERT INTO tbl VALUES (?, ?)', (0, 'hello'))

result = db.execute('SELECT * FROM tbl')
data = result.fetchall()
print(data)
