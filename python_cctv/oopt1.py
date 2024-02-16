# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def __add__(self,other):
#         return Vector(self.x + other.x , self.y + other.y )
    
#     def __repr__(self):
#         return f"X:{self.x} Y{self.y}"
#     def __len__(self):
#         return 10

# v1 = Vector(10,60)
# v2 = Vector(50,60)
# v3 = v1 + v2

# print(v3.x)
# print(v3.y)

# def mydecorator(func):
#     def wrapper(*args,**kwargs):
#         print("im decoreting yoyt function")
#         return_value = func (*args,**kwargs)

#     return wrapper()

# @mydecorator
# def hello_world(person):
#     return f"Hello World {person}"

# print(hello_world("Mike"))

# def logged(function):
#     def wrapper(**args, **kwargs):
#         value = function(**args,**kwargs)
#         with open('logfile.txt', 'a+') as f:
#             fname = function.__name__
#             print(f.write(f"{fname} returned value {value}"))
#             f.write(f"{fname} returned value {value}\n")
#         return wrapper

# def add(x,y):
#     return x +y




# print(add(10,20))


# import time

# def timed(func):
#     def wrapper(*args,**kwargs):
#         before = time.time()
#         func(*args,**kwargs)
#         after = time.time()
#         fname = function.__name__
#         print(f"{fname} took {after-before} second to execute")
#     return wrapper

# @timed
# def myfunction(x):
#     result = 1
#     for i in range(1,x):
#         result *= i 
#     return result


# def mygenerator(n):
#     for x in range(n):
#         yield x **3

# valeus = mygenerator(2000)
# print*nex

import sys

filename = sys.argv[1]
message = sys.argv[2]

with open(filename,'w+') as f:
    f.write(message)








