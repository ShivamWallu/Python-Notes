# # Without Inheritance
# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} says Woof!"

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} says Meow!"

# # Create instances of Dog and Cat
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# # Call speak method
# print(dog.speak())  # Output: Buddy says Woof!
# print(cat.speak())  # Output: Whiskers says Meow!








# With Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("hlo")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


# Create instances of Dog 
dog = Dog("Buddy")


# Call speak method
print(dog.speak())  # Output: Buddy says Woof!


