#
#
#

def addressOutput(**address):
    print(address["street"])
    print(address["zip"] + " " + address["city"])

addressOutput(street="Musterstr. 1", zip="12345", city="Entenhausen")

