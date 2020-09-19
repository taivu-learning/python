# Function's params
print("Function's params")


def sayHello(name):
    print(f"Hello {name}.")


sayHello("John Wick")
sayHello("Kaka")

# Function returns value
print("Function returns value")


def sum(num1, num2):
    result = num1 + num2
    return result


print(sum(1, 2))
print(sum(4, 5))

# Function's parameter as a Tuple
print("Function's parameter as a Tuple")


def myFunction(*param):
    if(len(param) == 2):
        print(param[0] + param[1])
        return

    print(param)


myFunction((2, 3))
myFunction(1, 2)
myFunction(1, "a", 3)
myFunction("Hello")

# Function's parameter as a dictionary
print("Function's parameter as a dictionary")


def myParamAsDict(**param):
    if(len(param) == 2):
        print(param['item1'] + param['item2'])
        return

    print(param)


# myParamAsDict({'item1': 1, 'item2': 2})    #error
myParamAsDict(item1=2, item2=3)
myParamAsDict(item1="Hello")
myParamAsDict(item1="Hello", item2="World", item3="Hihi")


def myParamAsDict2(param):
    if(len(param) == 2):
        print(param['item1'] + param['item2'])
        return

    print(param)


myParamAsDict2({'item1': 4, 'item2': 5})
