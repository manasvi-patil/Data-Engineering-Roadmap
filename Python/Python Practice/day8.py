#OOPS
#--> OOPS = Putting related data + functions together.

#1
class Student:
    def __init__(self, name, marks):  #creating constructor
        self.name = name  #saving data in obj
        self.marks = marks

    def get_grade(self):  #method (function inside class)
        if self.marks >= 75:
            return "Distinction"
        elif self.marks >= 50:
            return "Pass"
        else:
            return "Fail"

stud = Student("Sam", 86)
print(stud.name)
print(stud.get_grade())

#2
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New Balance: {self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrawn {amount}. New Balance: {self.balance}"
    
    def show_balance(self):
        return f"Current Balance: {self.balance}"
    
customer = BankAccount("Hashie", 50000)
print(customer.name)
print(customer.deposit(450))
print(customer.withdraw(50000))
print(customer.show_balance())

#Inheritance
#--> Reuse code between classes
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary= salary
    
    def update_salary(self, amount):
        self.salary = self.salary + amount
        return f"Update salary is {self.salary}"
    
    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2
    
class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.3

class Intern(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05
    
dev = Developer("Chris", 40000)
mgr = Manager("Sim", 70000)
intern = Intern("John", 20000)
print(dev.get_details())
print("Developer bonus: ", dev.calculate_bonus())

print(mgr.get_details())
print("Manager bonus: ", mgr.calculate_bonus())

print(intern.get_details())
print("Intern Bonus:", intern.calculate_bonus())

print(dev.update_salary(1000))

#Encapsulation
#--> Hiding internal data + controlling access using methods
#| Type        | Meaning                      |
#| ----------- | ---------------------------- |
#| balance     | public (anyone can access)   |
#| _balance    | protected (convention only)  |
#|  __balance  | private (real encapsulation) |

#1
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def update_salary(self, amount):
        if self.__salary + amount < 0:
            return "Invalid Salary and update not allowed"
        self.__salary += amount
        return self.__salary
        
    def get_salary(self):
        return f"The updated salary is {self.__salary}"
    
emp = Employee("Simran", 40000)
emp2 = Employee("Noah", 30000)
print(emp.name)
print(emp2.name)
print(emp.update_salary(400))
print(emp2.update_salary(-40000))
print(emp.get_salary())
print(emp2.get_salary())

#super()
#--> Call parent class constructor.
#--> the super() function is used to call methods from a parent (superclass) inside a child (subclass)
#--> Without super(), parent variables won’t initialize.
class Person:  
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Emp(Person):  
    def __init__(self, name, id):
       #Incorrect code
       #  self.name_ = name   # Forgot to call Person’s __init__
        super().__init__(name, id) 

emp = Emp("James", 103)
print(emp.name, emp.id)

#2 INheritance + Encapsulation
#Why can't child class access __balance?
#Answer: Because Python performs name mangling on private variables, making them accessible only within the class where they are defined.
class Account:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    def set_balance(self, new_balance):
        self.__balance = new_balance
    
class SavingsAccount(Account):  #Inheritance
    # def __init__(self, balance):
    #     super().__init__(balance)  #call objects from parent Account

    def deposit(self, amount):
       new_balance = self.get_balance() + amount
       self.set_balance(new_balance)
       return f"Balance after deposit {self.get_balance()}"
    
    def withdraw(self, amount):
        new_balance = self.get_balance() - amount
        self.set_balance(new_balance)
        return f"Balance after withdrawal {self.get_balance()}"
    
cust = SavingsAccount(50000)
print(cust.deposit(5000))
print(cust.withdraw(500))

#Multiple Inheritance
#--> WHen a child class inherits from more than one parent class
#1
class Father:
    def skills(self):
        print("Father: driving")
class Mother:
    def skills(self):
        print("mother: teaching")

class Child(Father, Mother):
    pass

c = Child()
c.skills()  #here only Father's method is called

#MRO - Method Resolution Order
#--> Python checks classes from left to right
#--> So for child class order was Child -> Father -> Mother

#2
class A:
    def show(self):
        print("A class")

class B(A):
    def show(self):
        print("B class")
        super().show()
class C(A):
    def show(self):
        print("C class")
        super().show()

class D(B, C):
    def show(self):
        print("D class")
        super().show()

c = D()
c.show()  #Here order will be D-> B-> C-> A
#Because Python uses C3 Linearization for MRO
#D → B → C → A → object and nOT D → B → A → C → A ❌

#Mini Task Multiple Inheritance
class Writer:
    def work(self):
        print("Writing content")
class Editor:
    def work(self):
        print("editing content")

class Author(Writer, Editor):
    pass

auth = Author()
auth.work()


