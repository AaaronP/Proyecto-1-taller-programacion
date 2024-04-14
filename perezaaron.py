t = int(input())

# O(t)
cases = []
for i in range(t):
    string = input()
    c, r = string.split()
    cases.append((int(c), int(r)))

"""
Dominio: n1, n2 y r, números naturales, donde n1 y n2 son los números a comprobar y r es el límite de comcurrencias de los dígitos
Ambito: True, False
"""


def todo(n1: int, n2: int, r: int) -> bool:
    if n1 >= 1000 and n1 < 10000:
        n1 *= 10
    if n2 >= 1000 and n2 < 10000:
        n2 *= 10

    # len(list) == 10
    list = str(n1) + str(n2)
    # O(list^2) o O(10^2)
    for i in list:
        if list.count(i) > r:
            return False
    return True


"""
Dominio: c, r ambos números naturales, donde c es el número a encontrar y r es el limite de concurrencias de los digitos
Ambito: Devuelve una cadena de texto, ejemplo: 13485/2697=5\n13845/2769=5
"""


def foo(c: int, r: int) -> str:
    string = ""
    a = 1000
    # en el peor de los casos haria 98999 bucles
    # y en el mejor haria solo 4000 bucles

    # 98999 * 100 = 9,899,900
    # O(9 899 900) en el peor de los casos
    while a * c < 100000:
        b = a * c

        # O(100) 100 bucles
        if todo(b, a, r):
            string += f"{b}/{a}={c}\n"

        a += 1

    return string


# O(t)
tests = []
for i in cases:
    tests.append(foo(i[0], i[1]))

# O(t)
for i in tests:
    if i == tests[-1]:
        print(i[:-1])
    else:
        print(i)
