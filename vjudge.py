from math import factorial

def lcm(a, b):
    list_a = []
    list_b = []

    for i in range(1, a + 1):
        list_a.append(a * i)
    for i in range(1, b + 1):
        list_b.append(b * i)

    print(list_a, list_b)

lcm(4, 6)

def c3(a,b):
    fact = factorial(a)

    for i in range(1, fact + 1):
        print(i)

    return fact

print(c3(10,2))