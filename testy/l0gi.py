import logging
#przed uzyciem modułu trzbea skonfigurować
# poziom logowania, formatowanie i miejsce docelowe logów
logging.basicConfig(level=logging.DEBUG,format='  %(asctime)s- %(levelname)s -%(message)s' , )
# Przykład użycia logów
logging.debug("To jest wiadomość debug")
logging.info("To jest informacja")
logging.warning("To jest ostrzeżenie")
logging.error("To jest błąd")
logging.critical("To jest krytyczny błąd")






# DEBUG (logging.DEBUG):

# Najniższy poziom logowania.
# Służy do debugowania i rejestrowania bardzo szczegółowych informacji dotyczących działania programu.
# Te informacje są przydatne do analizy i identyfikacji problemów na etapie programowania.
# INFO (logging.INFO):

# Poziom informacyjny.
# Służy do rejestrowania ogólnych informacji o przebiegu programu.
# Przydatny do śledzenia ogólnego postępu aplikacji.
# WARNING (logging.WARNING):

# Poziom ostrzeżeń.
# Służy do rejestrowania komunikatów dotyczących potencjalnie problematycznych sytuacji, które nie zatrzymują jeszcze działania programu, ale mogą wymagać uwagi.
# Ostrzeżenia sygnalizują sytuacje, które mogą prowadzić do błędów w przyszłości.
# ERROR (logging.ERROR):

# Poziom błędów.
# Służy do rejestrowania błędów, które nie zatrzymują jeszcze programu, ale wymagają uwagi programisty.
# Komunikaty na poziomie błędów sygnalizują poważniejsze problemy.
# CRITICAL (logging.CRITICAL):

# Najwyższy poziom logowania.
# Służy do rejestrowania krytycznych błędów, które zazwyczaj prowadzą do zatrzymania programu.
# Oznacza poważny problem, który wymaga natychmiastowej interwencji.
# Podczas konfigurowania logowania, możesz określić poziom, od którego logi powinny być uwzględniane. Na przykład, jeśli ustawisz poziom na INFO, to wszystkie logi na poziomie DEBUG zostaną zignorowane, ale logi na poziomie INFO, WARNING, ERROR i CRITICAL będą uwzględniane. Ustawienie niższego poziomu oznacza większą ilość logów rejestrowanych.




# %(name)s: Nazwa loggera.
# %(filename)s: Nazwa pliku, w którym występuje zdarzenie logowania.
# %(funcName)s: Nazwa funkcji, w której występuje zdarzenie logowania.
# %(lineno)d: Numer linii, w której występuje zdarzeń
# %(asctime)s: Data i czas, kiedy log został utworzony. asctime pochodzi od "ascii time".
# %(levelname)s: Poziom logowania, taki jak "DEBUG", "INFO", "WARNING", "ERROR" lub "CRITICAL".
# %(message)s: Treść samego logu.

#Możesz skonfigurować moduł logging do rejestrowania informacji w różnych miejscach, takich jak konsola, plik, czy nawet zdalny serwer.

# logging.basicConfig(filename="app.log", level=logging.debug)


# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler = logging.FileHandler('app.log')
# handler.setFormatter(formatter)

# logger = logging.getLogger('my_logger')
# logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)


# from logging.handlers import RotatingFileHandler

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=5)
# handler.setFormatter(formatter)

# logger = logging.getLogger('my_logger')
# logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)

















import colorlog

logger = colorlog.getLogger()
handler = colorlog.StreamHandler()
#wysyła logi do strumienia wyjściowego/konsoli
#handler do obiekt przetwarzający logi
handler.setFormatter(colorlog.ColoredFormatter('%(log_color)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
#dodaje handlera do logera , loger będzie korzystał ze strumienia handlera czyli logi będą wysyłane do konsoli (można zrobić też np. że będą wysyłane do pliku)
logger.setLevel(logging.DEBUG)



# Dzięki użyciu modułu colorlog, logi o różnych poziomach są automatycznie kolorowane, co ułatwia odróżnienie ich w konsoli. Oto krótka lista kolorów, które są domyślnie przypisane do różnych poziomów logowania:

# DEBUG: Niebieski
# INFO: Zielony
# WARNING: Żółty
# ERROR: Czerwony
# CRITICAL: Magenta (purpurowy)











