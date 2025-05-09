from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Connection function to ensure fresh connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="00000",
        database="jala_academy"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read')
def read():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', employees=rows)

@app.route('/create', methods=['POST'])
def create():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        name = request.form['name']
        department = request.form['department']
        salary = request.form['salary']
        joining_date = request.form['join_date']
        city = request.form['city']
        
        # Insert without specifying id (let it auto-increment)
        query = "INSERT INTO employees (name, department, salary, joining_date, city) VALUES (%s, %s, %s, %s, %s)"
        values = (name, department, salary, joining_date, city)
        cursor.execute(query, values)
        conn.commit()
        
        cursor.close()
        conn.close()
        return redirect(url_for('read'))
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return f"Database error: {err}", 500

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'GET':
        cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
        employee = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('update.html', employee=employee)
    
    if request.method == 'POST':
        try:
            name = request.form['name']
            department = request.form['department']
            salary = request.form['salary']
            joining_date = request.form['join_date']
            city = request.form['city']
            
            query = """
            UPDATE employees 
            SET name = %s, department = %s, salary = %s, joining_date = %s, city = %s
            WHERE id = %s
            """
            values = (name, department, salary, joining_date, city, id)
            cursor.execute(query, values)
            conn.commit()
            
            cursor.close()
            conn.close()
            return redirect(url_for('read'))
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            return f"Database error: {err}", 500

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM employees WHERE id = %s", (id,))
    conn.commit()
    
    cursor.close()
    conn.close()
    return redirect(url_for('read'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        search_id = request.form['searchId']
        cursor.execute("SELECT * FROM employees WHERE id = %s", (search_id,))
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        return render_template('index.html', search_result=result)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)