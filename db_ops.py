import pyodbc

def get_connection():
    return pyodbc.connect('DSN=LibraryDSN')

def add_book(title, author, year, isbn):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view_books():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_book(book_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

def update_book(book_id, title, author, year, isbn):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, book_id))
    conn.commit()
    conn.close()
