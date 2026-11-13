"""
Example 02: REST API using Flask (without a database)

Concept:
The same GET and POST operations as Example 01, using Flask.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Arjun", "department": "IT", "salary": 60000},
    {"id": 2, "name": "Priya", "department": "HR", "salary": 50000}
]


@app.get("/employees")
def get_employees():
    return jsonify(employees)


@app.get("/employees/<int:employee_id>")
def get_employee(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return jsonify(employee)
    return jsonify({"error": "Employee not found"}), 404


@app.post("/employees")
def add_employee():
    employee = request.get_json(silent=True)
    required = ["id", "name", "department", "salary"]

    if not isinstance(employee, dict) or any(field not in employee for field in required):
        return jsonify({"error": "Missing employee fields"}), 400

    if any(existing["id"] == employee["id"] for existing in employees):
        return jsonify({"error": "Employee ID already exists"}), 409

    employees.append(employee)
    return jsonify({"message": "Employee added successfully", "employee": employee}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
