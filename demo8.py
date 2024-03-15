import sqlite3

connection = sqlite3.connect('mydatabase.db')

# dropping tables 

#book_id_to_delete = 1

connection.execute('ALTER TABLE employees ADD COLUMN transport TEXT')

connection.commit()

#result = connection.execute('SELECT * FROM book')

#print("book")

#for row in result.fetchall():
#    print(f'Title: {row[1]}')
#    print(f'Author: {row[2]}')
#   print(f'Year: {row[3]}')
#    print('')