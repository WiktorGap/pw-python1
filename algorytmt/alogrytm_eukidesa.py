# input 2 liczby
# output jedna liczba


# def check_entry(x,y):
#     if x == y:
#         print(x)


# def algorytm(x,y):
#     if check_entry(x,y):
#         return x
#     else:
#         if x > y :
#             x = x - y
#             if not check_entry(x,y):
#                 return x

#         else:
#             y = x - y
#             if not check_entry(x,y):
#                 return y 


# print(algorytm(48,12))





def euk(a,b):
    while b:
        a ,b = b , a % b 
        return a 
euk(50,15)


