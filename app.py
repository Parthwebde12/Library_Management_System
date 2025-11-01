import tkinter as tk
from tkinter import ttk, messagebox
from operations import add_book, view_books, delete_book, update_book, get_book

# ---------------- Config ----------------
BG = "#f7f9fc"
ACCENT = "#2b6cb0"
FONT = ("Segoe UI", 10)
TITLE_FONT = ("Segoe UI", 18, "bold")

# ---------------- App ----------------
root = tk.Tk()
root.title("Library Management System")
root.geometry("850x600")
root.configure(bg=BG)
root.resizable(True, True)

# ---------------- State ----------------
editing_id = None  # None when adding, set to id when editing

# ---------------- Functions ----------------
def show_status(msg):
    status_var.set(msg)

def get_all_books():
    try:
        return list(view_books())
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch books:\n{e}")
        return []

def refresh_table(filtered=None):
    for r in tree.get_children():
        tree.delete(r)
    books = filtered if filtered is not None else get_all_books()
    for book in books:
        tree.insert("", "end", values=book)
    show_status(f"{len(books)} books displayed")

def clear_form():
    global editing_id
    editing_id = None
    title_var.set("")
    author_var.set("")
    year_var.set("")
    search_var.set("")
    title_entry.focus_set()
    submit_btn.config(text="Add Book")

def validate_inputs(title, author, year):
    if not title.strip() or not author.strip() or not year.strip():
        messagebox.showwarning("Validation", "All fields are required.")
        return False
    if not year.isdigit() or not (0 < int(year) <= 9999):
        messagebox.showwarning("Validation", "Year must be a valid number (1-9999).")
        return False
    return True

def on_submit():
    global editing_id
    title = title_var.get()
    author = author_var.get()
    year = year_var.get()
    if not validate_inputs(title, author, year):
        return
    try:
        if editing_id is None:
            rowid = add_book(title.strip(), author.strip(), int(year))
            show_status(f"Book added (ID {rowid}).")
        else:
            updated = update_book(editing_id, title.strip(), author.strip(), int(year))
            if updated:
                show_status(f"Book ID {editing_id} updated.")
            else:
                show_status(f"No changes applied to ID {editing_id}.")
            editing_id = None
            submit_btn.config(text="Add Book")
        clear_form()
        refresh_table()
    except Exception as e:
        messagebox.showerror("Error", f"Could not save book:\n{e}")

def delete_record():
    sel = tree.focus()
    if not sel:
        messagebox.showwarning("Delete", "Select a record to delete.")
        return
    item = tree.item(sel)
    book_id, title = item["values"][0], item["values"][1]
    if not messagebox.askyesno("Confirm Delete", f"Delete '{title}' (ID: {book_id})?"):
        return
    try:
        deleted = delete_book(book_id)
        if deleted:
            refresh_table()
            show_status("Book deleted.")
            clear_form()
        else:
            messagebox.showinfo("Delete", "No record deleted.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete:\n{e}")

def on_row_double_click(event):
    global editing_id
    sel = tree.focus()
    if not sel:
        return
    book_id, title, author, year = tree.item(sel)["values"]
    # populate form for editing
    editing_id = book_id
    title_var.set(title)
    author_var.set(author)
    year_var.set(year)
    submit_btn.config(text="Save Changes")
    show_status(f"Editing ID {book_id}. Make changes and click 'Save Changes'.")

def search_records(*_):
    query = search_var.get().strip().lower()
    if not query:
        refresh_table()
        return
    all_books = get_all_books()
    filtered = []
    for b in all_books:
        if any(query in str(field).lower() for field in b[1:]):  # ignore ID
            filtered.append(b)
    refresh_table(filtered)

