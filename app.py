from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory list of employees
employees = [
    {"id": 1, "name": "Alice", "role": "Developer"},
    {"id": 2, "name": "Bob", "role": "Manager"},
]

@app.route("/")
def home():
    return "Employee Management System API is running"

@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()
    employees.append(data)
    return jsonify({"message": "Employee added successfully"}), 201

@app.route("/employees/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return jsonify(emp), 200
    return jsonify({"error": "Employee not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
# Triggering CI/CD
