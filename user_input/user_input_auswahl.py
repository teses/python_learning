#
#
#
import random

def getUserInput():
    print("#" * 50)
    print("#")
    print("# Menü")
    print("#")
    print("# Bitte wählen Sie aus")
    print("# (N) Neues Spiel starten")
    print("# (Q) Beenden")
    print("#")
    print("#" * 50)
    eingabe = input("Bitte eine Auswahl angeben: ")
    return eingabe

def neuesSpiel():
    print("Neues Spiel wird gestartet")



#
# Hauptprogramm
#
meineEingabe = getUserInput()
#print(meineEingabe)
while True:
    if meineEingabe == "N" or meineEingabe == "n":
        neuesSpiel()
        break
    elif meineEingabe == "Q" or meineEingabe == "q":
        print("Programm beendet....")
        break
    else:
        print("Falsche Eingabe")
        meineEingabe = input("Bitte erneut eine Auswahl angeben: ")



