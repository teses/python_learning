#
#   list
#
meineListe = ["Apfel", "Banane", "Zitrone", "Birne", "Kiwi"]
print(meineListe)
print(len(meineListe))
print(type(meineListe))

# Zugriff auf Listenelemente
print(meineListe[1])
print(meineListe[0])

# Zugriff auf Listenelemente mit negativen index
print(meineListe[-2])

# Zugriff mit Range
print(meineListe[3:5])
print(meineListe[:5])
print(meineListe[3:])

print("-------------------------")
start = 3
ende = 5
print(meineListe[start:ende])

# berechneter Index
test = 3
print(meineListe[test-1])

# ein Wert anhängen
meineListe.append("Melone")
print(meineListe)

# einfügen
meineListe.insert(1, "Kirsche")
meineListe.insert(1, "Playstation")
meineListe.insert(1, "Bla")
print(meineListe)

# löschen anhand des Wertes
meineListe.remove("Playstation")
print(meineListe)

# löschen anhand des Index
meineListe.pop(1)
meineListe.pop() # den letzten löschen
print(meineListe)

# zwei listen zusammenfügen
meineListe2 = ["VW", "Audi", "BMW"]
meineListe.extend(meineListe2)
print(meineListe)

