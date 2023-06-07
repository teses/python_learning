x = 5
y = "John"
print(x)
print(y)

print("-------------------------------")

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 
print(x)
print(y)
print(z)
print(type(x))
print(type(y)) 
print(type(z)) 

print("---- Many Values to Multiple Variables ------------------------")

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("------ unpacking -----------------------")

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)