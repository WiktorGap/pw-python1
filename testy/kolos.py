filename = "działki.txt"


def odczytaj(filename):
    fileds = []
    try:
        with open(filename, "r") as file:
            for line in file:
                długość, szerokość, nazwa = line.strip().split(";")
                fileds.append({'długość': float(długość), 'szerokość': float(szerokość), 'rolnik': nazwa})
    except FileNotFoundError:
        print(f"Plik {filename} nie istnieje.")
        return fileds


def oblicz_powierzchnie(długość, szerokość):
    powierzchnia = float(długość) * float(szerokość)
    return powierzchnia


# def format_fields_data(fields, file):
#     fields_list = []
#     try:
#         with open(file, "a") as file_obj:
#             for field in fields:
#                 długość, szerokość, nazwa = field['długość'], field['szerokość'], field['rolnik']
#                 field_tuple = (długość, szerokość)
#                 fields_list.append((nazwa, field_tuple))

#                 # Zapisanie listy krotek do pliku
#                 file_obj.write(f"Oto wymiary pól rolnika {nazwa}: {fields_list}\n")

#         return fields_list
#     except FileNotFoundError:
#         print(f"Plik {file} nie istnieje.")
#         return []

def format_fields_data(fields, file):
    fields_list = []
    try:
        with open(file, "a") as file_obj:
            for field in fields:
                długość, szerokość, nazwa = field['długość'], field['szerokość'], field['rolnik']
                field_tuple = (długość, szerokość)
                fields_list.append((nazwa, field_tuple))

                # Zapisanie listy krotek do pliku
                file_obj.write(f"Oto wymiary pól rolnika {nazwa}: {field_tuple}\n")

        return fields_list
    except FileNotFoundError:
        print(f"Plik {file} nie istnieje.")
        return []







def wyswietl_informacje_o_dzialkach(filename):
    fields_dict = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                długość, szerokość, nazwa = line.strip().split(";")
                powierzchnia = oblicz_powierzchnie(float(długość), float(szerokość))

                if nazwa not in fields_dict:
                    fields_dict[nazwa] = []

                fields_dict[nazwa].append({'długość': float(długość), 'szerokość': float(szerokość), 'powierzchnia': powierzchnia})

    except FileNotFoundError:
        print(f"Plik {filename} nie istnieje.")
        return

    for rolnik, fields in fields_dict.items():
        print(f"Informacje o działkach rolnika {rolnik}:")
        for field in fields:
            print(f"Długość: {field['długość']}, Szerokość: {field['szerokość']}, Powierzchnia: {field['powierzchnia']} m²")
        laczna_powierzchnia = sum(field['powierzchnia'] for field in fields)
        print(f"Łączna powierzchnia działek rolnika {rolnik}: {laczna_powierzchnia} m\n")

filename = "działki.txt"
fields = odczytaj(filename)

# Wywołanie funkcji oblicz_powierzchnie dla każdej działki i zapisanie danych do pliku
format_fields_data(fields, filename)

# Wyświetlenie informacji o działkach
wyswietl_informacje_o_dzialkach(filename)
