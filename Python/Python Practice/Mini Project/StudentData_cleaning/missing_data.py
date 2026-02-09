import pandas as pd

# Load the CSV files
df1 = pd.read_csv(r'D:\Manasvi\Training\QA Training practice\Practice\Python\Python Practice\Mini Project\StudentData_cleaning\All Candidates List(Filtered and final list).csv')
df2 = pd.read_csv(r'D:\Manasvi\Training\QA Training practice\Practice\Python\Python Practice\Mini Project\StudentData_cleaning\data\output data\valid_students.csv')

# Identify rows in df1 not in df2 based on a specific column (e.g., 'id')
# The '~' acts as a 'NOT' operator, and 'isin' checks for existence
missing_rows = df1[~df1['Email ID'].isin(df2['email'])]

# Print the missing rows
print(missing_rows)

# Optionally, save the result to a new CSV
missing_rows.to_csv('missing_in_file2.csv', index=False)