#2 making object-based pipeline

students_data = [
    {"firstName": "Ron", "lastName": "Ginger", "email": "ron @gmail.com", "phone": "1231456", "year": "2024-25", "collegeName": "ABC", "location": "Mumbai", "pointer": 8.5},
    {"firstName": "Sam", "lastName": "Smith", "email": "sam@gmail.com", "phone": "1234956", "year": "2025", "collegeName": "PQR", "location": "Delhi", "pointer": 9.1},
    {"firstName": "Amit", "lastName": "Sawant", "email": " amitgmail.com", "phone": "1531456", "year": "25", "collegeName": "XYZ", "location": "Borivali", "pointer": 7.2},
    {"firstName": "Neha", "lastName": "Agarwal", "email": "neha@gmail .com", "phone": "1231486", "year": "2024", "collegeName": "MNO", "location": "Virar", "pointer": 11}
]

class Student:
    def __init__(self, firstName, lastName, email, phoneNo, yearOfPassing, collegeName, location, pointer):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phoneNo = phoneNo
        self.yearOfPassing = yearOfPassing
        self.collegeName = collegeName
        self.location = location
        self.pointer = pointer
    
    def __repr__(self):
        return (
            f"Student(Name={self.firstName} {self.lastName}, "
            f"Email={self.email}, Year={self.yearOfPassing}, "
            f"College={self.collegeName}, Location={self.location}, "
            f"Pointer={self.pointer})"
        )
    # def get_privateInfo(self):
    #     return self.__emailID
    
    # def set_email(self, email):
    #     self.__emailID = email

class Clean_data:
    def clean_email(self, email):
        return email.replace(" ", "").strip()

    def clean_yearOfGraduation(self, year):
        year = str(year)
        if year == "25" or "-" in year: #for 2024-25
            return 2025
        elif year == "2025": 
            return 2025
        return "Invalid Entry"

    def clean_location(self, location):
        return location.strip().title()
    
class DataValidator:
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

class DataProcessor:
    def __init__(self):
        self.cleaner = Clean_data()
        self.validator = DataValidator()
        self.valid_students = []
        self.invalid_students = []

    def process(self, student):
        reasons = []  #It resets for each student because reasons is a mutable list, it keeps memory across iterations
        #cleaning
        student.email = self.cleaner.clean_email(student.email)  #calling object
        # email = self.cleaner.clean_email(student.get_email())  #use this when email is encapsulated
        # student.set_email(email)
        student.yearOfPassing = self.cleaner.clean_yearOfGraduation(student.yearOfPassing)
        student.location = self.cleaner.clean_location(student.location)

        #Validate
        if not self.validator.validate_email(student.email):
            reasons.append("Invalid Email")
        if not self.validator.validate_year(student.yearOfPassing):
            reasons.append("Invalid Year")
        if not self.validator.validate_location(student.location):
            reasons.append("Invalid Location")
        
        if reasons:
            self.invalid_students.append({"student": f"{student.firstName} {student.lastName}", "reason": reasons})
        else:
            self.valid_students.append(student)

#driver code
processor = DataProcessor()

student_obj = []
for data in students_data:
    s = Student(
        data["firstName"],
        data["lastName"],
        data["email"],
        data["phone"],
        data["year"],
        data["collegeName"],
        data["location"],
        data["pointer"]
    )
    student_obj.append(s)

for s in student_obj:
    processor.process(s)

print("Valid students: ", processor.valid_students)
print("Valid students: ", len(processor.valid_students))
print("Invalid students: ", processor.invalid_students)
print("Valid students: ", len(processor.invalid_students))