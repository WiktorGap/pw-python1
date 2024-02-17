# # class Matematyka:
# #     @staticmethod
# #     def dodawanie(a,b):
# #         return a+b
    
# # m = Matematyka.dodawanie(5,6)
# # print(m)

# class Matematyka:
#     szerokosc = 0
#     dlugosc = 0
#     def __init__(self,szerokosc,dlugosc):
#         self.dlugosc = dlugosc
#         self.szerokosc = szerokosc

#     def mydecorator(func):
#         def wraper(self):
#             print("Użyto funkcji ")
#             print(func(self))
#             print("Koniec funkcji self.")
#         return wraper


#     @classmethod
#     def kwadrat(cls,bok):
#         return cls(bok,bok)

#     @mydecorator


#     def pole(self):
#         return self.szerokosc * self.dlugosc
    
# # kwadrat = Matematyka.kwadrat(4)
# # print(kwadrat.pole())
# # print(kwadrat.dlugosc)
# # print(kwadrat.szerokosc)
# m = Matematyka(4,5)
# print(m.pole())


# class Matematyka:
#     dlugosc = 0
#     szerokosc = 0
#     def __init__(self, szerokosc , dlugosc):
#         self.szerokosc=szerokosc
#         self.dlugosc=dlugosc

#     def decorator(func):
#         def wrapper(self):
#             print("--------------------")
#             print(func(self))
#             print("--------------------")
#         return wrapper
#     @classmethod
#     def kwadrat(cls,bok)
#         return cls(bok,bok)
    
#     @staticmethod
#     def pomnóż_boki(a,b):
#         return a * b 

    

#     @decorator
#     def obwód(self):
#         x= self.dlugosc * 2
#         y= self.szerokosc *2
#         return x +y





#     @decorator
#     def pole(self):
#         return self.dlugosc * self.szerokosc


# class Książka:
#     def __init__(self,tytuł,autor):
#         self.tytuł=tytuł
#         self.autor=autor
#     def __str__(self):
#         self.liczba_storn = liczba_storn




# ksiazka = Książka("Lalka", "Bolesław Prus")


# class Ksiazka:
#     def __init__(self, tytul, autor, liczba_stron):
#         self.tytul = tytul
#         self.autor = autor
#         self.liczba_stron = liczba_stron
    
#     def __len__(self):
#         return self.liczba_stron

# ksiazka = Ksiazka(tytul="Wiedźmin", autor="Andrzej Sapkowski", liczba_stron=400)
# print(len(ksiazka))  # Wywołuje __len__



# class Ksiazka:
#     def __init__(self, tytul, autor, strony):
#         self.tytul = tytul
#         self.autor = autor
#         self.strony = strony
    
#     def __getitem__(self,key):
#         return self.strony[key]
    
# ksiazka = Ksiazka(tytul="Wiedźmin", autor="Andrzej Sapkowski", strony=[1, 2, 3, 4])
# p1 = ksiazka.strony[2]
# print(p1)


# class MyClass:
#     def __getattribute__(self, name):
#         print(f"Accessing attribute: {name}")
#         return object.__getattribute__(self, name)
    
#     def get

# obj = MyClass()
# obj.some_attribute  # Wywołuje __getattribute__

import logging
#przed uzyciem modułu trzbea skonfigurować
# poziom logowania, formatowanie i miejsce docelowe logów
logging.basicConfig(level=logging.DEBUG,format='  %(asctime)s- %(levelname)s -%(message)s' , )

# %(name)s: Nazwa loggera.
# %(filename)s: Nazwa pliku, w którym występuje zdarzenie logowania.
# %(funcName)s: Nazwa funkcji, w której występuje zdarzenie logowania.
# %(lineno)d: Numer linii, w której występuje zdarze

