import pyodbc

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={MySQL ODBC 8.0 Unicode Driver};'
        'SERVER=localhost;'
        'DATABASE=library_db;'
        'USER=root;'
        'PASSWORD=parth1611;'
        'charset=utf8mb4;'
    )
    return conn
