#Dictionary in pipeline
def process_employee(emp):
    salary = emp.get("salary")

    if salary is None or salary < 0:
        emp["status"] = "Invalid"
        return emp

    tax = salary * 0.10
    emp["tax"] = tax
    emp["status"] = "Processed"
    return emp

employee = {
    "emp_id": 201,
    "salary": 75000
}

result = process_employee(employee)
print(result)

#Task2
employees = [
    {"emp_id": 101, "name": "Asha", "salary": 70000, "department": "IT"},
    {"emp_id": 102, "name": "Ravi", "salary": None, "department": "HR"},
    {"emp_id": 103, "name": "Neha", "salary": 60000, "department": "IT"},
    {"emp_id": 104, "name": "Amit", "salary": -5000, "department": "Finance"},
    {"emp_id": 105, "name": "Sara", "salary": 90000, "department": "Finance"}
]

valid_count = 0
invalid_count = 0

for emp in employees:
    salary = emp.get("salary")
    department = emp.get("department")
    name = emp.get("name")

    if salary > 0 and department == "IT":
        emp["salary_status"] = "Valid"
        valid_count += 1

        if "Valid":
            emp["tax"] = 0.1 * salary
    else:
        emp["salary status"] = "Invalid"
        invalid_count += 1

print(f"Valid employees: {valid_count}, Invalid employees: {invalid_count}, IT Department: {name}")
