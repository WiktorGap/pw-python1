import re
from datetime import datetime, timedelta
visit_time = 1 
max_visits = 8


def validate_number(number):
    return bool(re.match(r"^/d{9}",number))

def check_file_exists(file_path):
    try:
        with open(file_path,"r"):
            pass
        return True
    except FileNotFoundError:
        return False
    
def get_appointments_from_file(file_path):
        appointments = []
        if check_file_exists(file_path):
            with open(file_path,"r") as file:
                for line in file:
                 date =line.strip().split("; ")
                 appointments.append({"name":date[0] , "date":date[1] , "time":date[2]})
        else FileNotFoundError:
            pass
        return appointments

def chceck_availability(appointments,date):
    count = sum(1 for app in appointments if app["date"]==date)
    return count < max_visits

def save_appointment(file_path, number, date, time):
    if not validate_number(number):
        return print("Invalid number format")
    if not chceck_availability(appointments,date):
        return print("No term aviable")
    try:
        appointment_time = datetime.strptime(time, "%H:%M")
    except ValueError:
        return print("incorrect date format")
    work_hours = datetime.strptime("09:00", "%H:%M")
    end_hours = work_hours + timedelta(hours=8)
    appointments = get_appointments_from_file(file_path)
    if (work_hours<=appointment_time<=end_hours):
        with open(file_path,"a") as file:
            appointments.append({"number": number, "date": date, "time": time})
            file.write(f"{number};{date};{time}/n")
            print("Appointment saved")
    else:
        print("Appointment must be between 09:00 and 17:00")


#     available_hours = set(range(9, 17)) - set(int(appointment['time']) for appointment in appointments if appointment['date'] == date)

#     if available_hours:
#         print("\nAvailable hours:")
#         for hour in sorted(available_hours):
#             print(f"{hour}:00 - {hour + visit_time}:00")
#     else:
#         print("\nNo available hours.")


def show_available_hours(file_path, date):
    appointments =get_appointments_from_file(file_path)

    reserved_hours = []
    for appointment in appointments:
        reserved_hours.append(f"{appointment['date']} - {appointment['time']}")
    if reserved_hours:
        print("Reserved hours")
        for reserved_hour in reserved_hours:
            print(reserved_hour)
        else:
            print("no hours reserved")
    
    available_hours = set(range(9,17)) - set(int(appointment['time'])) for appointment in appointments if appointment['date']==date
    if available_hours:
         print("\nAvailable hours:")
         for hour in available_hours:
             print(f"Your visit {hour}:00 - {hour + visit_time}:00")
         else:
             print("No aviable hours")
