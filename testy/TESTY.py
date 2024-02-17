# funkcja .isdigit()

#str = "145135"
#print  (str.isdigit())

#str="Hwdjaku134"

#print(str.isdigit())


#def cheer(who_to_cheer):
#    print(f"Siema {who_to_cheer}!")
#cheer("dałnie")

#ef cheer(how, who):
#    print(how + "," + who + "!")
#cheer("kurwa", "co")

#def suma(x, y):
#    x = int(input("Podaj X"))
#    y = int(input("Podaj Y"))
#    wynik = x + y
#    print(f"Wynik x + y to= {wynik}")
#suma(7, 8)

#def wypisz_liczby():
#    print("Podaj liczby, pierwsza musi być większa!")
#    a= int(input("Podaj A:  "))  
#    b = int(input("Podaj B:  "))
#    if a>b:
#        print(a, b)
#    else:
#        print("Liczby nie spełniają warunku")
#wypisz_liczby()

#def return_number():
#    return 43

#result = return_number()
#print(result)

#def square_x(x):
#    return x * x
#print(square_x(7))

#def absolute(x):
#    if x >= 0:
#        return x
#    else:
#        return -x
    
#print(absolute(-11))
#def silnia(num):
#    result= 1
#    for i in range(1, num+1):
#        result *= i
#    return result
#print(silnia(5))
#d#ef silnia(n):
#    if n > 1:
#        return n*silnia(n-1)
#    return 1
#print(silnia(5))

#def silnia(n):
#    s = 1
#    for i in range(2 , n+1):
#        s *= i
#    else:
#        return s

# def main():
#     print("Podaj liczbę ocen, które będą wchodzić w skład średniej")
#     liczba_ocen = int(input())
#     suma = 0
    
#     for i in range(1, liczba_ocen+1):
#         print("Podaj ocenę " + str(i))
#         ocena = float(input())
#         suma += ocena
    
#     print("Suma ocen to " + str(suma))
#     print("średnia ocen to " + str(suma/liczba_ocen))
    
# if __name__ == "__main__":
#     main()

#PODAJ LICZBE I SPRAWDŹ CZY WIEKSZA OD 10

# liczba = int(input("podaj liczbe: "))
# if (liczba >10):
#     print("liczba wieksza od 10")
# else: print("liczba mniejsza lub równa 10")

#PODAJ WIEK, SPRAWDŹ CZY DZIECKO, MŁODZIEŻ, DOROSŁY

# wiek= int(input("podaj swoj wiek: "))

# if (wiek <10): print("jestes dziecko"):
# elif (wiek <18): print("jestes młodzież")
# else: print("jestes dorosły")



# wiek = int(input("podaj wiek: "))



# if wiek <10:
#     print("jesteś dzieckiem")
# elif wiek<18 ("jesteś młodzierz")
# else: print("jestes dorosły")
           
# DATYY
#WYŚWIETLA AKUTALNA DATĘ I GODZINĘ
# import datetime
# x = datetime.datetime.now()

# ata zawiera rok, miesiąc, dzień, godzinę, minutę, sekundę i mikrosekundę.



# print(x)

# import datetime
# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A"))


# import datetime
# x= datetime.datetime(2027, 7, 3)
# print(x)


# import datetime
# x = datetime.datetime(1986, 10, 29)

# print(x.strftime("%D"))

# import datetime
# x = datetime.datetime.now()

# print(x.strftime("%X"))

# x = min(1,7,-5)
# y = max(5,1,20)

# print(x)
# print(y)

# x = abs(-8.456)  WARTOSC BEZWZGLĘDNA
# print(x)

# x = pow(2, 4)    potęgowanie
# print(x)

# import math

# x = math.sqrt(81)
# print(x)

# import math 

# x = math.ceil(6.1)
# y =  math.floor(9.9)
# print(x)
# print(y)

# import math
# x = math.pi
# print(x)

# import math
# y = math.pi
# x = math.ceil(y)
# print(x)


# x = 
# print(type(x))


# cars = ["bmw","audi","mercedes","opel"]
# cars2= ["ford","alfa romeo","dodge",",ustang"]
# new_list =  cars + cars2
# print(new_list)

