filename="book.txt"

def read_phonebook():
    try:
        phonebook={}
        with open(filename,"r") as file:
            for line in file:
                number , name = line.strip().split("; ")
                phonebook[number] = name
    except FileNotFoundError:
        pass
    return phonebook

def save_phonebook(phonebook):
    with open(filename, "w") as file:
        for number,name in phonebook.iteams():
            phonebook[name]=number
            file.write(f"{name}:{number}")
            print("Phonebook saved")

def display_phonebook():
    phonebook = read_phonebook()
    for name, number in phonebook.items():
        print(f"{number};{name}")

def validate_number(number):
    return number.isdigit() and len(number)==3



def add_entry(name,number):
    if not validate_number(number):
        return print("Invalid number, try again.")
    
    phonebook = read_phonebook()
    if (name, number) in phonebook.items():
        return print("This data already exists")
    else:
        phonebook[number]=name
        return print("Number added succesfully")

save_phonebook(phonebook)

def remove_entry(number):
    phonebook = read_phonebook()
    for number in phonebook:
        del phonebook[number]
        save_phonebook(phonebook)
    else:
        print("This number doesn't exsist")

def modify_entry(old_number, new_name, new_phone_number):
    phonebook = read_phonebook()
    if old_number in phonebook:
        del phonebook[old_number]
        phonebook[new_name]=[new_phone_number]
        save_phonebook(phonebook)
    else:
        print("This numebr was not found")