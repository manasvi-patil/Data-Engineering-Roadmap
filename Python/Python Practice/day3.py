#Conditional Statements

#If,elif,else Statements
a = 6
b = 4
if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater than a")
else:
    print("a and b are equal")

#2 For Loops
#--> A for loop acts as an iterator in Python, it goes through items that are in a sequence 

#For Loop
list1 = list(range(10))
for lists in list1:
    if lists % 2 == 0:
        print(f"this is an even number {lists}")
    else:
        print(f"This is an odd number {lists}")

#While loop
#--> A while statement will repeatedly execute a single statement or group of statements as long as the condition is true

#Task 1
# Modify the code to:
# Skip even numbers
# Stop when number > 15
num = 1

while num < 20:
    if num > 15:
        print("loop is stopped")
        break
    
    if num % 2 == 0:
        num += 1
        continue
    
    print(f"Processing num: {num}")
    num += 1 

#Task 2 
#Valid score: 0 <= score <= 100
# Invalid score:
#  - None
#  - Negative number
#  - Greater than 100
# If invalid count exceeds 3, stop pipeline
scores = [78, None, 45, -10, 92, 67, None, 105, 88]
index = 0
invalid_index = 0
while index <len(scores):
    score = scores[index]

    #Invalid data check
    if score is None or score < 0 or score > 100:
        invalid_index += 1
        print(f"Invalid entry found at {index}")
        
        if invalid_index > 3:
            print("Stop this pipeline too many invalid entries")
            break

        index += 1
        continue

    #valid data processing
    if score >= 75:
        grade = "Distinction"
    elif score >= 50:
        grade = "Pass"
    else:
        grade = "Fail"

    print(f"Scores: {score}, Grade: {grade}")
    index += 1
  
#Task 3
# Modify the code to:
# - Stop pipeline if invalid_count == 2
# - Print total valid records processed
# When done, reply: “Loops & conditionals clear”

bucket = [9, None, 78, -8.6, 99, 108, 13, None, 67]
index = 0
invalid_data = 0
valid_count = 0

while index < len(bucket):
    items = bucket[index]

    if items is None or items > 100 or items < 0:
        print(f"Invalid entries: {items} and index: {index}")
        invalid_data += 1

        if invalid_data == 2:
            print("Stop pipeline")
            break
        index += 1
        continue
    print("Loops & conditionals clear")
    valid_count += 1

    #data processing
    if items >= 75:
        marks = "Excellent"
    elif items >= 20:
        marks = "Pass"
    else:
        marks = "Fail"

    print(f"Marks obtained: {items}, Grades assigned: {marks}")
    index += 1
print(f"The valid entries are: {valid_count}")