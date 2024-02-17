import os
current_directory = os.getcwd()
print(current_directory)
#ścieżka aktualnego katalogu

directory_path =  r"C:\\Users\\user\\Desktop\\py\\testy\\bibloteki\"
#print(os.listdir(directory_path))
#lista plików po scieżce do katalogu

#new_directory = os.mkdir(directory_path)

try:
    os.mkdir(directory_path)
    print("New directory was created")
except FileExistsError:
    print('Directory already exists')

print(os.listdir(directory_path))

os.makedirs()
moge stworzyc kilka kataologów 


ścieżka_katalogu_głównego = os.getcwd()
nowy_katalog = "nowy_katalog"

ścieżka_nowego_katalogu = os.path.join(ścieżka_katalogu_głównego, nowy_katalog)

try:
    os.makedirs(ścieżka_nowego_katalogu)
    print("Nowy katalog został utworzony")
except FileExistsError:
    print('Katalog już istnieje')

print(os.listdir(ścieżka_katalogu_głównego))


base = os.getcwd()
# base_path = "/ścieżka/do/bazowego/katalogu"
# file_name = "plik.txt"
filename = "plik.txt"
full_path = os.path.join(base, filename)
print(f"sciezka do pliku:  {full_path}")
# Plik nie musi fizycznie istnieć

sciezka_do_pliku = '/sciezka/do/twojego/pliku.txt'

#os.path.isfile()
if os.path.exists(sciezka_do_pliku):
    print(f"Plik {sciezka_do_pliku} istnieje.")
else:
    print(f"Plik {sciezka_do_pliku} nie istnieje.")

file_to_delete = "sciezka do tego pliku/plik.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print("plik usnięty")

else:
    print("plik istnieje ")




# Dołączanie ścieżek
path = os.path.join("folder", "podfolder", "plik.txt")
print("Pełna ścieżka:", path)

# Rozdziela ścieżkę na katalog i plik
directory, filename = os.path.split(path)
print("Katalog:", directory)
print("Plik:", filename)

# Rozszerzenie pliku
file_name, file_extension = os.path.splitext(path)
print("Nazwa pliku:", file_name)
print("Rozszerzenie:", file_extension)

import os

# Rozdziela ścieżkę na katalog i plik
path = "/katalog/podkatalog/plik.txt"
directory, filename = os.path.split(path)
print("Katalog:", directory)
print("Plik:", filename)


import os

# Sprawdzanie, czy ścieżka istnieje
exists = os.path.exists("/katalog/plik.txt")
is_directory = os.path.isdir("/katalog")
is_file = os.path.isfile("/katalog/plik.txt")

print("Istnieje:", exists)
print("To katalog:", is_directory)
print("To plik:", is_file)



import os

# Normalizacja ścieżki (usuwanie zbędnych kropek, podwójnych ukośników itp.)
normalized_path = os.path.normpath("/katalog/podkatalog/../plik.txt")
print("Normalizowana ścieżka:", normalized_path)
