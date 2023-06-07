

class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return self.firstname + " " + self.lastname


class Student(Person):

    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)
        self.graduationYear = 2019


student = Student(lastname="Max", firstname="Mustermann")
print(student)
