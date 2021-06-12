print("Try some data types in python!")

str = "Hello world! This is a string"
print(str)

num = 10.5
print(num)

print("\nList is a collection which is ordered and changeable. Allows duplicate members.")
myList = ['apple', 'lemon', 'banana']
print(myList)
print(myList[1])
myList[1] = "lemon_changed"
print(myList[1])

print("\nTuple is a collection which is ordered and unchangeable. Allows duplicate members.")
myTuple = ('apple', 'lemon', 'banana')
print(myTuple)
print(myTuple[2])
# myTuple[1] = "lemon_changed"   # You cann't reassign values for Tuple

print("\nRange: ")
myRange = range(1, 20, 4)
print(myRange)
for x in myRange:
    print(x)

print("\nDictionary is a collection which is unordered, changeable and indexed. No duplicate members.")
myDict = {'apple': 20, 'lemon': 15, 'banana': 17}
print(myDict)
print(myDict['lemon'])

print("\nSet is a collection which is unordered and unindexed. No duplicate members")
mySet = {'apple', 'lemon', 'banana'}
print(mySet)
for x in mySet:
    print(x)

myFrozenset = frozenset({'apple', 'lemon', 'banana'})
print(myFrozenset)
