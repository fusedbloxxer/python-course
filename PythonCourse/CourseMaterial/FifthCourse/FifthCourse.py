# def prima_functie():
#     # corpul functiei
#     pass
#
#
# def message():
#     print("Enter a value: ")
#
#
# message = 1  # !!! message() - error!
#
# print(message)
#
#
# def hello(name='Andreea'):
#     print("hello", name)
#
#
# name1 = input("Enter your name: ")
#
# hello(name1)
# hello()


# def message(what='phone', number='2'):
#     """
#     :param what:
#     :param number:
#     :return:
#     """
#     print("Enter", what, "number", number)
#
#
# message(number='3', what='number', new_param='oops') # Does not work!
# message(number='3', what='number')

# def suma(a, b, c):
#     print(f"{a} + {b} + {c} = {a + b + c}")
#
#
# # suma(3, c=2, c=1, b=2) # Does not work!
# # suma(3, a=1, b=2) # Does not work!
# suma(3, c=1, b=2)
#
#
# def happy_new_year(wishes=True):
#     print('3')
#     print('2')
#     print('1')
#     if not wishes:
#         return # None!
#     print("Happy new year")
#
# print(happy_new_year(True))

# def name():
#     return 123
#
# a = name()
# print(a)

# def sum_of_list(lst):
#     sum = 0
#     for elem in lst:
#         sum += elem
#     return sum
#
# a = sum_of_list([5, 4, 3])
# print(a)
#
# def u(x):
#     try:
#         if x % 2 == 0:
#             raise ValueError
#         else:
#             return 9
#     except ValueError:
#         return 5
#     finally:
#         return 8
#
# print(u(1))

# def litere(litera: str) -> bool:
#     if isinstance(litera, str):
#         return True
#     else:
#         return '23'
#
# a = litere(3)
# print(a)

# def is_leap_year(year: int) -> bool:
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 == 0:
#         return True
#     return False
#
#
# a = input("Introduceti anul: ")
#
# try:
#     an = int(a)
#     print("Anul este bisect." if is_leap_year(an) else "Anul nu este bisect.")
# except ValueError:
#     print("Nu ati introdus un numar")

# def validate_days(zi: str, luna: str, an: str) -> bool:
#     try:
#         a = datetime.datetime.strptime(f'{zi}.{luna}.{an}', '%d.%m.%Y')
#         print('try')
#         exit(0)
#         return True
#     except Exception as e:
#         print('except', e)
#         return False
#     else:
#         # Cand nu a aparut nicio exceptie
#         print('else')
#     finally:
#         print("Data este: ", zi, luna, an)
#         return False
#
# a = validate_days(20, 7, 2000)
# print(a)

# import math
#
# def is_prime(number: int) -> bool:
#     if number < 2:
#         return False
#     for i in range(2, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# print(is_prime(9))

# def multiply(a, b):
#     return
#
#
# def wishes():
#     return "hAPPY"
#
#
# print(multiply(3, 4))
#
# w = wishes()
# print(w)

# def Hi(MylIST):
#     for name in MylIST:
#         print(f"Hi, {name}")
#         return 'a'
#
# a = Hi(['Adam', 'John', 'Lucy'])
# print(a)

# def create_list(n):
#     myList = []
#     for i in range(n):
#         myList.append(i)
#     return myList
#
#
# print(create_list(5))

# def hi():
#     return
#     print('Hi')
#
# hi()

# def isiNT(DATA):
#     if type(DATA) == int:
#         return True
#     elif type(DATA) == float:
#         return False
#
# print(isiNT(5))
# print(isiNT(5.0))
# print(isiNT("5"))
#
# def evenNumLst(ran):
#     lst = []
#     for num in range(ran):
#         if num % 2 == 0:
#             lst.append(num)
#     return lst
#
# print(evenNumLst(11))
#
# def listUpdater(lst):
#     updList = []
#     for elem in lst:
#         elem **= 2
#         updList.append(elem)
#     return updList
#
# l = [1, 2, 3, 4, 5]
# print(listUpdater(l))

# def scope_test():
#     x = 123
#
# scope_test()
# print(x)

# var = 3
#
# def myFunction():
#     # global var
#     var = 2
#     print('Var este: ', var)
#     return var
#
#
# # var = 1
# myFunction()
# print(var)

# var = 2
#
# print(var)
#
# def multByVar():
#     global var
#     var = 5
#     return var
#
#
# # var = 3
# print(multByVar())
# print(var)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(4))

# def fun(a):
#     if a > 30:
#         return 3
#     else:
#         return a + fun(a + 3)
#
# # 25 + 28 + 3
# print(fun(25))

def pair():
    return 1, 2

a, b = pair()
print(a, b)