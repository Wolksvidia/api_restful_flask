import sqlite3

connetion = sqlite3.connect('data.db')

cursor = connetion.cursor()

create_table = 'CREATE TABLE users (id int, username text, password text)'

cursor.execute(create_table)

user = (1, 'admin', '1234')
insert_query = 'INSERT INTO users VALUES (?,?,?)'

cursor.execute(insert_query, user)

users = [
    (2, 'admin2', '1234'),
    (3, 'admin3', '1234'),
    (4, 'admin4', '1234'),
    (5, 'admin5', '1234'),
    (6, 'admin6', '1234')
]

cursor.executemany(insert_query, users)

select_query = 'SELECT * FROM users'

for row in cursor.execute(select_query):
    print(row)

connetion.commit()
connetion.close()