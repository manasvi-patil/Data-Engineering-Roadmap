#normalizes messy data input
#cleaning the data according to our requirement

class Clean_data:
    def clean_email(self, email):
        if not email:
            return email
        return email.replace(" ", "").strip().lower()
    
    def clean_yearOfGraduation(self, year):
        if year is None:
            return None
        year = str(year).strip()
        if year.lower() in ("", "none", "null", "na"): #handle CSV null-like values
            return None
        
        if year.isdigit() and len(year) == 2: #2-digit year
            return int("20" + year)
        
        if "-" in year:  #for 2024-25 & 24-2025
            parts = year.split("-")
            last_part = parts[-1].strip()

            if last_part.isdigit() and len(last_part) == 2:
                return int("20" + last_part)
            if last_part.isdigit() and len(last_part) == 4:
                return int(last_part)
            return None
        
        if year.isdigit() and len(year) == 4: #full year "2025"
            return int(year)
        return None

    # def clean_yearOfGraduation(self, year):
    #     year = str(year)
        
    #     if len(year) == 2: 
    #         return int("20" + year)
    #     if "-" in year: #for 2024-25
    #         return int("20" + year.split("-")[-1])
    #     if len(year) == 4: 
    #         return int(year)
    #     return year

    def clean_location(self, location):
        if location:
            return location.lower().strip()
        else:
            return location
    