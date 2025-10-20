from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# ✅ Database connection function
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="--",           # your MySQL username
        password="--",  # 🔹 replace with your MySQL password
        database="company"
    )

# 🏠 Home Page
@app.route('/')
def home():
    return render_template('index.html')

# ➕ Add Employee Page
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (name, age, email) VALUES (%s, %s, %s)", (name, age, email))
        conn.commit()
        conn.close()
        return redirect('/view')
    return render_template('add_employee.html')

# 👁️ View Employees Page
@app.route('/view')
def view_employee():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    conn.close()
    return render_template('view_employee.html', employees=data)

if __name__ == '__main__':
    app.run(debug=True)
