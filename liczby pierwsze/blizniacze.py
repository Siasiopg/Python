def eratostenes(a, n):
    sieve = [True] * (n+1-a)
    if a > n:
        print("Wykryto błąd. a musi byc mniejsze od b.")
    primes = []
    for i in range(len(sieve)):
        if i <= 1:
            sieve[i] = False
        elif sieve[i]:
            primes.append(i)
            for j in range(i, len(sieve), i):
                sieve[j] = False
    return primes


# print("Badane liczby z przedzialu [a, b]; a < b; a, b naleza do przedzialu [2, 10^6]")
a = int(input("Podaj a:"))
b = int(input("Podaj b: "))


liczby_pierwsze = eratostenes(a, b)

liczby_blizniacze = []

for k in range(1, len(liczby_pierwsze)):
    x0 = liczby_pierwsze[k - 1]
    x1 = liczby_pierwsze[k]
    if x1 - x0 == 2:
        liczby_blizniacze.append((x0, x1))
print('Liczba par liczb blizniaczych: ', len(liczby_blizniacze))
