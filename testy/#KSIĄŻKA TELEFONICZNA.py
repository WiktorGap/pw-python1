#KSIĄŻKA TELEFONICZNA

#1
filename = "book.txt"
def read_phonebook():    
    phonebook = {}  
    try:                                  
        with open(filename, "r") as file:  
            for line in file:        
                name, phone_number = line.strip().split('; ') 
                phonebook[phone_number]=name
    except FileNotFoundError:
        pass
    return phonebook



#1:

# Tworzy zmienną FILENAME i przypisuje do niej wartość 'book.txt'. Jest to nazwa pliku, który będzie używany do przechowywania danych książki telefonicznej.
# def read_phonebook():

# Definiuje funkcję read_phonebook(), która będzie odpowiedzialna za odczyt danych książki telefonicznej z pliku.
# phonebook = {}:

# Tworzy pusty słownik phonebook, który będzie przechowywał dane książki telefonicznej, gdzie kluczem będzie numer telefonu, a wartością nazwa.
# try::

# Rozpoczyna blok try (próbuje) - kod w tym bloku będzie próbował wykonać pewne operacje, a jeśli wystąpi wyjątek, przejdzie do bloku except.
# with open(FILENAME, 'r') as file:

# Otwiera plik o nazwie zapisanej w zmiennej FILENAME w trybie do odczytu ('r').
# Korzysta z konstrukcji with, co oznacza, że po zakończeniu bloku with plik zostanie automatycznie zamknięty.
# for line in file:

# Iteruje przez każdą linię w pliku.
# name, phone_number = line.strip().split('; '):

# Dla każdej linii pliku:
# Usuwa białe znaki (spacje, znaki nowej linii) z początku i końca linii za pomocą strip().
# Dzieli linię na dwie części na podstawie separatora '; ' (średnika z spacją).
# Przypisuje pierwszą część do zmiennej name (nazwa) i drugą do zmiennej phone_number (numer telefonu).
# phonebook[phone_number] = name:

# Dodaje do słownika phonebook nowy wpis, gdzie kluczem jest numer telefonu, a wartością jest nazwa.
# except FileNotFoundError:

# Jeśli wystąpi wyjątek FileNotFoundError (plik nie został znaleziony), przejdź do tego bloku.
# pass:

# Blok except jest pusty (słowo kluczowe pass oznacza, że nic nie rób). Brak obsługi wyjątku oznacza, że program po prostu pójdzie dalej bez żadnych działań w przypadku braku pliku.
#2










# def save_phonebook(phonebook):
#     with open(filename,"w") as file:
#         for number, name in phonebook.iteams()
#         file.write(f"{name}; {number}\n")
#     print("phonebook saved")

# file = "book.txt"

# def read_phonebook():
#     phonebook={}
#     try:
#         with open ( file,"r") as file:
#             for line in file:
#                 name, number = line.strip().split("; ")
#                 phonebook[name]=number
#     except FileNotFoundError:
#         pass
#     return phonebook

# def save_phonebook(phonebook):
#     with open(file, "w") as file:
#         for name, number in phonebook.iteams():
#              file.write(f"{name};{number}")
# print("Phonebook saved")



# plik = "book.txt"


# def read_phonebook():
#     phonebook={}
#     try:
#         with open(plik,"r") as file:
#             for lines in file:
#                 name, number = lines.strip().split("; ")
#                 phonebook[name]=number
#     except FileNotFoundError:
#         pass
#     return phonebook

# def save_phonebook(phonebook):
#     with open(plik, "w") as file:
#         for name, number in phonebook.iteams():
#             file.write(f"{name}:{number}")
#             print("Phonebook saved")

# def display_phonebook():
#      phonebook = read_phonebook
#      for name, number in phonebook.iteams():
#          print(f"{name}:{number}")



# filename="book.txt"
# def read_phonebook():
#     phonebook= {}
#     try:
#         with open(filename,"r") as file:
#             for line in file:
#                 name, number = line.strip().split("; ")
#                 phonebook[name]=number
#     except FileNotFoundError:
#         pass
#     return phonebook

def save_phonebook(phonebook):
    with open(filename, "w"):
        for name, number in phonebook.iteams():
            filename.write(f"{name};{number}\n")
        print ("Phonebook saved")

# def display_phonebook():
#     phonebook = read_phonebook
#     for name, number in phonebook.iteams():
#         print(f"{name}:{number}")


# def validate_number(phone_number):
#     return len(phone_number) == 9 and phone_number.isdigit()

# def add_entry(name, phone_number):
#     if not validate_number(phone_number):
#         print("Invalid phone number.")
#         return
#     phonebook = read_phonebook()
#     if phone_number in phonebook:
#         print("Phone number already exists.")
#         return
#     phonebook[phone_number] = name
#     save_phonebook(phonebook)
#     print("Phone number added.")




# def validate_number(phone_number: str):
#     return len(phone_number)==9 and phone_number.isdigit()



# def validate_number(phone_number: str):
#     return phone_number.isdigit() and len(phone_number)==9
    

# def add_entry():
#     phonebook = read_phonebook
#     name = input("Enter name: ")
#     number = input ("Enter number: ")
#     if not validate_number(number):
#         return("Invalid number")
#     if not name.isalpha:
#         return("Invalid name")
#     if name,number in phonebook.iteams():
#         return("This data already exists")
    
#     phonebook[name]=number
#     save_phonebook(phonebook)
#     return("Number and name added ")



