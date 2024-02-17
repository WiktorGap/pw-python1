# import random 

# print("""

# Zaczynamy gre
#       wybierz wpisz:
#       -papier
#       -kamień
#       -nożyce


#       """)

# x = str(input(print("Wybieram: ")))

# lista = ["papier" , "kamień" , "nożyce"]

# y = random.choice(lista)
# def graPapierKamień(x,y):
#     if x == y:
#             print("Remis")
#     elif:
#         if x == "papier" and y == "kamień"
#         print("Wygrałeś, komputer to cipa")
#         else: print("wygrał komputer")
#     elif:
#         if x == "kamień" and y == "nożyce"
#             print("wygrałeś")
#         else:print("przegrałeś")
#     elif:
#         if x == "nożyce" and y=="kamień"
#         print("wygrałeś")
#         else:print("przegrałeś")






import random

print("""
Zaczynamy grę.
Wybierz wpisz:
  - papier
  - kamień
  - nożyce
""")

x = str(input("Wybieram: "))

lista = ["papier", "kamień", "nożyce"]
y = random.choice(lista)

def graPapierKamień(x, y):
    kominikat1="wygrałeś"
    komunikat2="przegrałeś"
    print(f"Wybor komputera: {y}")
    if x == y:
        print("Remis")
    elif x == "papier" and y == "kamień":
        print(kominikat1)
    elif x == "kamień" and y == "nożyce":
        print(kominikat1)
    elif x == "nożyce" and y == "kamień":
        print(kominikat1)
    else:
        print(komunikat2)




def zapisz_wynik(graPapierKamień):
    lista_wygrana = []
    for kominkat1 in range(graPapierKamień):
        lista_wygrana.append(kominkat1)
    return len(lista_wygrana)




