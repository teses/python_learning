#
# for
#
autos = ["VW", "Audi", "Porsche"]
for auto in autos:
    print(auto)


#
print("-" * 50)
zahlen = range(2, 10, 2)
for zahl in zahlen:
    print(zahl)

print("-" * 50)
for zahl in range(3, 31, 3):
    print(zahl)

# else
print("-" * 50)
for zahl in range(3, 31, 3):
    print(zahl)
else:
    print("3er Reihe fertig....")

# Alle Buchstaben von A-Z
for x in range(65, 91):
    print(chr(x))

# verchachtelte schleife
print("-" * 50)
farben = ["blauer", "gelber", "grüner"]
obst = ["Apfel", "Pfirsich", "Kirsche"]
for farbe in farben:
    for frucht in obst:
        print(farbe + " " + frucht)

# dictionary durchlaufen
person = {
    "firstName": "Susi",
    "lastName": "Sauer",
    "gender": "w",
    "height": 163,
    "weight": 60.6
}
print("-" * 50)
for key in person:
    print(key + " = " + str(person[key]))

print("-" * 50)
for key, value in person.items():
    print(key + " = " + str(value))



