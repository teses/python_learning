#
# Argumente mit Namen
#

def addressOutput(zip, street, city):
    """

    :param zip:
    :param street:
    :param city:
    :return:
    """
    print(street)
    print(zip + " " + city)


addressOutput(street="Musterstr. 1", zip="12345", city="Entenhausen")
addressOutput("12345", "Musterstr. 1", "Entenhausen")
