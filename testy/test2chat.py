import re

filename = "bowy.txt"
user = input("Write your name: ")


class Database:
    def __init__(self, filename, user):
        self.filename = filename
        self.user = user
        self.data_base = {}  # Dodajemy atrybut data_base do klasy Database

    def read_file(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    items, user = line.strip().split("--")
                    self.data_base[user] = items
                    print("file exists")
        except FileNotFoundError:
            print("file doesn't exist")


def check_correct_user(user):
    return bool(re.match(r'^[a-zA-Z]{4,8}[!@#$%^&*()_+={}[\]:;<>,.?~\\/]+[0-9]{2,}$', user))


def decorator(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        return result
    return wrapper


def create_list_date(data_base, items, user):
    if data_base.read_file():
        list_of_items = []
        with open(data_base.filename, "a") as file:
            for items in data_base.data_base.values():
                list_of_items.append(items)
                file.write(f"List of items for user {user}: {list_of_items}\n")
            else:
                print("Your file is empty so the list is also")


def change_name_of_owner(new_user, old_user, user, data_base, create_list_date):
    if old_user == user:
        data_base.read_file()
        with open(data_base.filename, "a") as file:
            for items in data_base.data_base.items():
                data_base.data_base.pop(old_user)
                print(f"You deleted old name {old_user}, your new name is {new_user}")
                data_base.data_base[new_user] = items
                file.write(f"List of items for user {new_user}: {list_of_items}\n")
                print("data saved")


@decorator
def remove_permanently_date_from_database(data_base, user):
    if data_base.read_file():
        for user in data_base.data_base:
            del data_base.data_base[user]
            print(f"Data for {user} was deleted")


# Przykład użycia dekoratora
db_instance = Database(filename, user)
create_list_date(db_instance, "item1", user)
change_name_of_owner("new_user", user, user, db_instance, create_list_date)
remove_permanently_date_from_database(db_instance, user)
