import logging 
logging.basicConfig(filename="car.log",level=logging.INFO, format=('%(levelname)s-%(asctime)s-%(message)s'))

class Car:
    def __init__(self,make,model,year):
        self.__make=make
        self.__model=model
        self.__year=year
        self.__is_production=False
        self.komunikat="Car is in Production"
        self.komunkat1="Car is not in production"

    def is_in_production(self):
        # Metoda start_production rozpoczyna produkcję samochodu, jeżeli nie jest już produkowany. 
        # W przypadku rozpoczęcia produkcji dodaje informację do logów (używając modułu logging). 
        # Jeśli samochód już jest produkowany, dodaje ostrzeżenie do logów
        if not self.__is_production:
            logging.info(f"Rozpoczęcie produkcji {self.__make} {self.__model} {self.__year}")
            self.__is_production=True
        else:
            logging.WARNING("Aktualnie  jest produkowany")
    
    def stop_production(self):
        if self.__is_production:
            # print(f"Zatrzymanie produkcji {self.__make} {self.__model} {self.__year}")
            logging.info(f"Zatrzymanie produkcji {self.__make} {self.__model} {self.__year}")
            self.__is_production = False
        else:
            # print("Aktualnie nie jest produkowany.")
            logging.warning("Aktualnie nie jest produkowany.")
    

    def display_info(self):
        # print(f"Marka: {self.__make}")
        # print(f"Model: {self.__model}")
        # print(f"Rok produkcji: {self.__year}")
        # print(f"Czy jest aktualnie produkcja? {'Tak' if self.__is_production else 'Nie'}")
        logging.info(f"Marka: {self.__make}")
        logging.info(f"Model: {self.__model}")
        logging.info(f"Rok produkcji: {self.__year}")
        logging.info(f"Czy jest aktualnie produkcja? {'Tak' if self.__is_production else 'Nie'}")