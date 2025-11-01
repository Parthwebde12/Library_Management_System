import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "library.db")

# module-level connection + cursor (file created if missing)
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

# ensure table exists
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
    """Insert a book and return the inserted row id."""
    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (title, author, int(year))
    )
    conn.commit()
    return cursor.lastrowid

def view_books():
    """Return list of tuples (id, title, author, year)."""
    cursor.execute("SELECT id, title, author, year FROM books")
    return cursor.fetchall()

def get_book(book_id):
    """Return a single book tuple or None."""
    cursor.execute("SELECT id, title, author, year FROM books WHERE id = ?", (book_id,))
    return cursor.fetchone()

def delete_book(book_id):
    """Delete by id; return number of deleted rows."""
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    return cursor.rowcount

def update_book(book_id, title, author, year):
    """Update a book; return number of updated rows."""
    cursor.execute(
        "UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?",
        (title, author, int(year), book_id)
    )
    conn.commit()
    return cursor.rowcount