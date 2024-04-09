# def exp(n,b):
#     if b == 0:
#         return 1
#     res = exp(n, b//2)
#     res *= res
#     if n % 2 == 0:
#         return res
#     return res * n

# def convertR(n, b, r, m, e):
#     if n < r:
#         return m + n * b**e
#     return convertR(n//r, b, r, m + (n % r) * b**e, e + 1)

# def conversor(n, b, r):
#     m = 0
#     e = 0

#     while n >= r:
#         m += (n % r) * b**e
#         e += 1
#         n = n // r
#     m += n * b**e

#     return m

# def hola(n):
#     prod = 1

#     for i in range(1, n+1):
#         suma = 0
#         for j in range(i, i*i+1):
#             suma += exp(j,i)

#         prod *= suma
#         suma = 0

#     return prod

# def suma(i, j, res = 0):
#     if j > i*i:
#         return res
#     return suma(i, j + 1, res + exp(j,i))

# def pi(n, i = 1, res = 1):
#     if i > n:
#         return res
#     return pi(n, i+1, res * suma(i, i, 0))


def suma1(p, i, n, res):
    if p > i * 1:
        return res
    return suma1(p + 1, i, n, res + p * n)


def sumI(k, n, res):
    if k > n:
        return res
    return sumI(k + 1, n, res + k)


def sumL(j, n, res):
    if j > (n * n - 2 * n + 1):
        return res
    return sumL(j + 1, n, res + j)


def prod(i, n, res):
    if i > n:
        return res
    return prod(i + 1, n, res * i * suma1(i, i, n, 0))


def prodAux(n):
    return prod(sumI(1, n, 0), sumL(1, n, 0), 1)


# print(prodAux(3))


def sum1(i, p, n, res):
    if p > i:
        return res
    return sum1(i, p + 1, n, res + p * n)


def sumi(n, k=1, res=0):
    if k > n:
        return res
    return sumi(n, k + 1, res + k)


def sumT(n, j=1, res=0):
    if j > n:
        return res
    return sumT(n, j + 1, res + j)


def pi(t, n, i, res=1):
    if i > t:
        return res
    return pi(t, n, i + 1, res * i * sum1(i * i, i, n, 0))


def aux(n):
    return pi(sumT((n * n) - 2 * n + 1), n, sumi(n), 1)


# print(aux(3)) # 194317694037901482048000

def sqrt_aux(n, i, s, p):
    m = (i + s)/2
    if m*m - p < n and m*m + p > n:
        return m
    if m*m > n:
        return sqrt_aux(n, i, m, p)
    return sqrt_aux(n, m, s, p)

def sqrt(n):
    return sqrt_aux(n, 0, n, 1e-6)