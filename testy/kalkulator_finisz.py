# Zadanie 1: Kalkulator Budżetu Domowego
# Cel: Napisz program do zarządzania budżetem domowym. Program powinien umożliwić dodawanie wydatków i przychodów, przechowywać je w pliku i generować podsumowanie budżetu.
# Funkcje:
# Dodawanie wydatku/przychodu. !!!!
# Zapisywanie danych do pliku. !!!!
# Odczytywanie danych z pliku.  !!!
# Generowanie podsumowania (np. łącznych wydatków i przychodów).
# Wyświetlanie historii transakcji.
filename = "budżet.txt"
def Kalkulator(wydatki,przychód)
    wolne_środki = przychód - wydatki 
    return wolne_środki


def read_file(filename):
    budżet = []
    try:
        with open(filename, "r") as file:
            for line in file:
                wydatki , przychód =line.strip().split(";")
                budżet.append({'wydatki':wydatki, 'przychód':przychód})
            return budżet
    except FileNotFoundError:
        print(f"File {filename} dosen't exsist, your list is empty")
        return budżet


def zapisywanie_danych(filename, wydatki, przychód):
    budżet = []
    wolne_środki = Kalkulator(wydatki, przychód)
    try:
        with open(filename, "a") as file:
            budżet.append({'wydatki': wydatki, 'przychód': przychód, 'wolne_środki': wolne_środki})
            file.write(f"wydatki:{wydatki} , przychód:{przychód} ,wolne środki:{wolne_środki}\n")
            print("Data saved")
    except FileNotFoundError:
        print(f"File {filename} doesn't exist")
    return budżet

# def sumuj_klucz(budżet, klucz):
#     return sum(float(pozycja[klucz]) for pozycja in budżet)
# możemy użyć tej funkcji zamiast def generuj_podsumowanie dla konkretych zestawień jakie chcemy zobaczyć, bardziej ogólne podejście
def generuj_podsumowanie(budżet):
    łączne_wydatki = sum(float(pozycja['wydatki']) for pozycja in budżet)
    łączne_przychody = sum(float(pozycja['przychody']) for pozycja in budżet)
    łączne_wolne_środki = łączne_przychody - łączne_wydatki
    print(f"Twoje podsumowanie: łączne wydatki: {łączne_wydatki} , łaczne przychody: {łączne_przychody} , łączne wolne środki:{łączne_wolne_środki} ")