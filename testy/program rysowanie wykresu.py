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

# #nalezy zainstalować w terminalu moduły za pomocą komendy: pip install matplotlib numpy





# import turtle
# import math

# # Wprowadzanie danych
# omega = float(input("Wprowadź omegę, czyli prędkość kątową ramki: "))
# n = int(input("Wprowadź N, czyli liczbę ramek: "))
# a = float(input("Wprowadź powierzchnię ramki: "))
# b = float(input("Wprowadź wartość B, czyli wartość indukcji magnetycznej: "))

# # Dane dla wykresu
# czas = 0
# krok_czasowy = 0.1
# amplituda = 100

# # Inicjalizacja turtle
# turtle.speed(1)
# turtle.hideturtle()
# turtle.penup()
# turtle.goto(-400, 0)
# turtle.pendown()

# # Rysowanie osi Y
# turtle.left(90)
# turtle.forward(amplituda)
# turtle.write("Napięcie [V]", align="center", font=("Arial", 12, "normal"))
# turtle.backward(amplituda * 2)

# # Rysowanie osi X
# turtle.right(90)
# turtle.forward(800)
# turtle.write("Czas [s]", align="center", font=("Arial", 12, "normal"))
# turtle.backward(800)

# # Rysowanie wykresu sinusoidalnego
# turtle.penup()
# turtle.goto(-400, amplituda * math.sin(omega * czas) / 2)

# while czas <= 20:
#     napiecie = amplituda * math.sin(omega * czas)
#     x = czas * 40
#     y = napiecie / 2
#     turtle.pendown()
#     turtle.goto(x, y)
#     czas += krok_czasowy

# # Zakończenie rysowania
# turtle.hideturtle()
# turtle.done()







