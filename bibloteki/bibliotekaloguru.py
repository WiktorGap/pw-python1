import sys
from loguru import logger
logger.debug("That's it, simple logger")

#Loguru ma jedna funkcje do ustawienia forrmattera i handlera
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
#pokolorwane
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
#wyłapanie błedów
@logger.catch
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)
#korzystając z dekoratora / menedżera kontekstu catch(), który zapewnia, że każdy błąd jest poprawnie przekazywany do dziennika.


logger.add("somefile.log", enqueue=True)
#Funkcje korygujące korygujące używane jako źródła są także obsługiwane i powinny być oczekiwane z complete()


#Logowanie wyjątków, które występują w twoim kodzie, jest ważne w celu śledzenia błędów, a
#ale jest dość bezużyteczne, jeśli nie wiesz, dlaczego się nie udało. 
#Loguru pomaga zidentyfikować problemy, pozwalając wyświetlić pełny ślad stosu, wraz z wartościami zmiennych 

# Caution, "diagnose=True" is the default and may leak sensitive data in prod
logger.add("out.log", backtrace=True, diagnose=True)

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)


# 2018-07-17 01:38:43.975 | ERROR    | __main__:nested:10 - What?!
# Traceback (most recent call last):

#   File "test.py", line 12, in <module>
#     nested(0)
#     └ <function nested at 0x7f5c755322f0>

# > File "test.py", line 8, in nested
#     func(5, c)
#     │       └ 0
#     └ <function func at 0x7f5c79fc2e18>

#   File "test.py", line 4, in func
#     return a / b
#            │   └ 0
#            └ 5




#Korzystając z argumentu serialize, każda wiadomość dziennika zostanie przekonwertowana na ciąg JSON przed wysłaniem do skonfigurowanego źródła.
logger.add(custom_sink_function, serialize=True)


#Korzystając z bind(), możesz kontekstualizować wiadomości dziennika, modyfikując atrybut dodatkowy rekord
logger.add("file.log", format="{extra[ip]} {extra[user]} {message}")
context_logger = logger.bind(ip="192.168.0.1", user="someone")
context_logger.info("Łatwo kontekstualizuj swój dziennik")
context_logger.bind(user="someone_else").info("Atrybut extra jest tutaj podstawiony bezpośrednio")
context_logger.info("Użyj kwargs, aby dodać kontekst podczas formatowania: {user}", user="anybody")


#Możesz również mieć bardziej szczegółową kontrolę nad swoimi dziennikami, łącząc bind() i filter
logger.add("special.log", filter=lambda record: "special" in record["extra"])
logger.debug("Ta wiadomość nie jest rejestrowana w pliku")
logger.bind(special=True).info("Ta wiadomość jest rejestrowana w pliku!")



#Wreszcie, metoda patch() pozwala na dynamiczne przypisywanie wartości do słownika rekordu każdej nowej wiadomości
logger.add(sys.stderr, format="{extra[utc]} {message}")
logger = logger.patch(lambda record: record["extra"].update(utc=datetime.utcnow()))


logger.opt(lazy=True).debug("Jeśli poziom źródła <= DEBUG: {x}", x=lambda: expensive_function(2**64))



logger.opt(exception=True).info("Do wiadomości dziennika dodany zostaje ślad stosu błędu (tupla również akceptowana)")
logger.opt(colors=True).info("Kolory na wiadomość <blue>colors</blue>")
logger.opt(record=True).info("Wyświetl wartości z rekordu (np. {record[thread]})")
logger.opt(raw=True).info("Pomiń formatowanie źródła\n")
logger.opt(depth=1).info("Użyj kontekstu stosu nadrzędnego (użyteczne wewnątrz funkcji opakowujących)")
logger.opt(capture=False).info("Argumenty słów kluczowych nie dodawane są do słownika {dest}", dest="extra")


#Dostosowywalne poziomy
#Loguru zawiera wszystkie standardowe poziomy logowania, do których dodano trace() i success(). 
#Potrzebujesz więcej? W takim razie po prostu utwórz nowy poziom za pomocą funkcji level():

new_level = logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")

logger.log("SNAKY", "Zaczynamy!")

logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")


#Używanie loggera w Twoich skryptach jest proste, a możesz go skonfigurować() na początku. 
#Aby użyć Loguru wewnątrz biblioteki, pamiętaj, aby nigdy nie wywoływać add(), ale zamiast tego używaj disable(), 
#aby funkcje logowania stały się no-op. Jeśli deweloper chce zobaczyć dzienniki Twojej biblioteki, może je ponownie włączyć().

# Dla skryptów
config = {
    "handlers": [
        {"sink": sys.stdout, "format": "{time} - {message}"},
        {"sink": "file.log", "serialize": True},
    ],
    "extra": {"user": "someone"}
}
logger.configure(**config)

# Dla bibliotek, powinno być to `__name__` twojej biblioteki
logger.disable("my_library")
logger.info("Nie ważne, jakie dodane źródła, ta wiadomość nie jest wyświetlana")

# W Twojej aplikacji, włącz logger w bibliotece
logger.enable("my_library")
logger.info("Ta wiadomość jednak jest propagowana do źródeł")


