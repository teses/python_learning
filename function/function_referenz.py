
def addiere(a, b):
    return a + b


add = addiere
print(add(5, 3))

del addiere
print(add(6, 2))


