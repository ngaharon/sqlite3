import sqlite3

connection = sqlite3.connect('mydatabase.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name Text,
        age Text,
        department TEXT
        )
    ''')

#insert data into table

employee_data = [
    ("Andy Hunt", "32", "HR"),
    ("Alex sanya", "20", "UI design"),
    ("jakim kidundi", "38", "IT"),
    ("Vincent Aol", "21", "Software Engineer"),
    ("Aaron ngaira", "25", "Computer Science"),
    ("baraza bigman", "24", "IT"),
    ("issac kiplagat", "23", "Project Managment"),
    ("onyango lewis", "22", "Finance"),
    ("lennox introvert", "26", "Backend Developer"),
]

connection.executemany('INSERT INTO employees(name, age, department) VALUES(?,?,?)', employee_data)

#query data from the table

result = connection.execute('SELECT * FROM employees ORDER BY age ASC')
data = result.fetchall()

#display the data
for row in data:
    print(f'name: {row[1]}')
    print(f'age: {row[2]}')
    print(f'department: {row[3]}')
    print(f'')

connection.commit()

#close the database connection
connection.close()