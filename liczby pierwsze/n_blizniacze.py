def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(liczba**0.5) + 1):
        if liczba % i == 0:
            return False
    return True


def rozklad_bliźniaczy(n):
    if n % 2 != 0 or n < 2:
        print("Podana liczba nie jest parzysta lub jest mniejsza niż 2.")
        return

    sposoby_rozkładu = 0

    for i in range(2, n // 2 + 1):
        if czy_pierwsza(i) and czy_pierwsza(i + 2):
            sposoby_rozkładu += 1

    return sposoby_rozkładu


def wszystkie_rozklady(n):
    if n % 2 != 0 or n < 2:
        print("Podana liczba nie jest parzysta lub jest mniejsza niż 2.")
        return

    rozklady = []

    for i in range(2, n // 2 + 1):
        if czy_pierwsza(i) and czy_pierwsza(n - i):
            rozklady.append((i, n - i))
    return rozklady


liczba_parzysta = int(input("Podaj liczbe parzysta: "))
wszystkie = wszystkie_rozklady(liczba_parzysta)
sposoby_rozkładu = rozklad_bliźniaczy(liczba_parzysta)


print(
    f"Wszystkie {sposoby_rozkładu} sposoby rozkładu liczby {liczba_parzysta} na liczby bliźniacze to:")
for index, sposob in enumerate(wszystkie, start=1):
    print(f"Sposób {index}: {sposob}")
