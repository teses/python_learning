"""
Alle Fehler abfangen
"""


# erg = 10 * (1/0) # ZeroDivisionError
# erg = 4 * zahl # NameError
# erg = '2' + 2 # TypeError

# Alle Fehler abfangen
try:
    erg = 10 * (1 / 0)
except:
    print("Fehler")


# nur bestimmte Fehler abfangen
try:
    erg = 4 * zahl
except NameError:
    print("Fehler")

# mehrere Fehler unterschiedlich abfangen
try:
    #zahl = 0
    erg = 4 / zahl
except NameError:
    print("NameError: Fehler")
except ZeroDivisionError:
    print("ZeroDivisionError: Fehler")

# mehrere Fehler gleich abfangen
try:
    #zahl = 0
    erg = 4 / zahl
except (NameError, ZeroDivisionError):
    print("NameError oder ZeroDivisionError: Fehler")
