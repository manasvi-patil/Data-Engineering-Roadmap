#Data Types and Data structures
#--> Everything in Python is an "object", including integers/floats
#--> Most common and important types (classes)
#--> * "Single value": None, int, float, bool, str, complex
#--> * "Multiple values": list, tuple, set, dict

a = 42
b = 32.30
c = "Hello"
d = True
print(type(a))  #gets type of a
print(type(b))  #gets type of b
print(type(c))
print(type(d))

#1 Lists
my_list = [1, 2.3, "a", "Day 2"]
print(my_list)
print(len(my_list))

#Adding new element to a list
my_list.append("hello")  #append method takes only one argument
my_list.extend([5, 9.8, "b"]) 
my_list.insert(2, "d")  #adds only single element
print(my_list)

#Slicing
#--> used to access individual or rage of elements in a list
#--> list_object[start:end:step] or list_object[start:end]  ...here "step" is basically times or how many places to skip and consider that element
my_list = list(range(10))
print("Printing range of numbers from 0 till 9: ", my_list)
print("Printing alternate elements starting from 0: ", my_list[0::2]) #will print num starrting from 0 and till the end with a alternative of 2
print("Printing Printing every third element starting from 1: ", my_list[1::3])
print("Printing range of numbers from 4 to 7: ", my_list[4:7])

print(my_list[-1])
print(my_list[9:10])

#2 Dictionaries
#--> hash tables consisting of a key and value and value can be any python object

#Construct a dictionary
my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)
my_dict['key1'] = 123  #changing key value
print(my_dict['key1'])
#Python has a built-in method of doing a self subtraction or addition (or multiplication or division).
my_dict['key1'] = my_dict['key1'] - 123  #deleting value
print(my_dict)

new_dict = {"name": ['Manasvi', 'Hudah', 'Menaja'], "surname": ["Patil", 'Ansari', 'Bhide'], "age": [23, 23, 23]}
print(new_dict)
new_dict["country"] = ['Japan', 'Eygpt', "Germany"]
print(new_dict)

new_dict["name"] += ["Shweta"]  #adding additioanl value to name key
print(new_dict)


#3 Set and Booleans

#Sets
#--> Sets are unordered collection of UNIQUE elements
len = [1,1,1,2,2,3,4,5,6,6]
len_sets = set(len)
print(len_sets)  #eliminates duplicates

x = set()  #defining as set
x.add(1)
print(x)

#Tuples
#--> Tuple is ordered and UNCHANGEABLE and allow duplicate values
mytuple = ("Mango", "Banana", "Strawberry")
print(type(mytuple))

#---------------------------------------------------------

#               List   Tuple   Set    Dictionary
#Ordered        Yes     Yes    No       No
#Mutuable       Yes     No     Yes      Yes
#Constructor    [ ]    ( )     { }      { }
#Example