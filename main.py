import sqlite3

connection = sqlite3.connect(

"bank.db"

)

cursor = connection.cursor()

cursor.execute(

"""

CREATE TABLE IF NOT EXISTS accounts(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,

balance INTEGER

)

"""

)

connection.commit()

print(

"\nBANK MANAGEMENT SYSTEM"

)