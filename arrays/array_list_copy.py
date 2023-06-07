#
#
#

# copy von variablen
meinText1 = "Hallo"
meinText2 = meinText1
meinText2 = "Welt"
print(meinText1)
print(meinText2)

# dies ist KEINE Copy des Arrays sondern eine Referenz
meineListe1 = ["Apfel", "Banane", "Zitrone", "Birne", "Kiwi"]
meineListe2 = meineListe1
meineListe2.append("Melone")
print(meineListe1)
print(meineListe2)

# Copy mit .copy()
meineListe1 = ["Apfel", "Banane", "Zitrone", "Birne", "Kiwi"]
meineListe2 = meineListe1.copy()
meineListe2.append("Melone")
print(meineListe1)
print(meineListe2)


