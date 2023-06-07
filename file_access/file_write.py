#
# Datei schreiben
#

filehandler = open("c:\\logs\\testwrite.txt", "a")

lb = "\n"

# einzelne Zeilen schreiben
filehandler.write("Dies ist eine Zeile in der Datei" + lb)
filehandler.write("fbfdbfdbfsdbf" + lb)
filehandler.write("Hallo" + lb)
filehandler.write("Welt" + lb)
string = """mehrere Zeilen
in eine Datei
bla
blub
"""
filehandler.write(string)

# mehrere Zeilen gleichzeitig schreiben
meineListe = ["Apfel", "Banane", "Kiwi"]
filehandler.writelines(meineListe)

# besser so
for x in meineListe:
    filehandler.write(x + "\n")

filehandler.close()



