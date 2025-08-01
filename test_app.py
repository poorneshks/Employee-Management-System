from app import app

def test_get_employees():
    tester = app.test_client()
    response = tester.get("/employees")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "id" in data[0]
    assert "name" in data[0]
    assert "role" in data[0]

def test_add_employee():
    tester = app.test_client()
    new_emp = {"id": 3, "name": "Charlie", "role": "Tester"}
    response = tester.post("/employees", json=new_emp)
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Employee added successfully"

def test_get_employee_by_id():
    tester = app.test_client()
    response = tester.get("/employees/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1
    assert "name" in data
    assert "role" in data
