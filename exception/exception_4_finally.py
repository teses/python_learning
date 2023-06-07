"""
 finally
    Der finally Block wird auf jeden Fall ausgeführt
    Man könnte es auch als Clean-Up verwenden

"""


zahl = 2

try:
    erg = 4 * zahl
except Exception as err:
    print("Es ist ein Fehler aufgetreten: ", err)
finally:
    print("Das hier steht in finally")


# Beispiel mit Datei
#file = "../testfiles/notexistfile.txt"
file = "../testfiles/existfile.txt"
try:
    f = open(file, "r")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Beim schreiben in der Datei '" + file + "' ist ein Fehler aufgetreten")
    finally:
        f.close()
except:
    print("Beim öffnen der Datei '" + file + "' ist ein fehler aufgetreten")
