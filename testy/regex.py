mport re
txt = "Dopasowuje nie poznieycję, która nie jest nranicą nie słowa."
x = re.findall("nie",txt,1)
print(x)

x =re.split("\s",txt)
print(x)

x =re.sub("\s","WOW",txt)
print(x)


x =re.findall(r'\bnie\b',txt)
print(x)

x =re.findall(r'[\w]',txt)
print(x)

x =re.findall(r'[\w]+',txt)
print(x)

x =re.findall(r'[\w\.]+',txt)
print(x)

mail= "jakub.chmielak@pw.edu.pl"
#x =re.split("@",mail)
x=re.match("^[\w\.]+@[\w\.]+",mail)
print(x)
print(bool(x))

txt1= "Rok 2023 bedzie lepszy."
x= re.sub("\d","X", txt1)
print(x)

x= re.findall(r"\b[n]\w+", txt)
print(x)

kot= "Nasz kot ma 6 lat i waży 4kg."
x=re.findall(r"\d+",kot)
print(x)

x= re.search( r"^nasz",kot, re.IGNORECASE)
print(x)

nr = "Mój numer telefonu to 623-456-789."
#tel =re.search(r"\d{3}-\d{3}-\d{3}",nr)
tel = re.search(r"\b[4-8][0-9]{2}-\d{3}-\d{3}", nr)
print(tel)
domeny="Odwiedz https://www.example.com i http://www.anotherexample.org"
domain_names= re.findall(r'https?://www\.(\w+)',domeny)
print(domain_names)


# REGEX
# Wyrażenia regularne (regex) to potężne narzędzie do przetwarzania tekstów, które pozwala na wyszukiwane, weryfikacje
# w python
# pip install regex

# import re

# funkcje
# findall - zwraca liste zawierającą wszystkie wystąpienia(nawet w srodku slowa)

# search - zwraca obiekt match, jeśli w dowolnym miejscu znajdzie dopasowanie

# split - zwraca liste ,w której ciągu znaków został podzielony przy każdym dopasowaniu

# sub - zastępuje jedno lub więcej wystapień

# dotycza tylko pojndynczego znaku
# [a-k] - zwraca dopasowania pasujące do wzorów do a-z, małe litery

# [0-9] -

# [michal] - zwraca tylko te litery bez kolejnosci

# [^michal] - zwraca wszystkie poza tymi

# 00-69 [0-6][0-9] ->59 (pasuje)/72(nie pasuje)

# [+] - zwraca każdy znak

# \s - dzieli na liste zdanie po białym znaku

# x =re.sub("\s","WOW",txt) - połączy tekst z WOW- podmienia białe znaki na WOW

# x =re.findall(r'\bnie\b',txt) - r-oznacza row, dopasowuje grani






#Pobierz aktualna date i czas
import datetime
from datetime import timedelta
now= datetime.datetime.now()
import locale
locale.setlocale(locale.LC_ALL, 'pl_PL')
print(now)

#wyswietl aktualny rok
rok= now.year
print(rok)

#aktualny miesiąc i jego nazwe

month= now.strftime("%B")
print(month)

#dodaj 5 dni do aktualnej daty
new_date= now + timedelta(days=5)
print(new_date)

# odejmij 2 tygodnie od dzisiejszej daty
new_date= now + timedelta(weeks=-2)
print(new_date)

#oblicz wiek osoby urodzonej w dniu "1990-05-28"
past= datetime.datetime(1990,5,28).year
old= now.year - past
print(old)

#czyta plik tekstoowy i wyswietli jego zawartosc
filepath = "plik.txt"
f = open(filepath, "r", encoding="utf-8")
print(f.read())