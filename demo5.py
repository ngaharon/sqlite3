import sqlite3

connection = sqlite3.connect('mydatabase.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS Students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name Text,
        age INTEGER
    )
''')

connection.execute('''
    CREATE TABLE IF NOT EXISTS Courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name Text,
        student_id INTEGER,
        FOREIGN KEY(student_id) REFERENCES Students(id)
         )
''')

students_data = [
    ("Andy Hunt", 18),
    ("Alex sanya", 19),
    ("ernest macharia", 20),
]

courses_data = [
    ("Statistics", 1),
    ("DBMS", 2),
    ("RDBMS", 3),
]

connection.executemany('INSERT INTO Students(name, age) VALUES(?,?)', students_data)
connection.executemany('INSERT INTO Courses(name, student_id) VALUES(?,?)', courses_data)

results = connection.execute('''
   SELECT Students.name, Courses.name
   FROM Students
   INNER JOIN Courses ON Students.id = Courses.student_id 
''')

connection.commit()

print("Student - Course relationship")
for row in results.fetchall():
    print(f'student: {row[0]}, course: {row[1]}')

connection.close()