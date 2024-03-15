from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = 'mydatabase.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/')
def index():
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM book').fetchall()
    conn.close()
    return render_template('index.html', book=book)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']

        conn = get_db_connection()
        conn.execute('INSERT INTO book (title, author, year) VALUES(?, ?, ?)', (title, author, year))
    conn.commit()
    conn.close()

    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)


