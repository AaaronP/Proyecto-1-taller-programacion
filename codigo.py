import time

# Referencias
"""
https://www.baeldung.com/cs/backtracking-algorithms#:~:text=Backtracking%20is%20an%20algorithmic%20technique,satisfy%20them%20will%20be%20removed.
https://www.w3schools.com/python/python_ref_list.asp
https://www.w3schools.com/python/ref_string_format.asp
https://ellibrodepython.com/tiempo-ejecucion-python
https://docs.hektorprofe.net/python/funcionalidades-avanzadas/comprension-de-listas/
"""


# Detectar si un numero sobrepasa el
# limite de R
def todo(n: int, r: int) -> bool:
    list = [int(i) for i in str(n)]

    if len(list) < 4:
        return False

    if len(list) == 4:
        list.append(0)

    for i in list:
        if list.count(i) > r:
            return False

    return True


def todo2(n1, n2, r):
    list1 = [int(i) for i in str(n1)]
    list2 = [int(i) for i in str(n2)]

    if len(list1) < 4 or len(list2) < 4:
        return False

    if len(list1) == 4:
        list1.append(0)
    if len(list2) == 4:
        list2.append(0)

    list = list1 + list2

    for i in list:
        if list.count(i) > r:
            return False

    return True


def foo(c: int, r: int) -> None:
    if r > 5 or r < 1:
        print(-1)
        return

    b = 9999

    while b <= 99999:
        if todo(b, r):
            k = b // c
            if not b % c and todo2(b, k, r):
                print(f"{b}/{k}={c}")
        b += 1


# cantidad de casos de prueba
t = int(input())

list = []
for i in range(t):
    string = input()
    c, r = string.split()
    list.append((int(c), int(r)))

inicio = time.time()

for i in list:
    foo(i[0], i[1])

fin = time.time()
print("Seconds:", fin - inicio)
