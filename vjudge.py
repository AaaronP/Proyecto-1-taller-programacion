def exp(n,b):
    if b == 0:
        return 1
    res = exp(n, b//2)
    res *= res
    if n % 2 == 0:
        return res
    return res * n

def convertR(n, b, r, m, e):
    if n < r:
        return m + n * b**e
    return convertR(n//r, b, r, m + (n % r) * b**e, e + 1)

def conversor(n, b, r):
    m = 0
    e = 0

    while n >= r:
        m += (n % r) * b**e
        e += 1
        n = n // r
    m += n * b**e

    return m

def hola(n):
    prod = 1

    for i in range(1, n+1):
        suma = 0
        for j in range(i, i*i+1):
            suma += exp(j,i)

        prod *= suma
        suma = 0
    
    return prod

def suma(i, j, res = 0):
    if j > i*i:
        return res
    return suma(i, j + 1, res + exp(j,i))

def pi(n, i = 1, res = 1):
    if i > n:
        return res
    return pi(n, i+1, res * suma(i, i, 0))

