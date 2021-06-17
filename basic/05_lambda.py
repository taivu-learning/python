# lambda

def myMultiplier(n: int):
    return lambda a: a * n


doubler = myMultiplier(2)
tripler = myMultiplier(3)

print(doubler(3))
print(doubler(11))
print(tripler(3))
