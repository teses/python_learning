"""
Lambda Test 1
"""
plusZehn = lambda a: a + 10
print(plusZehn(2))
print(plusZehn(5))

"""
Lambda Test 2
"""
add = lambda a, b, c: a + b + c
print(add(1, 2, 3))
print(add(5, 1, 4))

"""
Lambda Test 3
"""
def myFunc(x):
    return lambda a: a * x

#def myFunc(x):
#    def calc(a):
#        return a * x
#    return calc


mydoubler = myFunc(2)
print(mydoubler(11))
print(mydoubler(5))

mytripler = myFunc(3)
print(mytripler(11))
print(mytripler(5))


