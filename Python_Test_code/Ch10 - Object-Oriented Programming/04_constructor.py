class Person:
    def __init__(self, name, bookprice):
        self.name = name
        self.bookprice = bookprice

    def display(self):
        print(f"Name: {self.name}, Book Price: {self.bookprice}")

# Creating an object of the Person class
person1 = Person("Shivam", 550)
person1.display()






# -------------------------------------------------------------------------------------



class Book:
    def __init__(self, title, author, pages=0):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

# Creating an object of the Book class
book1 = Book("Python Programming", "Shivam")
book1.display()

book2 = Book("Advanced Python", "Shivam", 350)
book2.display()
