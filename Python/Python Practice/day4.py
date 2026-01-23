#Functions
#--> A function is a reusable block of code that performs a task.
#returns = sends values back, reusable, returns value; 
#print = shows output, can't reuse, returns None

#Parameter and Argument
def process_score(score):  #score = argument
    return score
result = process_score(40)  #40 = parameter

#Task
scores = [30, 140, 60, 75, -8.9, 49]

def processed_score(scores, max_score = 100):
    if scores is None or scores < 0 or scores > max_score:
        return "Invalid"
    normalized = scores / max_score

    if normalized >= 0.75:
        grade = "Excellent"
    elif normalized >= 0.50:
        grade = "Pass"
    else:
        grade = "Fail"
 
    return normalized, grade  #tuple is returned

for score in scores:
    result = processed_score(score)
    
    if result is "Invalid":
        print(f"The Score {score} is Invalid")
    else:
        normalized, grade = result  #tuple unpacking
        print(f"The Score is {score}, normalized score is {normalized} and grade is {grade}")

#Lambda functions
#--> Lambda expressions allow us to create "anonymous" functions. This basically means we can quickly make ad-hoc functions without needing to properly define a function using def.

def square(num):  #this is normal function in standard way
    result = num**2
    return result
square(2)

#Now using lamda function
square_lambda = lambda num: num**2
square_lambda(2)