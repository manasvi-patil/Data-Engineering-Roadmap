#2 Adding list of students and storing valid & invalid students separately

students_data = [
    {"firstName": "Ron", "lastName": "Ginger", "email": "ron @gmail.com", "phone": "1231456", "year": "2024-25", "collegeName": "ABC", "location": "Mumbai", "pointer": 8.5},
    {"firstName": "Sam", "lastName": "Smith", "email": "sam@gmail.com", "phone": "1234956", "year": "2025", "collegeName": "PQR", "location": "Delhi", "pointer": 9.1},
    {"firstName": "Amit", "lastName": "Sawant", "email": " amitgmail.com", "phone": "1531456", "year": "25", "collegeName": "XYZ", "location": "Borivali", "pointer": 7.2},
    {"firstName": "Neha", "lastName": "Agarwal", "email": "neha@gmail .com", "phone": "1231486", "year": "2024", "collegeName": "MNO", "location": "Virar", "pointer": 11}
]

class Student:
    def __init__(self, firstName, lastName, emailID, phoneNo, yearOfPassing, collegeName, location):
        self.firstName = firstName
        self.lastName = lastName
        self.__emailID = emailID
        self.phoneNo = phoneNo
        self.yearOfPassing = yearOfPassing
        self.collegeName = collegeName
        self.location = location
    
    def get_privateInfo(self):
        return self.__emailID

class Clean_data:
    def clean_email(self, email):
        return email.replace(" ", "").strip()

    def clean_yearOfGraduation(self, year):
        year = str(year)
        if year == "25" or "-" in year: #
            return 2025
        elif year == "2025": #for 2024-25
            return 2025
        return "Invalid Entry"

    def clean_location(self, location):
        return location.strip().title()
    
class Validator:
    def validate_email(self, email):
        if "@" in email and "." in email:
            return True
        return False
    
    def validate_year(self, year):
        return year == 2025
    
    def validate_location(self, locationArea):
        allowed_locations = ["Andheri", "Mumbai", "Borivali", "Byculla"]
        if locationArea in allowed_locations:
            return True
        return False

valid_students = []
invalid_students = []

for student in students_data:
    reasons = []  #It resets for each student because reasons is a mutable list, it keeps memory across iterations
    # stud_info = Student() 
    cleaner = Clean_data() #creating object
    validator = Validator()

    email = cleaner.clean_email(student["email"])  #calling object
    year = cleaner.clean_yearOfGraduation(student["year"])
    location = cleaner.clean_location(student["location"])

    if validator.validate_email(email) and validator.validate_year(year) and validator.validate_location(location):
        valid_students.append(student)
    else:
        if not validator.validate_email(email):
            reasons.append("Invalid Email")
        if not validator.validate_year(year):
            reasons.append("Invalid Year")
        if not validator.validate_location(location):
            reasons.append("Invalid Location")
        
        invalid_students.append({"student": student, "reason": reasons})
            

    # print("Name: ", student["firstName"], student["lastName"] )
    # print("Email:", validator.validate_email(email))
    # print("Year:", validator.validate_year(year))
    # print("Location:", validator.validate_location(location))

print("Valid students: ", valid_students)
print("Invalid students: ", invalid_students)