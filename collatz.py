def collatz(n):
    leng = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else: n = 3*n+1
        leng += 1
    return leng + 1 

i, j = input().split()
leng = []

for x in range(int(i), int(j)):
    leng.append(collatz(x))

print(max(leng))
