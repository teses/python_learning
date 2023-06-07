"""
 else
    Der else Block wird ausgeführt, wenn kein Fehler geworfen wurde
"""


#zahl = 2

try:
    erg = 4 * zahl
except Exception as err:
    print("Es ist ein Fehler aufgetreten: ", err)
else:
    print("Dies wird ausgegeben wenn kein Fehler passiert.")


