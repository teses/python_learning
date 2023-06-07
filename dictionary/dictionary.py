#
#   Dictionary
#
person = {
    "firstName": "Susi",
    "lastName": "Sauer",
    "gender": "w",
    "height": 163,
    "weight": 60.6,
    "hobbies": ["singen", "tanzen"]
}
print(person)

# zugriff - variante 1
print(person["firstName"])
print(person["weight"])
print(person["hobbies"][1])
print(person["firstName"] + " " + person["lastName"])

# zugriff - variante 2
print(person.get("firstName") + " " + person.get("lastName"))

# neuen member hinzufügen
person["hair"] = "blond"
print(person)
print(person["hair"])

# member ändern
person["lastName"] = "Müller"
print(person)

# member löschen
person.pop("hair")
print(person)

# members hinzufügen
address = {
    "street": "Musterstr. 1",
    "zip": "1234",
    "city": "Entenhausen"
}
person.update(address)
print(person)
print(person["city"])
print(address)

 
