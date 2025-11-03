# Library Management System (DBMS-mini-Project)

A lightweight desktop Library Management System built with Python (Tkinter) and MySQL using ODBC (pyodbc). This app provides a simple GUI for basic library CRUD operations — add, view, update, and delete books — and is intended as a DBMS mini-project or learning reference.

---

Table of contents
- About
- Features
- Demo
- Tech stack
- Quick start
  - Clone
  - Dependencies
  - Database (SQL)
  - Configure connection (examples)
  - Run
- Usage (UI overview)
- Troubleshooting
- Security notes
- Packaging
- Roadmap / Improvements
- Contributing
- License
- Contact

---

About
This repository contains a small Tkinter application that connects to a MySQL database through an ODBC layer (pyodbc). It is designed to be simple, easy to set up, and educational — good for demonstrating database connectivity and basic GUI-driven CRUD patterns in Python.

Features
- Add new books (title, author, year, publisher, ISBN, quantity)
- Browse and search the book list
- Update and delete book records
- Clean, minimal Tkinter GUI
- Works with ODBC (DSN or DSN-less) using pyodbc

Demo
(Replace these with real screenshots or GIFs)
- Main list view showing books
- Add / Edit form dialog
- Confirmation prompt for delete actions

---

Tech stack
- Python 3.8+
- Tkinter (GUI)
- MySQL (database server)
- ODBC driver for MySQL (platform-specific)
- pyodbc (Python ODBC driver)

---

Quick start

1) Clone
```bash
git clone https://github.com/Parthwebde12/DBMS-mini-Project.git
cd DBMS-mini-Project
```

2) Create a virtual environment and install dependencies
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
# If there is no requirements.txt:
pip install pyodbc
```

requirements.txt (example)
```text
pyodbc>=4.0.30
```

3) Create the database and table
Connect to your MySQL server and run:
```sql
CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

CREATE TABLE IF NOT EXISTS books (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255),
  year INT,
  publisher VARCHAR(255),
  isbn VARCHAR(50),
  quantity INT DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

4) Configure ODBC / DB connection
Option A — Using a DSN (recommended for end users)
- Create an ODBC DSN (e.g., `LibraryDSN`) using your platform's ODBC manager and point it to `library_db`.

Option B — DSN-less connection (useful for development)
- Replace values below with your server credentials.

Example config.py (create in project root)
```python
# config.py
USE_DSN = False  # set True to use DSN

# If using DSN
DSN = "LibraryDSN"
DB_USER = "myuser"
DB_PASS = "mypassword"

# If using DSN-less
DSN_LESS_CONN_STR = (
    "DRIVER={MySQL ODBC 8.0 ANSI Driver};"
    "SERVER=127.0.0.1;"
    "PORT=3306;"
    "DATABASE=library_db;"
    "UID=myuser;"
    "PWD=mypassword;"
    "OPTION=3;"
)
```

Secure alternative: use environment variables (recommended)
```python
import os
conn_str = (
    "DRIVER={MySQL ODBC 8.0 ANSI Driver};"
    f"SERVER={os.environ['DB_HOST']};"
    f"PORT={os.environ.get('DB_PORT','3306')};"
    f"DATABASE={os.environ['DB_NAME']};"
    f"UID={os.environ['DB_USER']};"
    f"PWD={os.environ['DB_PASS']};"
)
```

5) Run the app
```bash
python app.py
```
The main window should open. Use the UI to add, edit, delete and search books.

---

Usage (UI overview)
- Add Book: opens a form to enter book details, then saves to DB.
- Edit: select a book in the list and click Edit to update record.
- Delete: select a book and click Delete. A confirmation prompt prevents accidental deletion.
- Search / Filter: type a search term to filter displayed books (if implemented).

---

Troubleshooting
- ODBC driver not found / driver name mismatch:
  - Verify installed driver name. On Windows, check ODBC Data Source Administrator.
  - For DSN-less, make sure the DRIVER value matches the installed driver (e.g., "MySQL ODBC 8.0 Unicode Driver").
- pyodbc cannot connect:
  - Test connection using the mysql client or another DB tool.
  - Confirm user credentials and that the user has privileges on library_db.
  - Ensure port (usually 3306) is open and accessible.
- "Data source name not found and no default driver specified":
  - If using DSN: confirm the DSN exists and is the correct type (User vs System).
  - Otherwise use DSN-less connection with a correct DRIVER string.
- Permissions errors:
  - Grant the MySQL user appropriate privileges: GRANT ALL on library_db.* TO 'user'@'host';

---

Security notes
- Do not commit credentials or DSN with passwords to version control.
- Prefer environment variables or an encrypted secret manager for production.
- Validate user input before inserting into the database to avoid injection vulnerabilities — using parameterized queries via pyodbc prevents SQL injection.

---

Packaging
To distribute this app on Windows, consider PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile app.py
```
Note: ODBC drivers must be present on the target machine — bundling them is platform-specific.

---

Roadmap / Improvements
- Add robust search and filtering UI
- Pagination for large datasets
- User authentication / multi-user roles (librarian vs member)
- Improved validation and richer error handling
- Import/export (CSV, JSON)
- Unit tests & CI (GitHub Actions)
- Desktop packaging for Windows/macOS/Linux

---

Contributing
Contributions are welcome!
1. Fork the repository
2. Create a branch: git checkout -b feature/my-feature
3. Make changes and add tests where appropriate
4. Open a Pull Request describing your changes and rationale

Please follow consistent coding style and do not commit secrets.
