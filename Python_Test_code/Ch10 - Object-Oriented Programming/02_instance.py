class Students:
    language = "python"     # This is a class attribute
    salary = 5000000


shivam = Students()
shivam.name = "Shivam"   # This is an instance attribute
print(shivam.name, shivam.language, shivam.salary)

Aman = Students()
Aman.name = "Aman"   # This is an instance attribute
print(Aman.name, Aman.language, Aman.salary)

sahil = Students()
sahil.language = "javascripts"
sahil.name = "Cina"   # This is an instance attribute
print(sahil.name, sahil.language, sahil.salary)