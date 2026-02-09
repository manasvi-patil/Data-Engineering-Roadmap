#defining the objects according to the data in csv to store values which we can use later for cleaning, validation and processing

class Student:
    def __init__(self, row, csv_column_mapping):  #this puts dict data into obj
        self.firstName = row.get(csv_column_mapping["firstName"])
        self.lastName = row.get(csv_column_mapping["lastName"])
        self.email = row.get(csv_column_mapping["email"])
        self.aggregatePercent = row.get(csv_column_mapping["aggregatePercent"])
        self.yearOfPassing = row.get(csv_column_mapping["yearOfPassing"])
        self.role = row.get(csv_column_mapping["role"])
        self.collegeName = row.get(csv_column_mapping["collegeName"])
        self.location = row.get(csv_column_mapping["location"])
    
    def to_dict(self):  #to_dict is used instead of dict bcus control over serialization and output schema. to_dict is a method in pandas lib which converts Dataframe or series obj to python dict
        return{    #in this data is taken out of obj
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            "aggregatePercent": self.aggregatePercent,
            "yearOfPassing": self.yearOfPassing,
            "role": self.role,
            "collegeName": self.collegeName,
            "location": self.location
        }

    def __repr__(self):
        return (
            f"{self.firstName} {self.lastName} |"
            f"{self.email}| {self.aggregatePercent} | {self.role} | {self.yearOfPassing} | {self.location}"
        )