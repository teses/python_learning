#
# while schleife
#

# eine simple schleife
i = 0
while i < 6:
    print(i)
    i += 1


# Das break Schlüsselwort
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

# continue Schlüsselwort
print("-"*50)
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# else in der while schleife
print("-" * 50)
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("i ist nicht mehr kleiner als 10")

#
print("-" * 50)
obst = ["Apfel", "Banane", "Kiwi"]
anzahl = len(obst)
i = 0
while i < anzahl:
    print(obst[i])
    i += 1
