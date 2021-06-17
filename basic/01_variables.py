# This is a comment

'''
This is a paragraph.
Because I want to comment a lot of content.
'''

name = "Vcttai"
print(f"Hello world! My name is {name}.")

appleColor, lemonColor = "red", "yellow"
print(f"Apple is {appleColor} and Lemon is {lemonColor}.")

paragraph = '''This is a paragraph,
because it is too long so that I break
it into lines'''
print(paragraph)


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

brand = "Toyota"
car = "Hilux"
buyStr = "I get a {carName}, from {brandName} company"
print(buyStr.format(carName=car, brandName=brand))