# def validate_number(phone_number: str):
#     return phone_number.isdigit() and len(phone_number)==9


# def add_entry(name,phone_number):
#     phonebook = read_phonebook
#     name = input()
#     phone_number = (input)

#     if name.isalpha():
#         return("corect")
#     if phone_number.isdigit():
#         return("corect")
    
#     for name, phone_number in phonebook.items():
#         return()
    
#     phonebook[name]=phone_number
#     save_phonebook(phonebook)




# filename = "plik.txt"

# def read_phonebook():
#     try:
#      phonebook = {}
#      with open (filename, "r") as file:
#         for line in file:
#             name, number = line.strip().split(";")
#             phonebook[name]= number
#     except FileNotFoundError:
#         pass
#     return phonebook


# def save_phonebook(phonebook):
#     with open(filename, "w") as file:
#         for name,number in phonebook.items():
#         file.write(f"{name};{number}\n")

# def display_phonebook()
#     phonebook = read_phonebook
#     for name, number in phonebook.items():
#         print(F"{name}:{number}")


# def validate_number(phone_number):
#     return phone_number.isdigit() and len(phone_number)==9


# def add_entry(name: str,phone_number: str):
#     phonebook = read_phonebook
#     phone_number = input()
#     if not validate_number:
#         return "Invalid number"
    
#     for (name,phone_number) in phonebook.items():
#         return "number and name already exists"

#     phonebook[name]=phone_number
#     save_phonebook(phonebook)         


# filename="book.txt"
# def read_phonebook():
#     try:
#         phonebook = {}
#         with open(filename,"r") as file:
#             for line in file:
#                 number , name = line.strip().split("; ")
#                 phonebook[number] = name
#      except FileNotFoundError:
#         pass
#     return phonebook

# def save_phonebook(phonebook):
#     with open(filename, "w") as file:
#         for number , name in phonebook.items():
#             file.write(f"{number};{name}\n")

# def display_phonebook():
#     phonebook = read_phonebook
#     for number, name in phonebook.items():
#         print(f"{number};{name}")

# def validate_number(number):
#     return number.isdigit() and len(number)==9

# def add_entry(number: str, name: str):
#     phonebook = read_phonebook
#     number = input("podaj namber: ")
#     if not validate_number:
#         return print("Invalid Number")
#     if number in phonebook:
#         return print("Numer egzystuje już w książce")
    
#     phonebook[number]=name
#     save_phonebook(phonebook)
#     print("NUmerinio dodany")

# def remove_entry(number):
#     phonebook = read_phonebook
#     if number in phonebook:
#         del number
#         print("numer istnieje")
#     else:
#         print("taki numer nie istnieje")


# def remove_entry(number):
#     phonebook = read_phonebook
#     if number in phonebook:
#         delete = phonebook.pop(number)
#         print(f"numer usnięty: {delete}")
#     else:
#         print("taki numer nie istnieje")

# def modify_entry(old_phone_number,new_name,new_phone_number):
#     phonebook = read_phonebook

#     if  old_phone_number  not in phonebook:
#         print("number not found")
#         return False
#     if not validate_number(new_phone_number):
#         print("Invalid number")
#         return False
#     del phonebook[old_phone_number]

#     phonebook[new_phone_number]= new_name

#     save_phonebook(phonebook)
#     print("phoenbook entr is modified")

#     return True 
    

filename="book.txt"
def read_phonebook():
    try:
        phonebook = {}
        with open(filename,"r") as file:
            for line in file:
                number , name = line.strip().split("; ")
                phonebook[name]=number
    except FileNotFoundError:
        pass
    return phonebook

def save_phonebook(phonebook):
    with open(filename, "w") as file:
        for name , number in phonebook.items():
            file.write(f"{name}; {number}\n")

def display():
    phonebook = read_phonebook
    for name, number in phonebook.items():
        print(f"{name}; {number}")

def validate_number(number):
    if number.isdigit() and len(number)==9
    return True

def add_entry(name: str,number: str):
    phonebook = read_phonebook
    number = input("Podaj number: ")

    if not validate_number:
        return print("Invalid number")
    
    for number in phonebook:
        phonebook[name]= [number]
    
    save_phonebook(phonebook)
    print("Phonebook saved")

def remove_entry(number):
    phonebook = read_phonebook
    if number in phonebook:
        delte=phonebook.pop(number)
        print(f"numer usunięto{delte}")
    else:
        print(f"twojego numeru{delte} nie ma")
    save_phonebook(phonebook)

# def modify_entry(old_phone_number,new_number,new_name):
#     phonebook = read_phonebook

#     if not validate_number(new_number):
#         return print("Invalid number")
#     if old_phone_number in phonebook:
#         remove_entry(old_phone_number)
#     phonebook[new_number]=new_name
#     save_phonebook(phonebook)


def modify_entry(old_phone_number, new_number, new_name):
    # Wczytanie obecnych danych z pliku
    phonebook = read_phonebook()

    if not validate_number(new_number):
        print("Invalid number")
        return

    # Sprawdzenie, czy stary numer istnieje w książce telefonicznej
    if old_phone_number not in phonebook:
        print("Old phone number not found.")
        return

    # Usunięcie starego numeru telefonu
    remove_entry(old_phone_number)

    # Dodanie nowego wpisu
    phonebook[new_number] = new_name

    # Zapisanie zaktualizowanej książki telefonicznej do pliku
    save_phonebook(phonebook)

    print("Phonebook entry modified.")



    
    














































