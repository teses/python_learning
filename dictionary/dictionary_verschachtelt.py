#
#
#
autos = [
    {
        "marke": "VW",
        "model": "Golf 3 GTI",
        "power": 360,
        "color": "black"
    },
    {
        "marke": "Audi",
        "model": "A3",
        "power": 120,
        "color": "red"
    }
]
print(autos[1]["marke"])

# variante
auto1 = {
    "marke": "VW",
    "model": "Golf 3 GTI",
    "power": 360,
    "color": "black"
}
auto2 = {
    "marke": "Audi",
    "model": "A3",
    "power": 120,
    "color": "red"
}
autos = [auto1, auto2]


###
bestellung = {
    "orderNo": "B123",
    "date": "2023-03-07",
    "customer": {
        "firstName": "Susi",
        "lastName": "Sauer"
    },
    "deliveryAddress": {
        "street": "Musterstr. 1",
        "zip": "12345",
        "city": "Entenhausen"
    },
    "positions": [
        {
            "title": "32 GB RAM",
            "quantity": "2",
            "price": 55.59
        },
        {
            "title": "Motherboard ASUS GX-2",
            "quantity": "1",
            "price": 326.99
        }
    ]
}
