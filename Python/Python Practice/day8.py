#OOPS
#Polymorphism
#--> Same function name but different behaviour
#--> Same button → different actions
#--> Same method → different output
#--> Polymorphism means one function name having multiple behaviors depending on the object.

class Vehicle:
    def speed(self):
        return 40
class Car:
    def speed(self):
        return 80   
class Bike:
    def speed(self):
        return 60
    
Vehicle = [Vehicle(), Car(), Bike()]
for v in Vehicle:
    print(v.speed())

#2
class DataSource:
    def read_data(self):
        print("Reading data from generic source")


class CSVSource(DataSource):
    def read_data(self):
        print("Reading data from CSV file")


class JSONSource(DataSource):
    def read_data(self):
        print("Reading data from JSON file")


class DatabaseSource(DataSource):
    def read_data(self):
        print("Reading data from Database")

sources = [CSVSource(), JSONSource(), DatabaseSource(), DataSource()]

for src in sources:
    src.read_data()

#Method Overiding and Polymorphism
#--> Polymorphism is a concept where the same method behaves differently for different objects. Method overriding is one of the ways to achieve polymorphism in object-oriented programming.

#Mini Task Override method
class Employee:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        print("Employee")
    
class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        super().get_role()   # call parent method
        print("Manager")      # child behavio

emp = [Manager("Chris"), Employee("Emp1")]
for e in emp:
    e.get_role()

#Abstraction
#--> Show only important details, hide implementation
#Think of abstract class like a blueprint 🏗️
# - Blueprint of a house ≠ actual house
# - You can’t live in a blueprint
# - You build a house from blueprint
#we cannot create an object of an Abstract Class
#Abstract class will only defines rules, not implementation

from abc import ABC, abstractmethod

class Employee(ABC):
    
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus
    
class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours):
        self.hourly_rate = hourly_rate
        self.hours = hours
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours

f = FullTimeEmployee(40000, 1000)
p = PartTimeEmployee(30, 100)
print(f.calculate_salary())
print(p.calculate_salary())
