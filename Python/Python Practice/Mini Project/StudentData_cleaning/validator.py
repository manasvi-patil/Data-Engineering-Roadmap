#cleaned normalized data is validated here and either rejected or accepted
from rapidfuzz import process

class DataValidator:
    def __init__(self, config):
        self.allowed_year = config["allowed_year"]
        self.allowed_locations = config["allowed_locations"]
        self.email_rules = config["email_must_contain"]

    def validate_email(self, email):
        if not email:
            return False
        return all(rule in email for rule in self.email_rules)
    
    def validate_year(self, year):
        return year == self.allowed_year
    
    def validate_location(self, location):
        if not location:
            return None
        
        match = process.extractOne(location, self.allowed_locations) #do fuzzy-matching to do string matching and save the corrected location
        if match and match[1] >= 50:
            return match[0]
        return None