<div class="banner">
    <h1>COMING SOON</h1>
</div>

<style>
.banner{display:flex;justify-content:center;padding:20px}
.banner h1{font-family:Arial,Helvetica,sans-serif;font-size:34px;color:#333;margin:0;
    animation:fadeMove 2s ease-in-out infinite}
@keyframes fadeMove{
    0%{opacity:0.2;transform:translateY(-8px)}
    50%{opacity:1;transform:translateY(0)}
    100%{opacity:0.2;transform:translateY(-8px)}
}
.container{max-width:760px;margin:18px auto;font-family:Arial,Helvetica,sans-serif;color:#222;padding:0 16px}
.card{border:1px solid #eaeaea;padding:14px;border-radius:6px;background:#fff}
code, pre{background:#f6f6f6;padding:6px;border-radius:4px}
</style>

<div class="container card">
# Student Management System (DBMS Mini Project)

A minimal, fixed, and simple web-based app using Python (Flask) with MySQL via ODBC (pyodbc). Basic CRUD: Add, View, Update, Delete student records.

## Tech Stack
- Python (Flask)
- MySQL
- ODBC (pyodbc)

## Folder Structure
```bash
student_db_app/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── ... (add/update/delete/view)
└── static/
        └── style.css
```

## Quick start
```bash
# clone
git clone https://github.com/parthwebde12/student_db_app.git
cd student_db_app

# dependencies
pip install flask pyodbc

# run
python app.py
```

</div>
