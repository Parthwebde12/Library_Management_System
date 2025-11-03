import tkinter as tk
from tkinter import ttk, messagebox
import db_ops

# ----------- FUNCTIONS -----------
def refresh_books():
    try:
        books = db_ops.view_books()
        for row in tree.get_children():
            tree.delete(row)
        for book in books:
            tree.insert("", "end", values=book)
        status_var.set("✅ Books loaded successfully.")
    except Exception as e:
        status_var.set(f"❌ Database connection error: {e}")

def add_book():
    title, author, year, isbn = title_var.get(), author_var.get(), year_var.get(), isbn_var.get()
    if not title or not author:
        messagebox.showwarning("Input Error", "Please fill in Title and Author")
        return
    db_ops.add_book(title, author, year, isbn)
    refresh_books()
    clear_fields()
    status_var.set("✅ Book added successfully.")

def delete_book():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a book to delete.")
        return
    book_id = tree.item(selected[0])['values'][0]
    db_ops.delete_book(book_id)
    refresh_books()
    clear_fields()
    status_var.set("🗑️ Book deleted successfully.")

def update_book():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Select a book to update.")
        return
    book_id = tree.item(selected[0])['values'][0]
    db_ops.update_book(book_id, title_var.get(), author_var.get(), year_var.get(), isbn_var.get())
    refresh_books()
    clear_fields()
    status_var.set("✏️ Book updated successfully.")

def clear_fields():
    title_var.set("")
    author_var.set("")
    year_var.set("")
    isbn_var.set("")

# ----------- UI SETUP -----------
root = tk.Tk()
root.title("📚 Library Management System")
root.geometry("880x550")
root.configure(bg="#f1f2f6")

# --- Fonts & Styles ---
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#273c75", foreground="white")
style.configure("Treeview", font=("Segoe UI", 10), rowheight=25)
style.map("Treeview", background=[("selected", "#74b9ff")])
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)

# --- Variables ---
title_var, author_var, year_var, isbn_var = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
status_var = tk.StringVar(value="Ready...")

# --- Header ---
header = tk.Label(root, text="📘 Library Management System", bg="#273c75", fg="white",
                  font=("Segoe UI", 18, "bold"), pady=12)
header.pack(fill="x")

# --- Input Frame ---
form_frame = tk.Frame(root, bg="#dcdde1", padx=15, pady=15)
form_frame.pack(padx=20, pady=10, fill="x")

labels = [("Title", title_var), ("Author", author_var), ("Year", year_var), ("ISBN", isbn_var)]
for i, (text, var) in enumerate(labels):
    tk.Label(form_frame, text=text, bg="#dcdde1", font=("Segoe UI", 10, "bold")).grid(row=i//2, column=(i%2)*2, padx=10, pady=8, sticky="e")
    tk.Entry(form_frame, textvariable=var, font=("Segoe UI", 10), width=30).grid(row=i//2, column=(i%2)*2+1, padx=10, pady=8)

# --- Buttons ---
btn_frame = tk.Frame(root, bg="#f1f2f6")
btn_frame.pack(pady=10)

btn_colors = {
    "Add Book": "#6ab04c",
    "Update Book": "#f9ca24",
    "Delete Book": "#eb4d4b",
    "Clear Fields": "#22a6b3",
    "Refresh": "#4834d4"
}

for i, (text, color) in enumerate(btn_colors.items()):
    action = [add_book, update_book, delete_book, clear_fields, refresh_books][i]
    tk.Button(btn_frame, text=text, command=action, width=14, bg=color, fg="white",
              relief="flat", font=("Segoe UI", 10, "bold"), activebackground="#130f40").grid(row=0, column=i, padx=8, pady=5)

# --- TreeView (Book Table) ---
tree_frame = tk.Frame(root, bg="#f1f2f6")
tree_frame.pack(padx=20, pady=10, fill="both", expand=True)

columns = ("ID", "Title", "Author", "Year", "ISBN")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=150 if col != "ID" else 60)

scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# --- Status Bar ---
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief="sunken", anchor="w",
                      bg="#273c75", fg="white", font=("Segoe UI", 10, "bold"))
status_bar.pack(side="bottom", fill="x")

# --- Initialize ---
refresh_books()
root.mainloop()
