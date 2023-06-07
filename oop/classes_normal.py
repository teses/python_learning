

class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return self.firstname + " " + self.lastname


p1 = Person("Max", "Mustermann")
print(p1.firstname + " " + p1.lastname)
print(p1)
