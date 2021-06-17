# Control loop: While, For
# Branching: If...Else


# If..elif..else
def myCompare(num1, num2):
    if num1 > num2:
        print("num1 < num2")
    elif num1 == num2:
        print("num1 == num2")
    else:
        print("num1 > num2")


# Test
myCompare(1, 2)
myCompare(3, 3)
myCompare(5, 2)

# and, or

MALE_GENDER = 'male'
FEMALE_GENDER = 'female'
VIP = ("Joel", "Elie")


def sayHello(name, gender, age):
    if name == VIP[0] or name == VIP[1]:
        print(f"Hello {name}")
        print("You are awesome!")
    elif gender == MALE_GENDER and age > 20:
        print(f"Hello Mr.{name}!")
        print('You are handsome!')
    elif gender == FEMALE_GENDER and age > 20:
        print(f"Hello Mrs.{name}!")
        print('You are beautiful!')
    else:
        print(f"Hello {name}")
        print("Your are cute.")


sayHello("Joel", "male", 10)
sayHello("Elie", "female", 30)
sayHello("Huy", "male", 30)
sayHello("Lan", "female", 30)
sayHello("Huong", "female", 10)


# While
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is bigger than 6")

# For
fruits = ['apple', 'banana', 'lemon']
for x in fruits:
    print(x)

for y in range(0, 10, 3):
    print(y)
