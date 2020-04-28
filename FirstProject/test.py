# print("Primul meu string pentru curs 1" * 2)
#
# print(2+2*2-2/1)
#
# a = "String"
# a += 'String1'
# print(type(a))
#
# # concatenare cu format
# a = "1"
# b = "2"
# c = "{1} {0} {1}".format(a, b)
# c = a + ' ' + b
# c = f"{a} {b}"
# print(c)
#
# a = "1"
# b = "2"
# c = int(a) + int(b)
# print(c)
#
# a = "1"
# b = 2
# c = int(a) + b
# print(c)
#
# a = input("Primul nr: ") # Returneaza string !
# b = input("Al doilea nr: ")
# c = int(a) + int(b)
# print(c)

# if conditie:
#     executie
# elif conditie:
#     executie2
# else:
#     executie3

# a = 2    # None - Obiect gol in memorie, nu are nicio valoare
# b = a    # Deep Copy !
# a = 3
#
# print(b)
#
# print(hex(int(id(a))))
# print(hex(int(id(b))))
#
# if a is b:
#     print("a este adevarat")
# elif a > b:
#     print("a este mai mare")
# else:
#     print("a este mai mic")

# while conditie:
#     sintaxa1
#     ...
#     sintaxa2

x = 10

# Nu exista x-- !
while x > 1:
    print("x este ", x)
    pass    # Block de instructiuni GOL - Nu face nimic!
    pass    # Este ca si cum rezerv acest spatiul pentru mai tarziu
    x -= 1

def funct():
    pass

# statement1 if expression1 else (statement2 if expression2 else statement3)

a = 3 if 1 == 1 else 3 if 1 == 5 else 7

# ok = "1"
#
# while ok == "1":
#     ok = input("1. Faceti conversie\n2. Iesiti din program\n")
#     if ok.isdigit() and int(ok) == 1:
#         euro = input("Valoare euro pentru convertire: ")
#         if len(euro) > 0:
#             floatSign = 1
#
#             if euro[0] == '-':
#                 floatSign = -1
#                 euro = euro[1:]
#
#             if euro.isdigit():
#                 euro = int(euro)
#             elif '.' in euro and len(a := euro.split(".")) and a[0].isdigit() and a[1].isdigit():
#                 euro = float(euro)
#             else:
#                 print("Valoarea nu este un numar!")
#                 continue
#             print("Valoarea convertita este: ", floatSign * euro * 4.87, " RON")

str = "abecedar"

print(str[-1])
print(str[-5:])
print(str[2::2])
print(str[::-1])

for x in str:
    print(x)

for poz, char in enumerate(str):
    print(poz, char)

for x in range(6):
    print(x)

for i in range(0, 5, 3):
    print(i)

for x in range(-1, 6, 2):
    print(x)

lista = [x for x in range(10)] # Comprehension list
lista = list(range(10))
print(lista)

# Seturi, dictionare, list, tupluri