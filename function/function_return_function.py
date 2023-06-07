


def FunktionA(x):

    def FunktionB(y):
        return x + y

    return FunktionB


ergebnis1 = FunktionA(5)
print(ergebnis1(3))
print(ergebnis1(2))

ergebnis2 = FunktionA(10)
print(ergebnis2(3))

