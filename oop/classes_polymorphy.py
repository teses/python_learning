"""
In Python gibt es keine Interfaces oder abstrakte Klassen/Methoden
Die Polymorphen Methoden werden spezifiziert.
Es gibt kein Mechanismuss der uns dazu zwingt
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Simulierung einer abstrakten Methode um Polymorphie zu erzwingen
    def move(self):
        raise Exception("move() muss in der Unterklasse existieren")

class Car(Vehicle):

    def move(self):
        print("brum brum...")


class Boat(Vehicle):
    def move(self):
        print("tuuuuuut.....plitsch platsch")


class Train(Vehicle):
    def move(self):
        print("tuf tuf,... Ich bin eine lokomotive....")


auto = Car("VW", "Golf")
schiff = Boat("AIDA", "Mita")
zug = Train("DB", "ICE")

for o in [auto, schiff, zug]:
    print(o.model)
    o.move()


