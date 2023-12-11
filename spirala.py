import matplotlib.pyplot as plt
import numpy as np

def archimedean_spiral(a, theta):
    """Funkcja opisująca spiralę Archimedesa w współrzędnych biegunowych."""
    r = a * theta
    return r

def plot_archimedean_spiral(a, theta_range):
    """Rysuje spiralę Archimedesa."""
    plt.ion()  # Włącz interaktywny tryb rysowania

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_title('Spirala Archimedesa')
    ax.set_xlabel('Współrzędna X')
    ax.set_ylabel('Współrzędna Y')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

    # Ustawienia zakresów osi X i Y z dodatkowym marginesem
    margin = 5
    ax.set_xlim(-margin, margin)
    ax.set_ylim(-margin, margin)

    for theta in np.linspace(0, theta_range, 1000):
        r = archimedean_spiral(a, theta)
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        # Rysowanie pojedynczego punktu spirali
        ax.plot(x, y, color='#cf0851', marker='o')

        # Odświeżenie wykresu
        plt.pause(0.0000000000000000001)

    plt.ioff()  # Wyłącz interaktywny tryb rysowania
    plt.show()

# Ustawienia spiral
a = 0.25  # Parametr spiral
theta_range = 6 * np.pi  # Zakres kątów

# Rysowanie spirali Archimedesa
plot_archimedean_spiral(a, theta_range)
