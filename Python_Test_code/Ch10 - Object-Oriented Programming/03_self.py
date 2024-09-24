class Students:
    language = "python"     # This is a class attribute
    salary = 5000000
    name = "Shivam"

    def getInfo(self):                       # Methods
        print("how much your salary")

    def cool(self):                       # Methods
        print(f"{self.name}, salary is very high {self.salary}")

    @staticmethod  # static method 
    def bad():                       # Methods
        print("how much your salary")    
        


shivam = Students()
shivam.salary = 200000           # instance attribute
print(shivam.name, shivam.language, shivam.salary)

shivam.getInfo()
shivam.cool()
shivam.bad()