# cars = ["bmw","audi","mercedes","opel","ford"]
# cars2= ["ford","alfa romeo","dodge",",ustang"]
# cars.extend(cars2)
# cars.append("volkswagen")
# cars.insert(0, "aston martin")
# cars[2]= "LOL"
# cars.index("bmw")
# for bmw in cars:
#     print("true")
# else: print("false")
# print(cars)
# print(cars[3:6])
# print(cars[::-1])
# print(cars.count("ford"))
# dni_tyg = ("pon","wt","śr","czw","pt","sb","nd")
# pikachu = {'type':'electric', 'attack':55, 'defense':40, 'speed': 90} 
# new_key_for_all = 70
# pikachu.fromkeys()

# import datetime
# # data1= datetime.datetime.now()
# # date2= datetime.datetime(2020, 10, 14)
# # print(data1)
# # print(date2)

# x = datetime.date(2020, 11, 19)
# # print(x)
# import datetime

# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# # Only days, seconds, and microseconds remain
# delta
# print(datetime.timedelta(days=64, seconds=29156, microseconds=10))

# import datetime
# d= datetime.date(2020,5,8)
# print(d)

# import datetime
# d= datetime.date.today()
# print(d.isoweekday())

# import datetime

# tday = datetime.date.today()
# timedelta= datetime.timedelta(days=3)
# print(tday - timedelta)


# tdelta = datetime.timedelta(days=7)

# print(tday + tdelta)

# import datetime 
# tday = datetime.date.today()

# bday = datetime.date(2023, 12 , 30)
# till_bday= bday - tday

# print(till_bday)

# import datetime
# t = datetime.time(9,30,45,10000)
# print(t.hour)

# import datetime
# dt = datetime.datetime.now()
# tdelta = datetime.timedelta(days=8)
# print(dt + tdelta)


# import calendar
# # nov = calendar.TextCalendar(calendar.SUNDAY)
# # nov.prmonth(2023, 11)

# # leaps = calendar.leapdays(2000,2023)
# # print(leaps)
# y1 = int(input("Enter first Year:"))
# y2 = int(input("Enter second Year:"))
# leaps = calendar.leapdays(y1, y2)

# print(f"No. of leap years: {leaps}")

# import calendar
# # year = int(input("enter year to display: "))
# # print(calendar.prcal(year))

# # cal = calendar.TextCalendar(calendar.SATURDAY)
# # for i in cal.itermonthdays(2022, 1):
# #     print(i)
# for name in calendar.month_name:
#     print(name)
# for name in calendar.day_name:
#     print(name)



# import re 
# wzor = r"banan"
# tekst = r"gruszkabananjabłko"

# print(re.match(wzor, tekst))

# if re.match(r".*" + wzor + r".*", tekst):
#     print("Dopasowano!")
# else:
#     print("Nie dopasowano")

# import re

# wynik = re.match(r"^(Hello) (World)+$","Hello World")

# if wynik:
#     print("Dopasowano!")
#     print(wynik.group())
#     print(wynik.group(0))
#     print(wynik.group(1))
#     print(wynik.group(2))
#     print(wynik.groups())
# else:
#     print("nie dopasowano")

# import re

# if re.match(r"^([A-Za-z0-9]+| [A-Za-z0-9][A-Za-z0-9\.-]+[A-Za-z0-9])@([A-za-z0-9]+ | [A-Za-z0-9][A-Za-z0-9-\.]+[A-Za-z0-9])\.[A-Za-z0-9])$", ""):
#     print("dopasowano")
# else:
#     print("nie dopasowano")


# x = 12
# y = 2

# try:
#     print(x +"!")
#     print(x/y)
#     print("Linijka po ")
# except ZeroDivisionError:
#     print("NASTAPILO DZIELENIE PRZEZ ZERo")
# except TypeError:
#     print("błą typów danych")

# print("Dalsze instrukcje...")

#BMI

# def bmi(weight :float, height :float) -> float:
#     calculate = weight/(height**2)
#     return calculate

# def what_bmi(bmi_calc :float)-> float:
#     print(f"Yput NMI ={round(bmi_calc,2)}")
#     if bmi_calc < 18.5 : print("You are underweight.")
#     elif bmi_calc< 24.9: print("You are normal weight.")
#     elif bmi_calc <29.9: print("You are overweight.")
#     else: print("You are obese.")




# def check_float(number)-> bool:
#     try:
#         float(number)
#         return True
#     except ValueError:
#         return False    


# try:  
#     weight= float(input("Enter your weight in kilograms: "))
#     height= float(input("Enter your height in meters: "))
#     if check_float(weight) and check_float(height):
#         bmi_calc= bmi(weight, height)
#         what_bmi(bmi_calc)
#     else: print("Enter only digit")
# except ValueError:
#     print("Invalid input")
# for i in range(0,10):
#     print(i)

