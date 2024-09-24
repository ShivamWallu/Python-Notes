# class Students(): # Blue print of Class
#         def __init__(self, subject , timing):  #Constructure with parameters
#             self.subject = subject       
#             self.timing = timing


#         def fees(self):
#             print(f"heelo students today your tuition timing : {self.timing} and subject : {self.subject} ")
            

    
# a = Students("Maths", 6)     # Creating an Objects
# a.fees() #calling method



# --------------------------------------------------------------------------------------------



# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Derived Class
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  # Call the constructor of Person to initialize name and age
        self.employee_id = employee_id  # Initialize employee_id in the Employee class

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}")

# Creating an object of the derived class
emp = Employee("John Doe", 30, "E12345")
emp.display()
