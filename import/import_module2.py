
# module importieren
# modul in unterordner modules
from modules import mymodule
# modul in unterordner modules/test
from modules.test import testmodule

# zugriff auf die Funktionen innerhalb der module
mymodule.sayHello("Thomas")
testmodule.sayHello("Thomas")

# Zugriff auf eine Dictonary innerhalb eines modules
print(mymodule.person1["name"])

## alle funktionen eines modules
print(dir(mymodule))

