
import math

def berechne(func, wert):
    print("Es wird die Funktion " + func.__name__ + " aufgerufen")
    print(func(wert))


#print(math.sin(2))

berechne(math.sin, 2)
berechne(math.cos, 2)


