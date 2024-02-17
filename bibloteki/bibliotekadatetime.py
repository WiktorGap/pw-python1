from datetime import datetime, date, time, timedelta
#W tym przykładzie importujemy klasy datetime, date, time, oraz timedelta z biblioteki datetime


# Aktualna data i czas
now = datetime.now()
print("Aktualna data i czas:", now)

# Wyodrębnianie roku, miesiąca, dnia, godziny, minut, sekund
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

print(f"Rok: {year}, Miesiąc: {month}, Dzień: {day}, Godzina: {hour}, Minuta: {minute}, Sekunda: {second}")


# Dodawanie i odejmowanie timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
yesterday = now - one_day

print("Jutro o tej samej godzinie:", tomorrow)
print("Wczoraj o tej samej godzinie:", yesterday)



# Formatowanie daty i czasu
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Sformatowana data i czas:", formatted_now)


# Parsowanie daty ze stringa
date_string = "2022-01-20"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print("Parsowana data:", parsed_date)


# Tworzenie obiektów date i time
today = date.today()
current_time = datetime.now().time()

print("Dzisiaj:", today)
print("Aktualny czas:", current_time)



# Formatowanie daty i czasu
formatted_date = now.strftime("%A, %B %d, %Y")
formatted_time = now.strftime("%I:%M %p")

print("Sformatowana data:", formatted_date)
print("Sformatowany czas:", formatted_time)



# Operacje na timedelta
three_days_later = now + timedelta(days=3)
one_week_ago = now - timedelta(weeks=1)
one_hour_later = now + timedelta(hours=1)

print("Za trzy dni:", three_days_later)
print("Tydzień temu:", one_week_ago)
print("Za godzinę:", one_hour_later)

# Dodawanie i odejmowanie dni od obiektu date
two_weeks_later = today + timedelta(weeks=2)
three_days_ago = today - timedelta(days=3)

print("Za dwa tygodnie:", two_weeks_later)
print("Trzy dni temu:", three_days_ago)

# Odczytywanie godziny i minuty z obiektu time
hour_of_time = current_time.hour
minute_of_time = current_time.minute

print("Godzina czasu:", hour_of_time)
print("Minuta czasu:", minute_of_time)




from datetime import datetime

now = datetime.now()

# %a - Dzień tygodnia, skrócona wersja
print(now.strftime("%a"))  # Przykład: Wed

# %A - Dzień tygodnia, pełna wersja
print(now.strftime("%A"))  # Przykład: Wednesday

# %w - Dzień tygodnia jako liczba 0-6, 0 to niedziela
print(now.strftime("%w"))  # Przykład: 3 (środa)

# %d - Dzień miesiąca 01-31
print(now.strftime("%d"))  # Przykład: 31

# %b - Nazwa miesiąca, skrócona wersja
print(now.strftime("%b"))  # Przykład: Dec

# %B - Nazwa miesiąca, pełna wersja
print(now.strftime("%B"))  # Przykład: December

# %m - Miesiąc jako liczba 01-12
print(now.strftime("%m"))  # Przykład: 12

# %y - Rok, krótka wersja, bez stulecia
print(now.strftime("%y"))  # Przykład: 22

# %Y - Rok, pełna wersja
print(now.strftime("%Y"))  # Przykład: 2022

# %H - Godzina 00-23
print(now.strftime("%H"))  # Przykład: 17

# %I - Godzina 00-12
print(now.strftime("%I"))  # Przykład: 05

# %p - AM/PM
print(now.strftime("%p"))  # Przykład: PM

# %M - Minuta 00-59
print(now.strftime("%M"))  # Przykład: 41

# %S - Sekunda 00-59
print(now.strftime("%S"))  # Przykład: 08

# %f - Mikrosekunda 000000-999999
print(now.strftime("%f"))  # Przykład: 548513

# %z - Przesunięcie UTC
print(now.strftime("%z"))  # Przykład: +0100

# %Z - Strefa czasowa
print(now.strftime("%Z"))  # Przykład: CST

# %j - Numer dnia w roku 001-366
print(now.strftime("%j"))  # Przykład: 365

# %U - Numer tygodnia w roku, niedziela jako pierwszy dzień tygodnia, 00-53
print(now.strftime("%U"))  # Przykład: 52

# %W - Numer tygodnia w roku, poniedziałek jako pierwszy dzień tygodnia, 00-53
print(now.strftime("%W"))  # Przykład: 52

# %c - Lokalna wersja daty i czasu
print(now.strftime("%c"))  # Przykład: Mon Dec 31 17:41:00 2018

# %C - Wiek
print(now.strftime("%C"))  # Przykład: 20

# %x - Lokalna wersja daty
print(now.strftime("%x"))  # Przykład: 12/31/22

# %X - Lokalna wersja czasu
print(now.strftime("%X"))  # Przykład: 17:41:00

# %% - Znak %
print(now.strftime("%%"))  # Przykład: %

# %G - Rok zgodny z ISO 8601
print(now.strftime("%G"))  # Przykład: 2022

# %u - Dzień tygodnia zgodny z ISO 8601 (1-7)
print(now.strftime("%u"))  # Przykład: 4 (środa)

# %V - Numer tygodnia zgodny z ISO 8601 (01-53)
print(now.strftime("%V"))  # Przykład: 01



now = datetime.now()

# Sformatowana data i czas
formatted_datetime = now.strftime("%A, %B ,%d, %Y %I:%M %p")
print("Sformatowana data i czas:", formatted_datetime)

# Sformatowany rok i miesiąc
formatted_year_month = now.strftime("%Y-%m")
print("Sformatowany rok i miesiąc:", formatted_year_month)

# Sformatowany dzień tygodnia i numer dnia w roku
formatted_weekday_and_day = now.strftime("%A, %j")
print("Sformatowany dzień tygodnia i numer dnia w roku:", formatted_weekday_and_day)
