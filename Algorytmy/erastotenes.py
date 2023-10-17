from math import sqrt
def pierwsza(n):
    i = 2
    while(True):
        if i > sqrt(n):
            print(f"Liczba {n} jest liczbą pierwszą.\n")
            break
        elif n % i == 0:
            print(f"Liczba {n} jest liczbą złożoną.\n")
            break
        else:
            i+=1

while(True):
    n = int(input("Podaj liczbę, którą chcesz zbadać: "))
    pierwsza(n)
    k = input("Aby przerwać pętlę wpisz 'exit': ")
    if k == "exit":
        break

#Kod działa poprawnie