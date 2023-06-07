#
#   Willkürliche Argumente in einer Funktion
#

def kinder(*namen):
    for name in namen:
        print(name)


kinder("Susi", "Hans", "Laura", "Jasmin")
kinder("Tick", "Trick", "Track")
kinder("Max", "Moritz")
kinder("Donald")

