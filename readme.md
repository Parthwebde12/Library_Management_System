# 📚 Library Management System (Mini DBMS Project)

A simple **Library Management System** built for a DBMS mini project using **Python Tkinter GUI** and **SQLite** database.  
This project allows users to **add, view, update, and delete books** in the library.

---

## 🛠️ Tech Stack

- **Frontend:** Python Tkinter GUI  
- **Backend/Database:** SQLite (built-in Python library)  
- **Python Version:** 3.x  

> ✅ Note: Originally we considered MySQL + ODBC, but for simplicity and portability, we switched to SQLite. No external database setup required.

---

## 📂 Project Structure

DBMS_Mini_Project/
│
├── app.py           # Tkinter GUI for library management
├── operations.py    # Database operations (CRUD) using SQLite
└── library.db       # SQLite database file (auto-created on first run)

---

## ⚡ Features

1. **Add Book** – Add a new book with Title, Author, and Year.  
2. **View Books** – Display all books in a table.  
3. **Update Book** – Edit existing book details.  
4. **Delete Book** – Remove books from the database.  
5. **Portable** – SQLite DB means no installation or server needed.

---

## 🖥️ Screenshots


---

## 🚀 How to Run

1. Clone or download this repository.  
2. Make sure Python 3.x is installed.  
3. Open terminal or CMD in project folder:

```bash
python app.py
