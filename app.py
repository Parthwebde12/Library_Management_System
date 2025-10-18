from flask import Flask, render_template, request, redirect
import pyodbc

app = Flask(__name__)

conn = pyodbc.connect(
    'DRIVER={MySQL ODBC 8.0 ANSI Driver};'
    'SERVER=localhost;'
    'DATABASE=college;'
    'USER=root;'
    'PASSWORD=parth1611;'
)
cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template('index.html', data=data)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/insert', methods=['POST'])
def insert():
    roll = request.form['roll']
    name = request.form['name']
    course = request.form['course']
    marks = request.form['marks']
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (roll, name, course, marks))
    conn.commit()
    return redirect('/')

@app.route('/edit/<int:roll>')
def edit(roll):
    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll,))
    data = cursor.fetchone()
    return render_template('edit.html', student=data)

@app.route('/update/<int:roll>', methods=['POST'])
def update(roll):
    name = request.form['name']
    course = request.form['course']
    marks = request.form['marks']
    cursor.execute("UPDATE students SET name=?, course=?, marks=? WHERE roll_no=?", (name, course, marks, roll))
    conn.commit()
    return redirect('/')

@app.route('/delete/<int:roll>')
def delete(roll):
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll,))
    conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
