

def FunktionA():
    print("Hallo ich bin in der FunktionA()")

def MeinFunktion():
    print("Hallo ich bin in der MeinFunktion()")

def FunktionB(func):
    print("Hallo ich bin in der FunktionB()")
    func()
    print("Die Aufgerufene Funktion func() heißt " + func.__name__)


FunktionB(FunktionA)
FunktionB(MeinFunktion)
