
# #Without Inheritance

# class Flyable:
#     def fly(self):
#         return f"{self.name} can fly!"

# class Quackable:
#     def quack(self):
#         return f"{self.name} can quack!"

# # Creating a duck instance manually combining behaviors
# class Duck:
#     def __init__(self, name):
#         self.name = name
#         self.flyable = Flyable()
#         self.quackable = Quackable()
#         self.flyable.name = self.name
#         self.quackable.name = self.name

#     def fly(self):
#         return self.flyable.fly()

#     def quack(self):
#         return self.quackable.quack()

# # Create instance of Duck
# duck = Duck("Daffy")

# # Call methods
# print(duck.fly())   # Output: Daffy can fly!
# print(duck.quack()) # Output: Daffy can quack!






class Animal:
    def __init__(self, name):
        self.name = name

class Flyable:
    def fly(self):
        return f"{self.name} can fly!"

class Quackable:
    def quack(self):
        return f"{self.name} can quack!"

class Duck(Animal, Flyable, Quackable):
    pass

# Create instance of Duck
duck = Duck("Daffy")

# Call methods
print(duck.fly())   # Output: Daffy can fly!
print(duck.quack()) # Output: Daffy can quack!