# Sorting support
sort_col = None
sort_reverse = False
def sort_by(col_index):
    global sort_col, sort_reverse
    all_items = [tree.item(i)["values"] for i in tree.get_children()]
    try:
        all_items.sort(key=lambda x: (x[col_index] if x[col_index] is not None else ""), reverse=sort_reverse)
    except Exception:
        all_items.sort(key=lambda x: str(x[col_index]), reverse=sort_reverse)
    sort_reverse = not sort_reverse
    # refresh_table expects list of tuples/rows
    refresh_table(all_items)

# ---------------- Styles & Layout ----------------
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", font=FONT, rowheight=26, fieldbackground="white")
style.configure("TLabel", background=BG, font=FONT)
style.configure("TButton", font=FONT)
style.configure("Header.TFrame", background=ACCENT)
style.map("TButton", background=[("active", "#1f4f7a")])

# Header
header = tk.Frame(root, bg=ACCENT)
header.pack(fill="x")
tk.Label(header, text="📚 Library Management", font=TITLE_FONT, bg=ACCENT, fg="white", padx=12, pady=10).pack(side="left")

# Main frame
main = tk.Frame(root, bg=BG, padx=12, pady=12)
main.pack(fill="both", expand=True)

# Left: form area
form_frame = tk.Frame(main, bg=BG)
form_frame.grid(row=0, column=0, sticky="n", padx=(0,12))

title_var = tk.StringVar()
author_var = tk.StringVar()
year_var = tk.StringVar()
search_var = tk.StringVar()
status_var = tk.StringVar()

tk.Label(form_frame, text="Title:", bg=BG).grid(row=0, column=0, sticky="w", pady=4)
title_entry = ttk.Entry(form_frame, textvariable=title_var, width=30)
title_entry.grid(row=0, column=1, pady=4)

tk.Label(form_frame, text="Author:", bg=BG).grid(row=1, column=0, sticky="w", pady=4)
author_entry = ttk.Entry(form_frame, textvariable=author_var, width=30)
author_entry.grid(row=1, column=1, pady=4)

tk.Label(form_frame, text="Year:", bg=BG).grid(row=2, column=0, sticky="w", pady=4)
year_entry = ttk.Entry(form_frame, textvariable=year_var, width=30)
year_entry.grid(row=2, column=1, pady=4)

btn_frame = tk.Frame(form_frame, bg=BG)
btn_frame.grid(row=3, column=0, columnspan=2, pady=(10,0))
submit_btn = ttk.Button(btn_frame, text="Add Book", command=on_submit)
submit_btn.pack(side="left", padx=4)
ttk.Button(btn_frame, text="Delete Selected", command=delete_record).pack(side="left", padx=4)
ttk.Button(btn_frame, text="Clear", command=clear_form).pack(side="left", padx=4)
ttk.Button(btn_frame, text="Refresh", command=refresh_table).pack(side="left", padx=4)

# Right: table & search
right_frame = tk.Frame(main, bg=BG)
right_frame.grid(row=0, column=1, sticky="nsew")
main.grid_columnconfigure(1, weight=1)
main.grid_rowconfigure(0, weight=1)

search_box = ttk.Entry(right_frame, textvariable=search_var, width=40)
search_box.pack(anchor="ne")
search_box.bind("<KeyRelease>", search_records)

columns = ("ID", "Title", "Author", "Year")
tree = ttk.Treeview(right_frame, columns=columns, show="headings", selectmode="browse")
for i, col in enumerate(columns):
    tree.heading(col, text=col, command=lambda c=i: sort_by(c))
    tree.column(col, anchor="w", width=120 if col != "Title" else 300)

vsb = ttk.Scrollbar(right_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
tree.pack(fill="both", expand=True, pady=(6,0))

tree.bind("<Double-1>", on_row_double_click)

# Status bar
status = ttk.Label(root, textvariable=status_var, anchor="w", background="#e9eef6", font=("Segoe UI", 9))
status.pack(fill="x", side="bottom")

# ---------------- Initialize ----------------
clear_form()
refresh_table()
show_status("Ready")

root.mainloop()
