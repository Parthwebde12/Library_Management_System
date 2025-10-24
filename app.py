import tkinter as tk
from tkinter import ttk, messagebox
from operations import add_book, view_books, delete_book

root = tk.Tk()
root.title("📚 Library Management System")
root.geometry("750x550")
root.configure(bg="#f0f0f0")

# ---------------- Functions ----------------
def add_record():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()

    if not title or not author or not year:
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        add_book(title, author, int(year))
        messagebox.showinfo("Success", "Book added successfully!")
        clear_entries()
        refresh_table()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    for book in view_books():
        tree.insert("", tk.END, values=book)

def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)

def delete_record():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to delete")
        return
    book_id = tree.item(selected)['values'][0]
    delete_book(book_id)
    refresh_table()

# ---------------- GUI ----------------
tk.Label(root, text="Library Management System", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=10)

form_frame = tk.Frame(root, bg="#f0f0f0")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Title:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
title_entry = tk.Entry(form_frame)
title_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Author:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5)
author_entry = tk.Entry(form_frame)
author_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Year:", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5)
year_entry = tk.Entry(form_frame)
year_entry.grid(row=2, column=1)

tk.Button(form_frame, text="Add Book", command=add_record).grid(row=3, column=0, pady=10)
tk.Button(form_frame, text="Delete Book", command=delete_record).grid(row=3, column=1, pady=10)
tk.Button(form_frame, text="Refresh", command=refresh_table).grid(row=3, column=2, pady=10)

columns = ("ID", "Title", "Author", "Year")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(fill=tk.BOTH, expand=True, pady=20)

refresh_table()
root.mainloop()
