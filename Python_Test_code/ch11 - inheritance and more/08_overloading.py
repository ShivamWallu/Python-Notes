class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(5)
num2 = Number(10)
print(num1 + num2)  # Output: 15




# -----------------------------------------------------------------------




class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Employee name: {self.name}"

    def __len__(self):
        return len(self.name)

shivam = Employee("Shivam")
print(str(shivam))  # Output: Employee name: Shivam
print(len(shivam))  # Output: 6
