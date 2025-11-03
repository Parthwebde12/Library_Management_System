# Library Management System

A simple desktop Library Management application built with Python (Tkinter) and MySQL using ODBC (pyodbc).  
This app demonstrates basic CRUD operations (Create, Read, Update, Delete) for managing books in a MySQL database with a lightweight Tkinter GUI.

---

## Features
- Add new books (title, author, year, publisher, ISBN, quantity)
- View list of books
- Update book details
- Delete books
- Simple and clean Tkinter-based user interface
- MySQL backend accessed via ODBC (pyodbc)

---

## Tech Stack
- Python 3.8+  
- Tkinter (built-in GUI toolkit)  
- MySQL (server)  
- ODBC driver for your OS (MySQL ODBC Driver / MySQL Connector/ODBC)  
- pyodbc (Python ODBC package)

---

## Prerequisites

1. Python 3.8+
2. MySQL server available and running
3. MySQL ODBC driver installed:
   - Windows: MySQL Connector/ODBC (install the MSI)
   - macOS / Linux: unixODBC + MySQL ODBC driver (install via package manager)
4. Create a System or User ODBC DSN, or use a DSN-less connection string
5. Install Python dependency:
```bash
pip install pyodbc
```

---

## Database Setup

Create a database and a simple `books` table. Example SQL:

```sql
CREATE DATABASE library_db;
USE library_db;

CREATE TABLE books (
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

---

## ODBC / Connection Setup

Option A — Using a DSN (recommended if you prefer central config):
- Create an ODBC Data Source Name (DSN) called e.g. `LibraryDSN` pointing to your `library_db`.
  - Windows: ODBC Data Source Administrator → Add → MySQL ODBC driver → configure.
  - macOS/Linux: Configure `odbc.ini` / `odbcinst.ini` or use a GUI like iODBC/ODBC Manager.

Option B — DSN-less connection (works cross-platform with correct driver name):
```python
import pyodbc

conn = pyodbc.connect(
    "DRIVER={MySQL ODBC 8.0 ANSI Driver};"
    "SERVER=127.0.0.1;"
    "PORT=3306;"
    "DATABASE=library_db;"
    "USER=myuser;"
    "PASSWORD=mypassword;"
    "OPTION=3;"
)
```
If using DSN:
```python
conn = pyodbc.connect("DSN=LibraryDSN;UID=myuser;PWD=mypassword;")
```

Notes:
- Replace driver name if you have a different version (e.g., `MySQL ODBC 8.0 Unicode Driver`).
- If you get driver not found errors, double-check the driver name and that the ODBC driver is properly installed.

---

## Run the App

1. Ensure MySQL is running and the `books` table exists.
2. Configure DSN or update connection string in the app (example: `config.py` or inside `app.py`).
3. Run:
```bash
python app.py
```

The GUI window should open and allow you to add, view, update, and delete books.

---

## Typical Project Structure (example)
- app.py            # Main Tkinter application
- config.py         # (optional) DB connection configuration
- requirements.txt  # pyodbc (if included)
- README.md

If you don't have `config.py`, check where the connection string is defined in `app.py` and update it there.

---

## Troubleshooting

- pyodbc cannot connect:
  - Verify MySQL server is running and reachable (try connecting with mysql client).
  - Verify credentials and database name are correct.
  - Verify the ODBC driver is installed and the driver name matches.
  - On Linux/macOS ensure unixODBC is installed and configured.

- "Data source name not found and no default driver specified":
  - If using DSN: ensure it exists and is defined as System/User DSN.
  - If DSN-less: use the exact installed driver name.

- Permission issues:
  - Ensure the MySQL user has privileges on the `library_db` database.

---

## Improvements / TODOs
- Add search/filtering for books
- Add user authentication
- Input validation and better error handling
- Export/Import (CSV)
- Pack into an executable (PyInstaller) for distribution

---

## Contributing
Contributions are welcome — fork the repo, add features or fixes, open a pull request. Please include:
- A clear description of the change
- Steps to reproduce (if relevant)
- Any schema or migration steps required

---

## License
Specify a license for the project (e.g., MIT). Add a LICENSE file to your repo.

---

## Contact
Created by Parthwebde12. For questions or help, open an issue in the repository.

---

If you'd like, I can:
- generate a sample config.py that contains a DSN and DSN-less template,
- produce the SQL migration file,
- or create a polished requirements.txt and a basic CONTRIBUTING.md.
Tell me which you'd like next.
