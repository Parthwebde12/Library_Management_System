import tkinter as tk
from tkinter import ttk, messagebox
import db_ops

# ----------------- Root Window -----------------
root = tk.Tk()
root.title("📚 Library Management System")
root.geometry("950x550")
root.configure(bg="#0f172a")  # Dark navy blue background

# ----------------- Style Config -----------------
style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview",
                background="#1e293b",
                foreground="white",
                rowheight=28,
                fieldbackground="#1e293b",
                font=("Segoe UI", 11))
style.configure("Treeview.Heading",
                background="#334155",
                foreground="white",
                font=("Segoe UI", 11, "bold"))
style.map("Treeview",
          background=[("selected", "#2563eb")])

# ----------------- Title Bar -----------------
title_frame = tk.Frame(root, bg="#1e293b", pady=10)
title_frame.pack(fill="x")

tk.Label(title_frame,
         text="📚 Library Management System",
         font=("Segoe UI", 20, "bold"),
         fg="white",
         bg="#1e293b").pack()

# ----------------- Input Frame -----------------
frame = tk.Frame(root, bg="#1e293b", padx=15, pady=10)
frame.pack(pady=15, fill="x")

labels = ["Title", "Author", "Year", "ISBN"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(frame, text=label, font=("Segoe UI", 12, "bold"),
             fg="white", bg="#1e293b").grid(row=i, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(frame, width=40, font=("Segoe UI", 11),
                     bg="#334155", fg="white", insertbackground="white", relief="flat")
    entry.grid(row=i, column=1, padx=10, pady=5, ipady=4)
    entries[label.lower()] = entry

# ----------------- Functions -----------------
def add_book():
    db_ops.add_book(entries["title"].get(), entries["author"].get(),
                    entries["year"].get(), entries["isbn"].get())
    messagebox.showinfo("Success", "Book added successfully!")
    show_books()

def show_books():
    for row in tree.get_children():
        tree.delete(row)
    for row in db_ops.view_books():
        tree.insert("", tk.END, values=row)

def delete_book():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Select", "Select a book to delete.")
        return
    book_id = tree.item(selected)['values'][0]
    db_ops.delete_book(book_id)
    messagebox.showinfo("Deleted", "Book deleted successfully.")
    show_books()

def update_book():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Select", "Select a book to update.")
        return
    book_id = tree.item(selected)['values'][0]
    db_ops.update_book(book_id,
                       entries["title"].get(), entries["author"].get(),
                       entries["year"].get(), entries["isbn"].get())
    messagebox.showinfo("Updated", "Book updated successfully.")
    show_books()

def on_row_select(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected)['values']
        entries["title"].delete(0, tk.END)
        entries["author"].delete(0, tk.END)
        entries["year"].delete(0, tk.END)
        entries["isbn"].delete(0, tk.END)
        entries["title"].insert(0, values[1])
        entries["author"].insert(0, values[2])
        entries["year"].insert(0, values[3])
        entries["isbn"].insert(0, values[4])

# ----------------- Buttons -----------------
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=5)

def make_button(text, cmd, color):
    btn = tk.Button(btn_frame, text=text, command=cmd,
                    bg=color, fg="white", font=("Segoe UI", 11, "bold"),
                    activebackground="#1d4ed8", activeforeground="white",
                    width=12, relief="flat", cursor="hand2")
    btn.pack(side="left", padx=7, pady=10)
    return btn

make_button("Add", add_book, "#22c55e")
make_button("View All", show_books, "#3b82f6")
make_button("Update", update_book, "#facc15")
make_button("Delete", delete_book, "#ef4444")
make_button("Exit", root.destroy, "#475569")

# ----------------- Treeview -----------------
tree_frame = tk.Frame(root, bg="#0f172a")
tree_frame.pack(padx=15, pady=10, fill="both", expand=True)

cols = ("ID", "Title", "Author", "Year", "ISBN")
tree = ttk.Treeview(tree_frame, columns=cols, show="headings", selectmode="browse")

for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=150)

tree.bind("<ButtonRelease-1>", on_row_select)
tree.pack(fill="both", expand=True)

# ----------------- Run -----------------
show_books()
root.mainloop()
