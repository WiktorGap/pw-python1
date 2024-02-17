# Testy Jednostkowe (Unit Tests): Obejmują testowanie najmniejszych jednostek kodu, takich jak funkcje, metody czy klasy. 
# Testy jednostkowe są niskopoziomowe i skupiają się na sprawdzaniu poprawności pojedynczych fragmentów kodu.

# Testy Integracyjne: Sprawdzają współpracę między różnymi modułami lub komponentami oprogramowania. 
#Mają na celu upewnienie się, że poszczególne części systemu działają ze sobą poprawnie.

# Testy Akceptacyjne: Sprawdzają, czy całe oprogramowanie spełnia oczekiwania użytkowników i jest gotowe do akceptacji.

#  Testy Jednostkowe:

# Cel Testów Jednostkowych: Zapewnienie, że pojedyncze fragmenty kodu działają zgodnie z oczekiwaniami.

# Biblioteki do Testów w Pythonie:

# unittest: Wbudowana biblioteka do testów jednostkowych w Pythonie.
# pytest: Zewnętrzna biblioteka, popularna ze względu na czytelność i łatwość użycia


#pytest automatycznie znajduje i wykonuje testy w plikach, które zaczynają się od test_ lub kończą na _test.py



# Przykład testu
def test_dodawania():
    assert dodaj(2, 3) == 5


# Przykład parametryzowanego testu
@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-1, 1, 0), (0, 0, 0)])
def test_dodawania_param(a, b, expected):
    assert dodaj(a, b) == expected


# Przykład fixture
@pytest.fixture
def przykladowe_dane():
    return [1, 2, 3, 4, 5]

def test_suma(przykladowe_dane):
    assert sum(przykladowe_dane) == 15

# Klasa do testowania
class MojaKlasa:
    def podwojenie(self, x):
        return x * 2

# Test jednostkowy przy użyciu pytest
def test_podwojenia():
    moja_instancja = MojaKlasa()
    wynik = moja_instancja.podwojenie(3)
    assert wynik == 6, f"Błąd: Oczekiwano 6, otrzymano {wynik}"



#pytest nazwa_pliku_z_testem.py




#@pytest.fixture w pytest oznacza funkcję jako tzw. fixture, czyli fragment kodu, który dostarcza pewne dane lub konfiguracje dla testów. F
#Fixture to mechanizm pozwalający na przygotowanie środowiska testowego i udostępnianie go dla jednego lub wielu testów
    

import pytest

# Definicja fixture
@pytest.fixture
def przykladowe_dane():
    return [1, 2, 3, 4, 5]

# Test wykorzystujący fixture
def test_suma(przykladowe_dane):
    assert sum(przykladowe_dane) == 15
W tym przykładzie:

@pytest.fixture oznacza funkcję przykladowe_dane jako fixture.
#Fixture ta zwraca listę [1, 2, 3, 4, 5].
#W teście test_suma argument przykladowe_dane oznacza, że test ten korzysta z wartości zwróconej przez f