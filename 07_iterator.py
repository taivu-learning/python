# Iterator

myTuple = ("Apple", "Orange", "Mango")
itor = iter(myTuple)

print(itor)
print(next(itor))
print(next(itor))
print(next(itor))

for fruit in myTuple:
    print(fruit)
