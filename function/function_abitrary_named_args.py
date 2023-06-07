

def addressOutput(**address):
    print(address['street'])
    print(address['zip'] + " " + address['city'])


addressOutput(street="Musterstrasse", zip="12345", city="Entenhausen")
addressOutput(street="Musterstrasse", zip="12345")

