import tkinter as tk
from tkinter import messagebox
from operations import connect_db, add_book, view_books, delete_book, update_book

# ---------- Window Setup ----------
root = tk.Tk()
root.title("📚 Simple Library Management")
root.geometry("500x450")
root.config(bg="#f7f7f7")

# ---------- Variables ----------
book_id_var = tk.StringVar()
title_var = tk.StringVar()
author_var = tk.StringVar()
year_var = tk.StringVar()
isbn_var = tk.StringVar()

# ---------- Functions ----------
def add_book_ui():
    if title_var.get() == "" or author_var.get() == "":
        messagebox.showwarning("Input Error", "Title and Author are required!")
        return
    add_book(title_var.get(), author_var.get(), year_var.get(), isbn_var.get())
    messagebox.showinfo("Success", "Book added successfully!")
    clear_fields()
    view_books_ui()

def view_books_ui():
    text_area.delete(1.0, tk.END)
    books = view_books()
    for book in books:
        text_area.insert(tk.END, f"ID: {book[0]} | {book[1]} by {book[2]} ({book[3]}) | ISBN: {book[4]}\n")

def delete_book_ui():
    if book_id_var.get() == "":
        messagebox.showwarning("Input Error", "Enter Book ID to delete!")
        return
    delete_book(book_id_var.get())
    messagebox.showinfo("Deleted", "Book deleted successfully!")
    clear_fields()
    view_books_ui()

def update_book_ui():
    if book_id_var.get() == "":
        messagebox.showwarning("Input Error", "Enter Book ID to update!")
        return
    update_book(book_id_var.get(), title_var.get(), author_var.get(), year_var.get(), isbn_var.get())
    messagebox.showinfo("Updated", "Book updated successfully!")
    clear_fields()
    view_books_ui()

def clear_fields():
    book_id_var.set("")
    title_var.set("")
    author_var.set("")
    year_var.set("")
    isbn_var.set("")

# ---------- Labels and Entries ----------
tk.Label(root, text="Book ID:", bg="#f7f7f7").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=book_id_var, width=25).grid(row=0, column=1, pady=5)

tk.Label(root, text="Title:", bg="#f7f7f7").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=title_var, width=25).grid(row=1, column=1, pady=5)

tk.Label(root, text="Author:", bg="#f7f7f7").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=author_var, width=25).grid(row=2, column=1, pady=5)

tk.Label(root, text="Year:", bg="#f7f7f7").grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=year_var, width=25).grid(row=3, column=1, pady=5)

tk.Label(root, text="ISBN:", bg="#f7f7f7").grid(row=4, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=isbn_var, width=25).grid(row=4, column=1, pady=5)

# ---------- Buttons ----------
tk.Button(root, text="Add Book", width=15, command=add_book_ui, bg="#d0f0c0").grid(row=5, column=0, pady=10)
tk.Button(root, text="View All", width=15, command=view_books_ui, bg="#add8e6").grid(row=5, column=1, pady=10)
tk.Button(root, text="Update Book", width=15, command=update_book_ui, bg="#ffb6c1").grid(row=6, column=0, pady=5)
tk.Button(root, text="Delete Book", width=15, command=delete_book_ui, bg="#ff7f7f").grid(row=6, column=1, pady=5)
tk.Button(root, text="Clear Fields", width=15, command=clear_fields, bg="#e0e0e0").grid(row=7, column=0, columnspan=2, pady=5)

# ---------- Text Area ----------
text_area = tk.Text(root, height=10, width=55)
text_area.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

# ---------- Initialize ----------
connect_db()
view_books_ui()

root.mainloop()
