#Recruitment data cleaning project

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
        return location.strip()
    
class Validator:
    def validate_email(self, email):
        if "@" in email and "." in email:
            return email
        return "Invalid Email"
    
    def validate_year(self, year):
        if year == 2025:
            return f"The Year of Graduation is 2025"
    
        
    def validate_location(self, locationArea):
        allowed_locations = ["Andheri", "Mumbai", "Borivali", "Byculla"]
        if locationArea in allowed_locations:
            return locationArea
        return "This location not considered for recruitment"

#firstName, lastName, emailID, phoneNo, yearOfPassing, collegeName, location
s1 = Student("Ron", "Ginger", "ron @gmail.com", 785423698, "2024-25", "XYZ College", "Mumbai")
email = s1.get_privateInfo()
cleaner = Clean_data()
validator = Validator()

email = cleaner.clean_email(s1.get_privateInfo())
year = cleaner.clean_yearOfGraduation(s1.yearOfPassing)
location = cleaner.clean_location(s1.location)

print(email, year, location)
print("Name: ", s1.firstName, s1.lastName)
print("Email Valid:", validator.validate_email(email))
print("Year valid:", validator.validate_year(year))
print("Location valid:", validator.validate_location(location))
