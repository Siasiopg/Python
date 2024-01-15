def sort(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
                if tab[j][0]  > tab[j+1][0]:
                    tab[j], tab[j+1] = tab[j+1], tab[j]
                elif tab[j][0] == tab[j+1][0] and tab[j][1] > tab[j+1][1]:
                    tab[j], tab[j+1] = tab[j+1], tab[j]
                    

tab = []
n = int(input())
for i in range(n):
    tab.append(list(map(int, input().split()))) 

sort(tab)
print("---------")
for x in tab:
    print(x)