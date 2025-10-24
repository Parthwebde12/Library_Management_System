import sqlite3

# Connect to SQLite database (file will be created if it doesn't exist)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
)
""")
conn.commit()

def add_book(title, author, year):
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()

def view_books():
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()

def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()

def update_book(book_id, title, author, year):
    cursor.execute("UPDATE books SET title=?, author=?, year=? WHERE id=?", (title, author, year, book_id))
    conn.commit()
