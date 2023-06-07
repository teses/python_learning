"""
Alle Fehler abfangen
"""


# erg = 10 * (1/0) # ZeroDivisionError
# erg = 4 * zahl # NameError
# erg = '2' + 2 # TypeError

try:
    erg = 4 * zahl
except Exception as err:
    print(type(err)) # Exception type
    print(err.args) # argumente des Fehlers
    print(err) # erlaubt es die Argumente direkt zu printen



