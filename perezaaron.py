# Detectar si un numero sobrepasa el
# limite de r
def todo(n1, n2, r):
    # añadiendo un 0 al numero si solo tiene 4 digitos
    if n2 < 10000:
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
            list.append(f"{b}/{k}={c}\n")

        b += c

    return "".join(list[::-1])


# cantidad de casos de prueba
t = int(input())

cases = []
for i in range(t):
    string = input()
    c, r = string.split()
    cases.append((int(c), int(r)))

tests = []
for i in cases:
    tests.append(foo(i[0], i[1]))

for i in tests:
    with open("output.txt", "a") as f:
        f.write(i + "\n")
