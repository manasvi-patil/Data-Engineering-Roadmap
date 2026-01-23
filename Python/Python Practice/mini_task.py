#1. Validate Salary: 
#   - salary must be > 0; otherwise mark as "Invalid"
#2. Calculate tax
#   - tax = 10% of salary
#3. Assign grade
#   - salary >= 100000 -->"Very High"
#   - salary >= 80000 -->"High"
#   - salary >= 50000 -->"Medium"
#   - else -->"Low"
#4. Count valid & Invalid records

employees = [
    {"id": 1, "name": "Asha", "salary": 70000},
    {"id": 2, "name": "Ravi", "salary": None},
    {"id": 3, "name": "Neha", "salary": 120000},
    {"id": 4, "name": "Amit", "salary": -5000},
    {"id": 5, "name": "Sara", "salary": 90000},
    {"id": 5, "name": "Sara", "salary": 40000}
]


def process_employee(emp):
    try:
        salary = emp["salary"]

        if salary is None or salary <= 0:
            return {"status": "Invalid"}
        tax = salary * 0.1

        if salary >= 100000:
            grade = "Very High"
        elif salary >= 80000:
            grade = "High"
        elif salary >= 50000:
            grade = "Medium"
        else:
            grade = "low"

        return {"status": "Valid", "tax": tax, "grade": grade}
    
    except Exception as e:
        return {"status": "Error", "error": str(e)}

#Process all employees
valid_count = 0
invalid_count = 0

for emp in employees:
    result = process_employee(emp)

    if result["status"] == "Valid":
        emp["tax"] = result["tax"]
        emp["grade"] = result["grade"]
        valid_count += 1
    else:
        emp["status"] = "Invalid"
        invalid_count += 1

#Print results
print("Process Employees:")
for emp in employees:
    print(emp)
print("Valid employees:", valid_count)
print("Invalid employees:", invalid_count)