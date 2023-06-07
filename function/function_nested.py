

def funktion1():
    print("Hallo ich bin Funktion 1")
    varinfunc1 = "Hallo"

    def funktion2():
        varinfunc2 = "Welt"
        print("Hallo ich bin Funktion 2")
        print(varinfunc1)


    print("Hallo ich bin auch in der Funktion 1")
    #print(varinfunc2) GEHT NICHT
    funktion2()


funktion1()