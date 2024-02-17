# Importuje moduł math, który zawiera funkcje matematyczne.
import math

# Oblicza pierwiastek kwadratowy z liczby 25 i przypisuje wynik do zmiennej result.
result = math.sqrt(25)

# Wypisuje wynik obliczeń, który jest pierwiastkiem kwadratowym z 25.
print(result)  # Output: 5.0

# Oblicza 2 do potęgi 3 i przypisuje wynik do zmiennej result.
result = math.pow(2, 3)

# Wypisuje wynik obliczeń, który jest równy 8.
print(result)  # Output: 8.0

# Oblicza wartość e do potęgi 2 i przypisuje wynik do zmiennej result.
result = math.exp(2)

# Wypisuje wynik obliczeń, który jest przybliżoną wartością e do potęgi 2.
print(result)  # Output: 7.3890560989306495

# Oblicza logarytm liczby 8 o podstawie 2 i przypisuje wynik do zmiennej result.
result = math.log(8, 2)

# Wypisuje wynik obliczeń, który jest równy 3.0.
print(result)  # Output: 3.0

# Oblicza sinus kąta π/2 i przypisuje wynik do zmiennej result_sin.
result_sin = math.sin(math.pi/2)

# Oblicza cosinus kąta π i przypisuje wynik do zmiennej result_cos.
result_cos = math.cos(math.pi)

# Oblicza tangens kąta π/4 i przypisuje wynik do zmiennej result_tan.
result_tan = math.tan(math.pi/4)

# Wypisuje wyniki funkcji trygonometrycznych na ekranie.
print(result_sin, result_cos, result_tan)  # Output: 1.0  -1.0  0.9999999999999999



result = math.ceil(4.3)
print(result)  # Output: 5



import math
result = math.floor(4.9)
print(result)  # Output: 4

result = math.factorial(5)
print(result)  # Output: 120

result_sinh = math.sinh(1)
result_cosh = math.cosh(1)
result_tanh = math.tanh(1)
print(result_sinh, result_cosh, result_tanh)

print(math.pi)  # Output: 3.141592653589793
print(math.e)   # Output: 2.718281828459045

angle_in_degrees = 90
angle_in_radians = math.radians(angle_in_degrees)
print(angle_in_radians)  # Output: 1.5707963267948966

