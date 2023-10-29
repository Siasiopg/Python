import timeit as tm


def eratostenes(n):
    sieve = [True for _ in range(n+1)]
    sieve[0] = sieve[1] = False
    primes = []
    for i in range(len(sieve)):
        if i <= 1:
            sieve[i] = False
        elif sieve[i]:
            primes.append(i)
            for j in range(i, len(sieve), i):
                sieve[j] = False

    return primes


print('--------------')
randint_time: float = tm.timeit(
    stmt='print(len(eratostenes(1000)))',
    setup='''def eratostenes(n):
                sieve = [True for _ in range(n)]
                sieve[0] = sieve[1] = False
                primes = []
                for i in range(len(sieve)):
                    if i <= 1:
                        sieve[i] = False
                    elif sieve[i]:
                        primes.append(i)
                        for j in range(i, len(sieve), i):
                            sieve[j] = False

                return primes''',
    number=1)
print(f'print(len(eratostenes(1000))): {round(randint_time, 10)}s')

print('--------------')
randint_time: float = tm.timeit(
    stmt='print(len(eratostenes(10000)))',
    setup='''def eratostenes(n):
                sieve = [True for _ in range(n)]
                sieve[0] = sieve[1] = False
                primes = []
                for i in range(len(sieve)):
                    if i <= 1:
                        sieve[i] = False
                    elif sieve[i]:
                        primes.append(i)
                        for j in range(i, len(sieve), i):
                            sieve[j] = False

                return primes''',
    number=1)
print(f'print(len(eratostenes(10000))): {round(randint_time, 10)}s')

print('--------------')
randint_time: float = tm.timeit(
    stmt='print(len(eratostenes(100000)))',
    setup='''def eratostenes(n):
                sieve = [True for _ in range(n)]
                sieve[0] = sieve[1] = False
                primes = []
                for i in range(len(sieve)):
                    if i <= 1:
                        sieve[i] = False
                    elif sieve[i]:
                        primes.append(i)
                        for j in range(i, len(sieve), i):
                            sieve[j] = False

                return primes''',
    number=1)
print(f'print(len(eratostenes(100000))): {round(randint_time, 10)}s')

print('--------------')
randint_time: float = tm.timeit(
    stmt='print(len(eratostenes(1000000)))',
    setup='''def eratostenes(n):
                sieve = [True for _ in range(n)]
                sieve[0] = sieve[1] = False
                primes = []
                for i in range(len(sieve)):
                    if i <= 1:
                        sieve[i] = False
                    elif sieve[i]:
                        primes.append(i)
                        for j in range(i, len(sieve), i):
                            sieve[j] = False

                return primes''',
    number=1)
print(f'print(len(eratostenes(1000000))): {round(randint_time, 10)}s')
