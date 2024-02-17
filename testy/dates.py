import datetime
import sys


        #FORMATOWANIE DATY
now = datetime.datetime.now()
#wyswietlanie dzisiejszej daty i godziny
print(f"Dzisiejsza data: {now}")

#wyswietl tylko rok
now_year= now.strftime("%Y")
print(f"dzisiejszy rok: {now_year}")

#wyswietlanie daty w formacie yyyy-mm-dd
data= now.strftime("%Y"'-' "%m"'-' "%d")
print(f"Dzisiejsza data inny format bez godziny {data} ")

#wyswietl tylko miesiąc pełna nazwa
now_month= now.strftime("%B")
print(f"Miesiac pelna nazwa po ang: {now_month}")

#miesiąc skrót nazwy
now_month= now.strftime("%b")
print(f"Miesiac skrócona nazwa po ang: {now_month}")

#miesiąc cyfra
now_month=now.strftime("%m")
print(f"Miesiac cyfra {now_month}")

#miesiąc po polsku
miesiac= {1:"Styczeń",2:"Luty",3:"Marzec",4:"Kwiecień",5:"Maj",6:"Czerwiec",7:"Lipiec",8:"Sierpień",9:"Wrzesień",10:"Październik",11:"Listopad",12:"Grudzień"}
now_month= int(now.strftime("%m"))
month= miesiac[now_month]
print(f"Miesiac po polsku: {month}")

#wyswietl dzien tygodnia
day= now.strftime("%A")
print(f"dzien tygodnia: {day}")






#dodanie n dni, m tygodni do aktualnej daty
add= datetime.datetime.now()
new= add + datetime.timedelta(days=5, weeks=-2)
add= new.strftime("%Y"'-'"%m"'-'"%d")
print(f"dodane n dni i m tygodni do daty {add}")

#podanie przez uzytkownika daty w formacie dd.mm.yyyy i zamiana na date w formacie yyyy-mm-dd
try:
    today= input("podaj date w formacie dd.mm.yyyy : ")
    today_date = datetime.datetime.strptime(today, '%d'"."'%m'"."'%Y')
    today_new_date= today_date.strftime("%Y""-""%m""-""%d")
    print(f"zmieniony format daty podanej przez uzytkownika: {today_new_date}")

   
except ValueError: 
    print("Podaj prawidlowy format daty")
    sys.exit()




        #RÓŻNICE MIEDZY DATAMI
#roznica w latach miedzy podaną data a dzisiejszą
now= datetime.datetime.now()
now_year= now.year
today_date_year=today_date.year
roznica= now_year - today_date_year
print(f"Róznica w latach od podanej daty wynosi: {roznica} lat")
    #roznica w dniach
now= datetime.datetime.now()
roznica= now - today_date
print(f"Róznica w dniach od podanej daty wynosi: {roznica.days} dni")
    #róznica w tygodniach
now= datetime.datetime.now()
roznica= now - today_date
roznica_weeks= roznica.days/7
print(f"Róznica w tygodniach od podanej daty wynosi: {int(roznica_weeks)} tygodni")
    #róznica w godzianch
now= datetime.datetime.now()
roznica= now - today_date
roznica_hours= roznica.days*24
print(f"Róznica w godzinach od podanej daty wynosi: {roznica_hours} godzin")
    #róznica w minutach
now= datetime.datetime.now()
roznica= now - today_date
roznica_min= roznica.days*24*60
print(f"Róznica w minutach od podanej daty wynosi: {roznica_min} minut")
    #róznica w sekundach
now= datetime.datetime.now()
roznica= now - today_date
roznica_sec= roznica.days*24*60*60
print(f"Róznica w sekundach od podanej daty wynosi: {roznica_sec} sekund"



#Pobierz akualna date
from datetime import datetime
from datetime import date
from datetime import timedelta
from datetime import timezone
now = datetime.now()
print(now)
#tylko rok
print(now.year)
#tylko rok za pomoca dyrektyw
print(now.strftime("%Y"))

# #wyswietl aktualny miesiac jako November
# print(now.strftime("%B"))

# #wyświtl aktualny dzien tygodnia
# print(now.strftime("%A"))

# #konwertuj napis "2023-11-15" na obiekt daty
# data_object = datetime.strptime("2023-11-14","%Y-%m-%d")
# print(data_object)

# #dodaj 5dni do aktualnej daty
# data_object = datetime.strptime("2023-11-14","%Y-%m-%d")
# new_date= data_object + timedelta(days=5)
# print(new_date)

# #odejmij 2 tygodnie
# new_now= now + timedelta(weeks=-2)
# print(new_now)

# #wyswietl roznice w dniach 1.01.2023 a dzisiaj
# past_date= datetime(2023,1,1)
# days= now - past_date
# print(days.days)



#sprawdz czy rok 2024 jest przestepny
import calendar

new_year = calendar.isleap(2024)
if new_year: print("jest rok przestępny")
else:print("nie jest to rok przestepny")

#wyswielt numer biezacego tygodnia roku
print(now.strftime("%U"))

#zmien format daty z "2023-11-15" 00:00:00 na format RFC 2822
data_object = datetime.strptime("2023-11-14","%Y-%m-%d")

rfc_date= datetime.strptime("2023-11-15 00:00:00", "%Y-%m-%d %H:%M:%S").strftime("%a,%d %b %Y %H:%M%S +0000")
print(rfc_date)

#znajdz dzien tygodnia dla 4 lipca 2023
data_now= datetime(now.year,now.month,now.day)
print(data_now.strftime("%A"))



# Instrukcje formatowania dat i czasu przy użyciu strftime() i strptime() są elastyczne. Dyrektywy najczęsciej używane przy formatowaniu:

# %Y : rokz pełną liczba cyfr "2023"
# %m : miesiąc jako liczba z zerem wiodących od 01 do 12
# %d dzien miesiaca z zerem wiodącym od 01 do 31
# %H godzina(zegar 24h) jako liczba z zerem wiodącym od 00 do 23
# %I godzina(zegar 12h) jako liczba z zerem wiodącym 0d 01 do 12
# %M minuta jako liczba z zerem wiodącym od 00 do 59
# %S sekunda jako liczba z zerem wiodącym od 00 do 59
# %f mikrosekundy jako liczba z zerem wiodącym od 000000 do 999999
#itd. wiecej na stronie w slack
# każda może byc użyta w metodzie strftime( ) do formatowania obiektu datetime w python lub w metodzie strptime() do parsowania stringu w celu utwozenia obiektu datetime
#strona do dyrektyw dat
https://man7.org/linux/man-pages/man3/strftime.3.html