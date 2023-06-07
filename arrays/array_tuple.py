#
# tuple
#
# Ein tuple mit einen Eintrag geht mit dieser Syntax so NICHT
miniListe = ("Apfel")
print(miniListe)

# Wenn man ein tuple mit einem Eintrag haben möchte muss
# mann folgende Syntax nehmen
miniListe = ("Apfel",)
print(miniListe)

# ein tuple
meineListe = ("Apfel", "Banane", "Zitrone", "Birne", "Kiwi")
print(meineListe)
print(len(meineListe))
print(type(meineListe))

# Zugriff auf Elemente
print(meineListe[1])
print(meineListe[0])

# Zugriff auf Elemente mit negativen index
print(meineListe[-2])

# Zugriff mit Range
print(meineListe[3:5])
print(meineListe[:5])
print(meineListe[3:])
print(meineListe[-4:-2])
print("-" * 50)
start = 3
ende = 5
print(meineListe[start:ende])

# berechneter Index
test = 3
print(meineListe[test-1])

# ein Wert anhängen Trick 1
tmp = list(meineListe)
tmp.append("Melone")
meineListe = tuple(tmp)
print(meineListe)
# ein Wert anhängen Trick 2
newListe = ("Aprikose",)
meineListe = meineListe + newListe
print(meineListe)

print("-" * 50)
print(meineListe * 3)

# zusammenfügen
meineListe2 = ("VW", "Audi", "BMW")
print(meineListe + meineListe2)