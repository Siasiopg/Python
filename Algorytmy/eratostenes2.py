def eratostenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    primes = []

    for current in range(2, int(n**0.5) + 1):
        if sieve[current]:
            for multiple in range(current * current, n + 1, current):
                sieve[multiple] = False

    for num in range(2, n + 1):
        if sieve[num]:
            primes.append(num)

    return primes

n = 5000
prime_numbers = eratostenes(n)
print(f"Ilość liczb pierwszych w przedziale [0, {n}] to:", len(prime_numbers))
n = 50000
prime_numbers = eratostenes(n)
print(f"Ilość liczb pierwszych w przedziale [0, {n}] to:", len(prime_numbers))
n = 500000
prime_numbers = eratostenes(n)
print(f"Ilość liczb pierwszych w przedziale [0, {n}] to:", len(prime_numbers))
n = 5000000
prime_numbers = eratostenes(n)
print(f"Ilość liczb pierwszych w przedziale [0, {n}] to:", len(prime_numbers))
