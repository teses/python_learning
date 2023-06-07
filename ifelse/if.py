#
# if-Bedingung
#
a = 5
b = 10

if a < b:
    print("a ist kleiner b")

#
alter = 18
if alter >= 18:
    print("tanzen.....")

# logische operatoren
a = False
b = True
if a and b:
    print("UND Es geht......")

if a or b:
    print("ODER es geht...")

if not(a or b):
    print("NICHT ODER es geht...")


a = True
b = True
c = True
d = False
if not(not a or not b) or c and d:
    print("wat geht.....")

#
a = 10
b = 9
c = 8

if a > b:
    if b < c:
        print("Gaga")
        print("Gugu")

if a > b and b < c:
    print("Gaga")
    print("Gugu")

#
meineListe = ["Apfel", "Banane", "Kiwi"]
if "Banane" in meineListe:
    print("Banane ist in der Liste")

#
suchwort = "Apfel"
if suchwort in meineListe:
    print(suchwort + " ist in der Liste")


# suchen in dict
person = {
    "firstName": "Susi",
    "lastName": "Sauer",
}
if "Susi" in person.values():
    print("Susi gefunden")

# is
meineListe = ["Hallo", "Welt"]
meineListe2 = meineListe
if meineListe is meineListe2:
    print("sind gleich")




