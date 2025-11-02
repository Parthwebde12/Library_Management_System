import sqlite3

# --- Create database and table ---
def connect_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            year TEXT,
            isbn TEXT
        )
    """)
    conn.commit()
    conn.close()

# --- Add a new book ---
def add_book(title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)",
                   (title, author, year, isbn))
    conn.commit()
    conn.close()

# --- View all books ---
def view_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows

# --- Delete a book by ID ---
def delete_book(book_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

# --- Update a book by ID ---
def update_book(book_id, title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE books
        SET title=?, author=?, year=?, isbn=?
        WHERE id=?
    """, (title, author, year, isbn, book_id))
    conn.commit()
    conn.close()
