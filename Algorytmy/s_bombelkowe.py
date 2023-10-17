#Ponizej wersja wlasna - proba nieudana, pojawiaja sie bledy d[i+1]
'''def bubble(d):
    n = len(d)

    j = 1
    for j in range(n):
        if j < n:
            i = 1
            for i in range(0, n-i-1):
                if i < n:
                    if d[i] > d[i+1]:
                        d[i], d[i+1] = d[i+1], d[i]
                        i+=1
                    else:
                        i+=1
                else:
                    j+=1
                    break
        else: break

k = int(input("Ile elementow chcesz podac: "))
d = []
for i in range(k):
    d.append(int(input()))
print(bubble(d))
'''

def sortowanie_babelkowe(lista):
    n = len(lista)
    
    for i in range(n):
        # Optymalizacja: flaga, która sprawdza, czy w danym przejściu nie dokonano żadnej zamiany
        zamiana = False
        
        for j in range(0, n - i - 1):
            # Porównujemy parę sąsiednich elementów i zamieniamy je, jeśli są w złej kolejności
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                zamiana = True
        
        # Jeśli w tym przejściu nie dokonano żadnej zamiany, lista jest już posortowana
        if not zamiana:
            break

# Przykład użycia:
moja_lista = [64, 34, 25, 12, 22, 11, 90]
sortowanie_babelkowe(moja_lista)
print("Posortowana lista:", moja_lista)
