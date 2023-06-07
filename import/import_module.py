
# variante 1
from mymodules import meinefunktionen
from mymodules.unterordner import anderefunktionen
from mymodules.unterordner.nocheinordner import einmodul

# mit aliases
from mymodules.unterordner.nocheinordner import einmodul as ein

# Funktionen/Variable aus ein Modul importieren
from mymodules.meinefunktionen import machDiesDas
from mymodules.meinefunktionen import person

# Aufrufe
meinefunktionen.machDiesDas()
print(meinefunktionen.person)
anderefunktionen.machDiesDasAndere()
einmodul.machDiesDasModul()
ein.machDiesDasModul()

machDiesDas()
print(person["firstname"])






