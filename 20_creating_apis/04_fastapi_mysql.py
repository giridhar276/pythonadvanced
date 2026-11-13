"""
Example 04: REST API using FastAPI and MySQL

Concept:
The same database GET and POST operations as Example 03, using FastAPI.

Prerequisite: Run your earlier CSV-to-MySQL import program.
"""

import pymysql
from fastapi import FastAPI, HTTPException
from db_config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

app = FastAPI(title="Employee API - FastAPI MySQL")


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
        return employees
    finally:
        connection.close()


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM employees WHERE csv_row_number = %s",
                (employee_id,)
            )
            employee = cursor.fetchone()
        if employee is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee
    finally:
        connection.close()


@app.post("/employees", status_code=201)
def add_employee(employee: dict):
    required = ["csv_row_number", "age", "education", "income"]
    if any(field not in employee for field in required):
        raise HTTPException(
            status_code=400,
            detail="Required: csv_row_number, age, education, income"
        )

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
        return {"message": "Employee inserted successfully"}
    except pymysql.err.IntegrityError:
        connection.rollback()
        raise HTTPException(status_code=409, detail="Employee ID already exists")
    finally:
        connection.close()


# Run: uvicorn 04_fastapi_mysql:app --reload
# Open: http://127.0.0.1:8000/docs
