#1 Strings
#--> used to record text info
#--> its a sequence and keeps track of every element in string in specific order
#--> For eg; PYTHON -> 012345  ...indexing starts at 0

#Creating String
print()  #creates line space
print('This is Day1')

#String Indexing
s = 'Hello World'
print(s[2], s[-1])

#String Concatenation and Repetition
s1 = 'Hi'
s2 = 'Bye'
print(s1 + ' ' + s2)  #Addition

s3 = 'data'
print(s3 * 5)  #Multiplication

#String Slicing and Indexing
s = 'Namaste World'
print(s[-5:])
print(s[4:7])

#Built-in String methods
#--> Objects have built-in methods, these are functions inside of object
#-->Format: object.method(parameters)  ...parameters are extra arguments we pass into method

s = 'Hello World'
print(s.upper())
print(s.lower())

#Print formatting
#--> we can add .format() to add formatted ojs to printed string statements

name ="Manasvi"
role = "Data Engineer"
age = 23
print("My name is %s, I am working as a %s and my age is %s years old." % (name, role, age))
print("My name is {}, I am working as a {} and my age is {} years old.".format(name, role, age))
print(f"My name is {name}, I am working as a {role}")

my_string = 'hello'
name = 'Sam'
print(f"{my_string}, my name is {name} ")

#Numbers
#--> Integers: 1,2,-5, 1000; Floating-point numbers: 1.2,-0.5, 2e2, 3E2

#Basic Arithmetic
print(2+1)
print(2-1)
print(21/7)
print(2**3)
print(2 + 10 * 10 + 3)  #order of operations is followed
print((2+10) * (10+3))

#Variable Assignments
#--> Names can not start with a number.
#--> There can be no spaces in the name, use _ instead.
#--> Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
a = 3    #Let's create an object called "a" and assign it the number 3
b = 4
mean = (a+b)/2
print(mean)
