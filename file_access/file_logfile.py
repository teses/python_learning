#
#
#
# Import der Module
import datetime
import time

# Konfiguration
logdatei = "c:\\logs\\erster_log.txt"

# Funktionen
def writelog(file, msg):
    """
    Funktion zum loggen
    :param file: Pfad und Dateiname
    :type file: str
    :param msg: String der geloggt wird
    :type msg: str
    :return: keine Rückgabe
    """
    now = datetime.datetime.now()
    nowFormated = now.strftime("%Y-%m-%d %H:%M:%S")
    fh = open(file, "a")
    fh.write("[" + nowFormated + "] " + msg + "\n")
    fh.close()


writelog(logdatei, "Die ist mein erster log.")
time.sleep(2)
writelog(logdatei, "Dateien erfolgreich kopiert")
time.sleep(3)
writelog(logdatei, "Backup fertig")
time.sleep(1)
writelog(logdatei, "jetzt ist aber schluss")





