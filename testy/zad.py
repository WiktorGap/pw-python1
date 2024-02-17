class Osoba:
    def __init__(self, imie="Jan", nazwisko="Kowalski", wiek=19, adres={}):
        self.imie = imie
        self.nazwisko = nazwisko  # Poprawione: zmiana "naziwsko" na "nazwisko"
        self.wiek = wiek
        self.adres = adres  # Usunięcie nieprawidłowego zapisu, zakładam, że adres jest słownikiem

    def dodaj_adres(self, miasto,ulica,kod_pocztowy):
        self.adres[miasto]= {"ulica": ulica, "kod_pocztowy": kod_pocztowy}


# Tworzenie obiektu Osoba z domyślnymi danymi
osoba1 = Osoba()

# Dodawanie adresu za pomocą metody dodaj_adres
osoba1.dodaj_adres("Warszawa", "Prosta", "00-001")

# Wyświetlanie danych osoby
print(f"Imię: {osoba1.imie}, Nazwisko: {osoba1.nazwisko}, Wiek: {osoba1.wiek}, Adres: {osoba1.adres}")
