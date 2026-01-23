#JSON Handling
import json
data = '{"emp_id": 101, "salary":80000}'
python_data = json.loads(data)
print(python_data["salary"])
if python_data["salary"] > 50000:
    print("High Salary")
else:
    print("Low Salary")

#Error Handling
#--> e is the error object (or exception message). When an error happens, Python stores details about that error in e.
#--> Exception = type of error; e = actual error message
employees = [
    {"name": "Asha", "salary": 70000},
    {"name": "Ravi", "salary": None},
    {"name": "Neha", "salary": "90000"}
]

for emp in employees:
    try:
        salary = emp["salary"]
        tax = salary * 0.1
        print(f"{emp['name']} tax: {tax}")
    except Exception as e:
        print(f"Error for {emp['name']}: {e}")

#2 
data = [10, 20, 0, "abc", 50]
for d in data:
    try:
        result = 100/d
        print(result)
    except Exception as e:
        print(f"Invalid value: {result}")
        print(f"Error for {result}: {e}")

for d in data:
    try:
        num = int(d)
        print(num)
    except ValueError:
        print(f"Invalid number: {d}")

#3
try:
    x = 10 + "abc"
except Exception as e:
    print(e)

#Types of Exception types
#BaseException
#|- Exception
#    |- ValueError - TypeError - ZeroDivisionError - KeyError - IndexError
#Exception = general error class
#ValueError, TypeError, etc = specific type of exceptions

#ValueError
#--> When value is missing
a = int("abc")
print(a)

#TypeError
#--> When datatypes are incompatible
b = 10 + 'abc'
print(b)

#KeyError
#--> When invalid key is called
d = {"name": "Asha"}
print(d["salary"])

#IndexError
#--> When called index is incorrect
lst = [1, 2]
print(lst[5])

#| Error Type        | Meaning                |
#| ----------------- | ---------------------- |
#| ValueError        | Wrong value            |
#| TypeError         | Wrong data type        |
#| KeyError          | Missing dictionary key |
#| IndexError        | Wrong list index       |
#| ZeroDivisionError | Divide by zero         |
