#
#
#
def addressCard(person):
    print(person["firstName"] + " " + person["lastName"])
    print(str(person["weight"]) + " kg")
    print(str(person["height"]) + " cm")


person = {
    "firstName": "Susi",
    "lastName": "Sauer",
    "height": 163,
    "weight": 60.6
}

addressCard(person)

