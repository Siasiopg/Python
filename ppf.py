from math import sin, pow
def f(x):
    return pow(x, 2)
def g(x):
    return sin(x)
def sum(h, n):
    dx = 0.88/n
    suma = 0
    for i in range(1, n):
        suma += h((0.88*i)/n)*dx
    return suma


print(sum(g, 10000) - sum(f, 10000))
