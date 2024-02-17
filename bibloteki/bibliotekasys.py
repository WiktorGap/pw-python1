import sys

# sys.argv  lista argymentow
# sys.platform   wersja systemu opercyjnegp
# sys.version   wersja pythona
# sys.exit(0)
#sys.path   sciezka wyszukiwania modulow

# print("Liczba argumentów:", len(sys.argv))
# print("Argumenty:", sys.argv)


# print("Ścieżki wyszukiwania modułów:", sys.path)

# Polecenie : sys.stdin, sys.stdout, sys.stderr - Dostęp do standardowego wejścia, wyjścia i błędów.
# Opis: sys.stdin, sys.stdout, sys.stderr umożliwiają dostęp do standardowego wejścia, wyjścia i błędów.
sys.stdout.write("To jest standardowe wyjście.\n")


# Polecenie : sys.stdin.readline() - Odczytuje jedną linię ze standardowego wejścia.
# Opis: sys.stdin.readline() odczytuje jedną linię ze standardowego wejścia.
line = sys.stdin.readline()
print("Wczytana linia:", line)



# Polecenie : sys.stderr.write(msg) - Wypisuje komunikat błędu do standardowego wyjścia błędów.
# Opis: sys.stderr.write(msg) wypisuje komunikat błędu do standardowego wyjścia błędów.
sys.stderr.write("To jest komunikat błędu.\n")



# Polecenie : sys.getsizeof(object[, default]) - Zwraca ilość pamięci zajmowanej przez obiekt.
# Opis: sys.getsizeof(object[, default]) zwraca ilość pamięci zajmowanej przez obiekt.
my_list = [1, 2, 3, 4, 5]
print("Rozmiar listy:", sys.getsizeof(my_list))


# Polecenie : sys.modules - Słownik zawierający załadowane moduły Pythona.
# Opis: sys.modules to słownik zawierający załadowane moduły Pythona.
#print("Załadowane moduły:", sys.modules)



# Polecenie : sys.getfilesystemencoding() - Zwraca kodowanie używane przez system plików.
# Opis: sys.getfilesystemencoding() zwraca kodowanie używane przez system plików.
print("Kodowanie systemu plików:", sys.getfilesystemencoding())


#sys.setrecursionlimit(5000)


# Definicja funkcji trace_function
def trace_function(frame, event, arg):
    # Ta funkcja przyjmuje trzy argumenty:
    # - frame: obiekt reprezentujący stos wywołań (call stack),
    # - event: rodzaj zdarzenia (np. 'call', 'line', 'return', 'exception'),
    # - arg: dodatkowe dane związane z zdarzeniem.

    # Wypisz informacje o zdarzeniu i numerze linii.
    print(f"Event: {event}, Line: {frame.f_lineno}")

# Ustawienie funkcji śledzącej za pomocą sys.settrace
sys.settrace(trace_function)
# sys.settrace pozwala na ustawienie funkcji, która będzie wywoływana przed wykonaniem każdej linii kodu.
# W naszym przypadku używamy funkcji trace_function.

# Definicja przykładowej funkcji example_function
def example_function():
    # Prosta funkcja, która dodaje dwie liczby.
    a = 1
    b = 2
    c = a + b

# Wywołanie funkcji example_function
example_function()
# Wywołanie tej funkcji spowoduje uruchomienie funkcji trace_function przed każdą linią kodu w example_function.

# Przykładowy wynik wykonania:
# Event: call, Line: 19  <-- Zdarzenie 'call' (wywołanie funkcji) na linii 19.
# Event: line, Line: 20  <-- Zdarzenie 'line' (wykonanie linii) na linii 20 (deklaracja zmiennej 'a').
# Event: line, Line: 21  <-- Zdarzenie 'line' na linii 21 (deklaracja zmiennej 'b').
# Event: line, Line: 22  <-- Zdarzenie 'line' na linii 22 (deklaracja zmiennej 'c').
# Event: return, Line: 23  <-- Zdarzenie 'return' (zakończenie funkcji) na linii 23.






def trace_function(frame, event, arg):
    if frame.f_code.co_name == "example_function":
        print(f"Numer linii kodu: {frame.f_lineno}")
    return trace_function

sys.settrace(trace_function)

def example_function():
    a = 1
    b = 2
    c = a + b

def another_function():
    x = 10
    y = 20
    z = x * y

example_function()
another_function()

