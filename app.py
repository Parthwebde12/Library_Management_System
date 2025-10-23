import tkinter as tk
from tkinter import messagebox
from operations import add_book, view_books, delete_book

def add_book_ui():
    title = entry_title.get()
    author = entry_author.get()
    genre = entry_genre.get()
    year = entry_year.get()

    if not title or not author:
        messagebox.showerror("Error", "Title and Author required")
        return

    add_book(title, author, genre, year)
    messagebox.showinfo("Success", "Book added successfully!")
    clear_entries()

def view_all_books():
    books = view_books()
    listbox.delete(0, tk.END)
    for b in books:
        listbox.insert(tk.END, f"{b[0]} - {b[1]} ({b[2]}, {b[3]}, {b[4]})")

def delete_selected_book():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a book to delete")
        return
    book_text = listbox.get(selected[0])
    book_id = int(book_text.split(" - ")[0])
    delete_book(book_id)
    messagebox.showinfo("Deleted", "Book removed successfully!")
    view_all_books()

def clear_entries():
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_genre.delete(0, tk.END)
    entry_year.delete(0, tk.END)

root = tk.Tk()
root.title("Library Management System")

tk.Label(root, text="Title").grid(row=0, column=0)
entry_title = tk.Entry(root); entry_title.grid(row=0, column=1)

tk.Label(root, text="Author").grid(row=1, column=0)
entry_author = tk.Entry(root); entry_author.grid(row=1, column=1)

tk.Label(root, text="Genre").grid(row=2, column=0)
entry_genre = tk.Entry(root); entry_genre.grid(row=2, column=1)

tk.Label(root, text="Year").grid(row=3, column=0)
entry_year = tk.Entry(root); entry_year.grid(row=3, column=1)

tk.Button(root, text="Add Book", command=add_book_ui).grid(row=4, column=0, pady=5)
tk.Button(root, text="View Books", command=view_all_books).grid(row=4, column=1)
tk.Button(root, text="Delete Book", command=delete_selected_book).grid(row=5, column=0, columnspan=2, pady=5)

listbox = tk.Listbox(root, width=60)
listbox.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
