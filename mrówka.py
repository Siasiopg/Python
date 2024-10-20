import numpy as np
import matplotlib.pyplot as p

T = 12.5
r = 5
dt = 0.05
t1 = 3

t = t1
x1 = []
y1 = []

while True:
    x = r * np.sin(2 * np.pi * t / T)
    y = r * np.cos(2 * np.pi * t / T)

    x1.append(x)
    y1.append(y)

    if y > x:
        break

    t += dt

print(
    f"Odpowiedź do zadania 4.1: W {t:.2f} sekundzie od początku ruchu, czyli w {t-3:.2f} sekundzie od 3 sekundy ruchu.\n")

T2 = 10
dt2 = 0.5
v = 1

t2 = np.arange(0, T2 + dt2, dt2)
r2 = v * t2


x_2 = r2 * np.sin(2 * np.pi * t2 / T2)
y_2 = r2 * np.cos(2 * np.pi * t2 / T2)


length = 0
for i in range(1, len(x_2)):
    length_odc = np.sqrt((x_2[i] - x_2[i - 1])**2 + (y_2[i] - y_2[i - 1])**2)
    length += length_odc

print(
    f"Odpowiedź do zadań 4.2 i 4.3: Długość, którą przebyła mrówka: {length:.4f}\n")

p.figure(figsize=(8, 6))
p.plot(x_2, y_2, label='Droga mrówki', color='green')
p.title('Mrówka')
p.xlabel('x')
p.ylabel('y')
p.axhline(0, color='gray', lw=0.5, ls='--')
p.axvline(0, color='gray', lw=0.5, ls='--')
p.grid()
p.axis('equal')
p.legend()
p.show()
