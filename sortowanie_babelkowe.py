def sort(height):
    n = len(height)
    for i in range(n):
        for j in range(n-i-1):
            if height[j] > height[j+1]:
                height[j], height[j+1] = height[j+1], height[j]
dane = []
n = int(input())
for i in range(n):
    temp = int(input())
    dane.append(temp)

sort(dane)
print(dane)