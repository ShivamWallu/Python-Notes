class Person:
    def __init__(self, name):
        self._name = name  # The actual attribute (with a leading underscore to indicate it's private)

    @property
    def name(self):
        # This method is accessed like an attribute (person.name)
        return self._name

    @name.setter
    def name(self, value):
        # This method is used to set the attribute (person.name = "New Name")
        if not value:
            raise ValueError("Name cannot be empty!")
        self._name = value

# Example usage
person = Person("Alice")
print(person.name)  # Calls the getter method

person.name = "Bob"  # Calls the setter method
print(person.name)
