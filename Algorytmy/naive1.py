from math import sqrt

def naive(n):
    if n <=1:
        return False
    if n <=3:
        return True
    if n%2 == 0 or n%3 ==0:
        return False
    i = 5
    while i*i <=n:
        if n%i == 0 or n% (i+2) ==0:
            return False
        i+=6
    return True
pierwsze = []
n = 1000
for k in range(2, n+1):
    if naive(k):
        pierwsze.append(k)
print(len(pierwsze))
pierwsze = []
n = 10000
for k in range(2, n+1):
    if naive(k):
        pierwsze.append(k)
print(len(pierwsze))
pierwsze = []
n = 100000
for k in range(2, n+1):
    if naive(k):
        pierwsze.append(k)
print(len(pierwsze))
pierwsze = []
n = 1000000
for k in range(2, n+1):
    if naive(k):
        pierwsze.append(k)
print(len(pierwsze))
