#
# set
#
meinSet = {"Apfel", "Zitrone", "Banane"}
print(meinSet)

# doppelte werden aussortiert
meinSet2 = {"Apfel", "Zitrone", "Banane", "Zitrone", 1, True, 2}
print(meinSet2)

# hinzufügen
meinSet.add("Melone")
print(meinSet)

# mehrere mit update()
meinSet3 = {"Ananas", "Kiwi"}
meinSet.update(meinSet3)
print(meinSet)

meinSet4 = ["Pfirsich", "Kirsche", "Kirsche"]
meinSet.update(meinSet4)
print(meinSet)

# entfernen mit remove(). Bei nicht existens gibt es ein Fehler
meinSet.remove("Pfirsich")
print(meinSet)

# entfernen mit discard(). Bei nicht existens gibt es ein KEIN Fehler
meinSet.discard("gibtesnicht")
print(meinSet)

# entfernen mit pop()
x = meinSet.pop()
print(meinSet)
print(x)

# Vereinigung mit union(); duplikate werden entfernt
print("-" * 50)
meinSet = {"Apfel", "Zitrone", "Banane", "Kiwi"}
meinSet3 = {"Ananas", "Kiwi"}
neuesSet = meinSet.union(meinSet3)
print(neuesSet)

# Schnittmenge bilden mit intersection()
meinSet = {"Apfel", "Zitrone", "Banane", "Kiwi"}
meinSet3 = {"Apfel", "Ananas", "Kiwi"}
neuesSet = meinSet.intersection(meinSet3)
print(neuesSet)

# Elemente die NICHT in beiden sind
meinSet = {"Apfel", "Zitrone", "Banane", "Kiwi"}
meinSet3 = {"Apfel", "Ananas", "Kiwi"}
neuesSet = meinSet.symmetric_difference(meinSet3)
print(neuesSet)

# Elemente die in A sind aber NICHT in B
meinSetA = {"Apfel", "Zitrone", "Banane", "Kiwi"}
meinSetB = {"Apfel", "Ananas", "Kiwi"}
neuesSet = meinSetA.difference(meinSetB)
print(neuesSet)

# Elemente die in B sind aber NICHT in A
meinSetA = {"Apfel", "Zitrone", "Banane", "Kiwi"}
meinSetB = {"Apfel", "Ananas", "Kiwi"}
neuesSet = meinSetB.difference(meinSetA)
print(neuesSet)
