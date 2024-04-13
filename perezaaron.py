t = int(input())

cases = []
for i in range(t):
    string = input()
    c, r = string.split()
    cases.append((int(c), int(r)))

"""
Dominio: n1, n2 y r, números naturales, donde n1 y n2 son los números a comprobar y r es el límite de comcurrencias de los dígitos
Ambito: True, False
"""

def contar_digitos(numero, contador):
        while numero > 0:
            digito = numero % 10
            contador[digito] += 1
            if contador[digito] > r:
                return False
            numero //= 10
        return True


def todo(n1, n2, r):
    if n1 >= 1000 and n1 < 10000:
        n1 *= 10
    if n2 >= 1000 and n2 < 10000:
        n2 *= 10

    list = str(n1) + str(n2)
    for i in list:
        if list.count(i) > r:
            return False

    return True


"""
Dominio: c, r ambos números naturales, donde c es el número a encontrar y r es el limite de de concurrencias de los digitos
Ambito: Devuelve una cadena de texto, ejemplo: 13485/2697=5\n13845/2769=5
"""


def foo(c: int, r: int) -> None:
    string = ""
    a = 1000

    while a * c < 100000:
        b = a * c
        if todo(b, a, r):
            string += f"{b}/{a}={c}\n"

        a += 1

    return string


tests = []
for i in cases:
    tests.append(foo(i[0], i[1]))

for i in tests:
    print(i)
