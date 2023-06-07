#
#   Datei Zugriff
#
#   r - Read    Datei lesen. Error wenn sie nicht existiert
#   a - Append  Öffnet eine Datei um am Ende anzufügen.
#               Wenn Datei nicht existiert wird sie angelegt
#   w - Write   Öffnet eine Datei um vom Anfang zu schreiben.
#               Wenn Datei nicht existiert wird sie angelegt
#   x - Create  Erzeugt eine Neue Datei. Error wenn die Datei schon existiert
#
#   Dateiart
#
#   t - Textformat
#   b - Binärformat
#

filehandler = open("c:\\logs\\testdatei.txt", "r")

# komplette Datei einlesen
print(filehandler.read())

# Teile einlesen Datei einlesen
filehandler.seek(0) # Zeiger wieder zum Anfang setzen
print(filehandler.read(8))

# Zeilenweise einlesen
print("-" * 50)
filehandler.seek(0)
print(filehandler.readline())
print(filehandler.readline())
print(filehandler.readline())

# zeilenweise mit einer for schleife
print("-" * 50)
filehandler.seek(0)
for line in filehandler:
    print(line)

# Alle Zeilen in ein Array einlesen
filehandler.seek(0)
lines = filehandler.readlines()
for line in lines:
    print(line)






filehandler.close()

