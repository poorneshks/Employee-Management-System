from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
employees = [
    {"id": 1, "name": "Alice", "role": "Developer"},
    {"id": 2, "name": "Bob", "role": "Manager"}
]

# Get all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

# Get one employee by ID
@app.route('/employees/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    employee = next((e for e in employees if e['id'] == emp_id), None)
    return jsonify(employee) if employee else ('Not Found', 404)

# Create new employee
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    new_id = max(e['id'] for e in employees) + 1 if employees else 1
    new_employee = {"id": new_id, "name": data['name'], "role": data['role']}
    employees.append(new_employee)
    return jsonify(new_employee), 201

# Update employee
@app.route('/employees/<int:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    data = request.get_json()
    for e in employees:
        if e['id'] == emp_id:
            e['name'] = data.get('name', e['name'])
            e['role'] = data.get('role', e['role'])
            return jsonify(e)
    return ('Not Found', 404)

# Delete employee
@app.route('/employees/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    global employees
    employees = [e for e in employees if e['id'] != emp_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
