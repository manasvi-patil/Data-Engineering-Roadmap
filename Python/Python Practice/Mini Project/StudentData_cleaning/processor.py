#here we will combine all cleaner, validator and student files data and decide the flow
import csv
import json
from student import Student
from cleaner import Clean_data
from validator import DataValidator

class DataProcessor:
    def __init__(self, config_path):
        with open(config_path, "r") as f:  #reading the config json
            self.config = json.load(f)

        self.cleaner = Clean_data()
        self.validator = DataValidator(self.config)
        self.valid_students = []
        self.invalid_students = []

    def process_csv(self, input_csv):
        with open(input_csv, newline="", encoding="utf-8") as f:  #reading csv
            reader = csv.DictReader(f)

            for row in reader:
                student = Student(row, self.config["csv_column_mapping"])

                #Cleaning data
                student.email = self.cleaner.clean_email(student.email)  #calling object
                student.yearOfPassing = self.cleaner.clean_yearOfGraduation(student.yearOfPassing)
                student.location = self.cleaner.clean_location(student.location)
                
                #Validating data
                reasons = []  #It resets for each student because reasons is a mutable list, it keeps memory across iterations

                if not self.validator.validate_email(student.email):
                    reasons.append("Invalid Email")
                if not self.validator.validate_year(student.yearOfPassing):
                    reasons.append("Invalid Year")
                if not self.validator.validate_location(student.location):
                    reasons.append("Invalid Location")
                    
                if reasons:
                    self.invalid_students.append({"student": student.to_dict(), "reason": reasons})
                    # print("Invalid students saved")
                else:
                    filtered_student = {
                         col: student.to_dict().get(col)
                         for col in self.config["valid_output_columns"]
                    }
                    self.valid_students.append(filtered_student)

    def write_csv(self, filename, data):
        if not data:
            print(f"No data to write in {filename}")
            return
        
        with open(filename, "w", newline="", encoding="utf-8") as f:  #creating csv file using dictionary keys as column headers
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
