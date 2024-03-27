from eulerlib import Divisors

import time

inicio = time.time()

# Referencias
"""
https://www.baeldung.com/cs/backtracking-algorithms#:~:text=Backtracking%20is%20an%20algorithmic%20technique,satisfy%20them%20will%20be%20removed.
https://www.w3schools.com/python/python_ref_list.asp
https://www.w3schools.com/python/ref_string_format.asp
https://ellibrodepython.com/tiempo-ejecucion-python
https://pypi.org/project/eulerlib/
https://docs.hektorprofe.net/python/funcionalidades-avanzadas/comprension-de-listas/
"""


# Detectar si un numero sobrepasa el
# limite de R
def todo(n: int, r: int) -> bool:
    list = []

    while n != 0:
        list.append(n % 10)
        n //= 10

    if len(list) < 4:
        return False

    # if len(list) == 4 and list.count(0) == 1:
    #     return False

    if len(list) == 4:
        list.append(0)

    for i in list:
        if list.count(i) > r:
            return False

    return True


def filtrar(lista: list) -> list:
    return [n for n in lista if n >= 1000]


def foo(c: int, r: int, t: int) -> None:
    if r > 5 or r < 1:
        print(-1)
        return
    if t < 1 or t > 100:
        print(-1)
        return

    i = 10000
    a = 0

    div = Divisors(99999)

    while a < t:
        for j in filtrar(div.divisors(i)):
            if todo(i, r) and todo(j, r):
                if i / j == c:
                    print(f"{i}/{j}={c}")
                    a += 1
        i += 1


foo(20, 2, 70)

fin = time.time()
print("Seconds:", fin - inicio)
