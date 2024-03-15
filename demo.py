import sqlite3

connection = sqlite3.connect('mydatabase.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS book(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title Text,
        author Text,
        year INTEGER
        )
    ''')

#insert data into table

book_data = [
    ("The Progmatic Programmer", "Andy Hunt", 1999),
    ("Head First Python", "Paul Barry", 2010),
    ("Automate the Boring Stuff with Python", "Al Sweigart", 2015),
    ("Python for Data Analysis", "Wes Mckinney", 2017),
    ("Fluent Python", "Luciano Ramalho", 2015),
]

connection.executemany('INSERT INTO book(title, author, year) VALUES(?,?,?)', book_data)

#query data from the table

result = connection.execute('SELECT * FROM book')
data = result.fetchall()

#display the data
for row in data:
    print(f'Title: {row[1]}')
    print(f'Author: {row[2]}')
    print(f'Year: {row[3]}')
    print(f'')

connection.commit()

#close the database connection
connection.close()