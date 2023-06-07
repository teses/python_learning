

class TestKlasse:
    publicAttribut = 20
    _protectedAtribut = 5
    __privatesAttribut = 10

    def publicMethod(self):
        print("Ich bin public in der Klasse " + type(self).__name__)

    def _protectedMethod(self):
        print("Ich bin protected in der Klasse " + type(self).__name__ + ". Mich bitte nicht von aussen benutzen.")

    def __privateMethod(self):
        print("Ich bin eine private Methode in der Klasse " + type(self).__name__)

# Aufruf der TestKlasse
test = TestKlasse()
print(test.publicAttribut)
print(test._protectedAtribut)
#print(test.__privatesAttribut)  # GEHT NICHT !!
print(test._TestKlasse__privatesAttribut) # Geht sollte man aber vermeiden

test.publicMethod()
test._protectedMethod()
#test.__privateMethod() # GEHT NICHT !!
test._TestKlasse__privateMethod() # Geht sollte man aber vermeiden
