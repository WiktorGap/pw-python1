import matplotlib.pyplot as plt
import numpy as np

# Wprowadzanie danych
omega = float(input("Wprowadź omegę, czyli prędkość kątową ramki: "))
n = int(input("Wprowadź N, czyli liczbę ramek: "))
a = float(input("Wprowadź powierzchnię ramki: "))
b = float(input("Wprowadź wartość B, czyli wartość indukcji magnetycznej: "))

# Generowanie danych czasowych
d = np.arange(0, 2, 0.001)

# Obliczanie wartości napięcia dla każdego czasu
y = omega * n * b * a * np.sin(omega * d)

# Wyświetlanie równania
print("----------------------------------------")
print(f"Wygląd równania: {omega} * {n} * {b} * {a} * sin({omega} * t)")
print("----------------------------------------")

# Wykres
plt.plot(d, y, color="r")
plt.xlabel("Czas w sekundach")
plt.ylabel("Napięcie w Voltach")
plt.title("Wykres napięcia w funkcji czasu")
plt.show()

#nalezy zainstalować w terminalu moduły za pomocą komendy: pip install matplotlib numpy


