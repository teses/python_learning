"""
Ein Fehler ausgeben wenn gewünscht
"""

x = -1
x = 2
if(x < 0):
    raise Exception("x ist kleiner als 0")

# man kann auch ein eigenen Fehler typen ausgeben
z = "Hallo"
if not type(z) is int:
    raise TypeError("z ist keine Zahl")

