import re
import datetime
filename = "bowy.txt"
user = input(str("Write your name"))
#import logging
#logging.basicConfig(filename="filelogin.log",level=logging.DEBUG,format=('%(levelname)s-%(asctime)s-%(message)s'))
#iteams = lista rzeczy użytkownika


class Database:
    def __init__(self, filename , user):
        self.filename =filename
        self.user =user

def check_correct_user(user):
    return bool (re.match(r'^[a-zA-Z]{4,8}[!@#$%^&*()_+={}[\]:;<>,.?~\\/]+[0-9]{2,}$'), user)



def decorator(func):
    def wrapper(self)



def read_file(filename):
    try:
        data_base = {}
        with open(filename, "r") as file:
            for line in file:
                iteams , user = line.strip().split("--")
                data_base[user] = iteams
                print("file exist")
    except FileNotFoundError:
        print("file dosen't exisst")
#zrobv  
#zrobić dekorator??
def create_list_date(data_base, iteams,user):
    if read_file(filename):
        list_of_items = []
        with open(filename, "a") as file:
            user for iteams in data_base.iteams():
                list_of_items.append(iteams)
                file.write(f"List of iteams for user{user} : {list_of_items}\n")
            else:
                print("Your file is empty so list also")


def change_name_of_owner( new_user , old_user , user , data_base, create_list_date):
    if old_user == user:
        read_file(filename)
        with open(filename, "a") as file:
            old_user for iteams in data_base.items():
                data_base.pop(old_user)
                print(f"You delte old name {old_user} , your new name is {new_user}")
                data_base[new_user] = iteams
                file.write(f"List of iteams for user{new_user} : {list_of_items}\n")
                print("data saved")
                






def remove_permamently_date_form_datebase(data_base, user):
    if read_file(filename):
        for user in data_base:
            del data_base[user]
            print(f"Data for {user} was deleted")




            
            
