
user_choice= -1

tasks = []
tasks.append("wynies smieci")
tasks.append("posprzątaj biurko")

def show_tasks():
    task_index = [0]
    for task in tasks:
        print(task + "[" + str(task_index) + "]")
        task_index += 1


while user_choice != 5:
    if user_choice == 1:
    
    
     show_tasks()   
     if user_choice ==2:
        task = input("wpisz tresc zadania")
        tasks.append(task)
        print("dodadano zad")
    if user_choice ==3:


    print("1. pokaz zad")
    print("2. dodaj zad")
    print("3.usun zad")
    print("4. zapisz zmiany do pliku")
    print("5. wyjdz")

    user_choice = int(input("Podaj liczbę"))