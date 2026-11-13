"""
Example 01: REST API using FastAPI (without a database)

Concept:
GET reads employee JSON data stored in Python.
POST adds a new employee to the Python list.
"""

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Employee API - FastAPI JSON")

employees = [
    {"id": 1, "name": "Arjun", "department": "IT", "salary": 60000},
    {"id": 2, "name": "Priya", "department": "HR", "salary": 50000}
]


@app.get("/employees")
def get_employees():
    return employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")


@app.post("/employees", status_code=201)
def add_employee(employee: dict):
    required = ["id", "name", "department", "salary"]
    if any(field not in employee for field in required):
        raise HTTPException(status_code=400, detail="Missing employee fields")

    if any(existing["id"] == employee["id"] for existing in employees):
        raise HTTPException(status_code=409, detail="Employee ID already exists")

    employees.append(employee)
    return {"message": "Employee added successfully", "employee": employee}


# Run: uvicorn 01_fastapi_json:app --reload
# Open: http://127.0.0.1:8000/docs
