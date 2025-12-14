import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="parth1611",   # I have put my sql server database you can upload yours to run it in your system
        database="library_db"
    )

def add_book(title, author, year, isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year, isbn) VALUES (%s, %s, %s, %s)", 
                   (title, author, year, isbn))
    conn.commit()
    conn.close()

def view_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=%s", (book_id,))
    conn.commit()
    conn.close()

def update_book(book_id, title, author, year, isbn):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s", 
                   (title, author, year, isbn, book_id))
    conn.commit()
    conn.close()
