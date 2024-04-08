import time

# Referencias
"""
https://www.baeldung.com/cs/backtracking-algorithms#:~:text=Backtracking%20is%20an%20algorithmic%20technique,satisfy%20them%20will%20be%20removed.
https://www.w3schools.com/python/python_ref_list.asp
https://www.w3schools.com/python/ref_string_format.asp
https://ellibrodepython.com/tiempo-ejecucion-python
"""


# Detectar si un numero sobrepasa el
# limite de r
def todo(n1, n2, r):
    # añadiendo un 0 al numero si solo tiene 4 digitos
    if n1 == 9999:
        n1 *= 10
    if n2 >= 1000 and n2 < 10000:
        n2 *= 10

    list = str(n1) + str(n2)
    for i in list:
        if list.count(i) > r:
            return False

    return True


def foo(c: int, r: int) -> None:
    list = []
    b = 10000
    while b < 100000:
        if b % c:
            b += c
            continue
        k = b // c
        if k < 1000:
            b += c
            continue

        if todo(b, k, r):
            list.append(f"{b}/{k}={c}")

        b += c

    for i in list[::-1]:
        print(i)


# cantidad de casos de prueba
t = int(input())

cases = []
for i in range(t):
    string = input()
    c, r = string.split()
    cases.append((int(c), int(r)))

inicio = time.time()


for i in cases:
    foo(i[0], i[1])
    print()

fin = time.time()
print("Seconds:", fin - inicio)
