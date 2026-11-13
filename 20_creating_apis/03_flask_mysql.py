"""
Example 03: REST API using Flask and MySQL

Concept:
GET reads records from the existing employees table.
POST inserts a new record into that table.

Prerequisite: Run your earlier CSV-to-MySQL import program.
"""

import pymysql
from flask import Flask, jsonify, request
from db_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

app = Flask(__name__)


def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )


@app.get("/employees")
def get_employees():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM employees ORDER BY csv_row_number LIMIT 20")
            employees = cursor.fetchall()
        return jsonify(employees)
    finally:
        connection.close()


@app.get("/employees/<int:employee_id>")
def get_employee(employee_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM employees WHERE csv_row_number = %s",
                (employee_id,)
            )
            employee = cursor.fetchone()
        if employee is None:
            return jsonify({"error": "Employee not found"}), 404
        return jsonify(employee)
    finally:
        connection.close()


@app.post("/employees")
def add_employee():
    employee = request.get_json(silent=True)
    required = ["csv_row_number", "age", "education", "income"]

    if not isinstance(employee, dict) or any(field not in employee for field in required):
        return jsonify({"error": "Required: csv_row_number, age, education, income"}), 400

    insert_query = """
    INSERT INTO employees (csv_row_number, age, education, income)
    VALUES (%s, %s, %s, %s)
    """
    employee_data = (
        employee["csv_row_number"], employee["age"],
        employee["education"], employee["income"]
    )

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(insert_query, employee_data)
        connection.commit()
        return jsonify({"message": "Employee inserted successfully"}), 201
    except pymysql.err.IntegrityError:
        connection.rollback()
        return jsonify({"error": "Employee ID already exists"}), 409
    finally:
        connection.close()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
