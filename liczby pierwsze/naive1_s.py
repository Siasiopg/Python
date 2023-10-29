import timeit as tm


def naive(n):
    liczby = 0
    for i in range(2, n+1):
        d = 2
        while (True):
            if i % d == 0:
                break
            else:
                d += 1
    return liczby


print('--------------')
randint_time: float = tm.timeit(
    stmt='print(naive(1000))',
    setup='''def naive(n):
                liczby = 0
                for i in range(2, n+1):
                    d = 2
                    while (d*d < i):
                        if i % d == 0:
                            break
                        else:
                            d += 1
                    if not d*d <= i:
                        liczby += 1
                return liczby''',
    number=1)

print(f'print(naive(1000)): {round(randint_time, 10)}s')

print('--------------')
randint_time: float = tm.timeit(
    stmt='print(naive(10000))',
    setup='''def naive(n):
                liczby = 0
                for i in range(2, n+1):
                    d = 2
                    while (d*d < i):
                        if i % d == 0:
                            break
                        else:
                            d += 1
                    if not d*d <= i:
                        liczby += 1
                return liczby''',
    number=1)

print(f'print(naive(10000)): {round(randint_time, 10)}s')

print('--------------')
randint_time: float = tm.timeit(
    stmt='print(naive(100000))',
    setup='''def naive(n):
                liczby = 0
                for i in range(2, n+1):
                    d = 2
                    while (d*d < i):
                        if i % d == 0:
                            break
                        else:
                            d += 1
                    if not d*d <= i:
                        liczby += 1
                return liczby''',
    number=1)

print(f'print(naive(100000)): {round(randint_time, 10)}s')

print('--------------')
randint_time: float = tm.timeit(
    stmt='print(naive(1000000))',
    setup='''def naive(n):
                liczby = 0
                for i in range(2, n+1):
                    d = 2
                    while (d*d < i):
                        if i % d == 0:
                            break
                        else:
                            d += 1
                    if not d*d <= i:
                        liczby += 1
                return liczby''',
    number=1)

print(f'print(naive(1000000)): {round(randint_time, 10)}s')
