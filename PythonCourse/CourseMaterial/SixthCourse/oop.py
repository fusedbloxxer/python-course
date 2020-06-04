# Max este o pisica mare care doarme toata ziua
# object name = max
# class = pisica
# proprietate = mare
# activitatea = doarme

# 0 masina Dacia defecta nu porneste dimineata
# object name = Dacia
# class = masina
# proprietatea = defecta
# activitatea = nu porneste

# obj name => substantiv
# proprietatea => adjectiv
# activitatea => verb

# class Masina:  # definire clasa
#     pass
#
#
# Dacia = Masina()  # obiect
#
# stack = []
#
#
# def push(val):
#     stack.append(val)
#
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
#
# push(3)
# push(2)
# push(1)
#
# print(stack)
#
# print(pop())
# print(pop())
# print(pop())
#
#
# class Stack:
#     def __init__(self):
#         self.__stackList = []
#
#     def push(self, val):
#         self.__stackList.append(val)
#
#     def pop(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
#
#
# # Mosteniri de clasa, de la st la dr
# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def get_sum(self):
#         return self.__sum
#
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val


# stackObject1 = Stack()
# stackObject2 = Stack()
# stackObject3 = Stack()
#
# stackObject1.push(1)
# stackObject2.push(stackObject1.pop() + 1)
# stackObject3.push(stackObject2.pop() - 2)
# 1 + 1 - 2
# print(stackObject3.pop())
#
# stackObject = AddingStack()
#
# for i in range(5):
#     stackObject.push(i)
#
# print(stackObject.get_sum())
#
#
# for i in range(5):
#     print(stackObject.pop())

# class ExampleClass:
#     def __init__(self, val = 1):
#         self.__first = val
#
#     def set_second(self, val):
#         self.__second = val
#
# obj1 = ExampleClass()
# obj2 = ExampleClass(2)
#
# obj2.set_second(3)
#
# obj3 = ExampleClass(4)
# obj3.__third = 5
#
# obj4 = ExampleClass(6)
#
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)
# print(obj4.__dict__)

# class Example:
#     __counter = 0
#
#     def __init__(self, val=1):
#         self.__first = val
#         Example.__counter += 1
#
# obj1 = Example()
# obj2 = Example(2)
# obj3 = Example(4)
# print(obj1.__dict__, Example._Example__counter)
# print(obj1.__dict__, obj1._Example__counter)
# print(obj1.__dict__, obj1._Example__counter)

# class Example:
#     variabila = 1
#
#     def __init__(self, val):
#         self.variabila2 = 3
#         Example.variabila = val
#
# print(Example.__dict__)
# obj1 = Example(2)
# print(Example.__dict__)
# print(obj1.__dict__)

# class Example:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
# obj1 = Example(1)
# print(obj1.a)
# print(obj1.b)

# class Example:
#     __attr = 1
#     __counter = 0
#
#     # def __init__(self, val):
#     #     if val % 2 != 0:
#     #         self.a = 1
#     #     else:
#     #         self.b = 1
#     def method(self):
#         print('method')
#
#
# # obj1 = Example(1)
# # print(obj1.a)
# #
# # try:
# #     print(obj1.b)
# # except AttributeError:
# #     pass
#
# print(hasattr(Example, '__attr'))
#
# obj = Example()
# obj.method()

# class Classy:
#     # variabila = 2
#
#     def other(self):
#         print("other")
#
#     def method(self):
#         print("method")
#         self.other()
#
# obj = Classy()
# obj.method()

# class Classy:
#     def __init__(self, value=None):
#         self.var = value
#
# obj1 = Classy("object")
# obj2 = Classy()
# print(obj1.var)
# print(obj2.var)

# class Classy:
#     def visible(self):
#         print("visible")
#
#     def __hidden(self):
#         print("hidden")
#
# obj = Classy()
# obj.visible()
#
# try:
#     obj.__hidden()
# except:
#     print('failed')
#
#     obj._Classy__hidden()

# class Classy:
#     variabila = 1
#
#     def __init__(self):
#         self.var = 2
#
#     def method(self):
#         pass
#
#     def __hidden(self):
#         pass
#
# obj = Classy()
# print(obj.__dict__)
# print(Classy.__dict__)

# class Class:
#     pass
#
# print(Class.__name__)
# obj = Class()
# print(type(obj).__name__)

# class SuperOne:
#     pass
#
#
# class SuperTwo:
#     pass
#
#
# class SuperThree(SuperOne, SuperTwo):
#     pass
#
#
# def print_bases(cls):
#     for x in cls.__bases__:
#         print(x.__name__)
#
#
# class SuperFour(SuperThree):
#     pass
#
#
# print_bases(SuperOne)
# print_bases(SuperTwo)
# print_bases(SuperThree)
# print_bases(SuperFour)


# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#
#     def __str__(self):
#         return f"{self.name} in {self.galaxy}"
#
#
# sun = Star("Sun", "Milky Way")
# print(sun)

# class Vehicule:
#     pass
#
#
# class VehiculeDeTractare(Vehicule):
#     pass
#
#
# class VehiculeCuRemorca(VehiculeDeTractare):
#     pass
#
#
# # for cls1 in [Vehicule, VehiculeDeTractare, VehiculeCuRemorca]:
# #     for cls2 in [Vehicule, VehiculeDeTractare, VehiculeCuRemorca]:
# #         print(issubclass(cls1, cls2), end='\t')
# #     print()
#
# objVehicule = Vehicule()
# obj = VehiculeDeTractare()
# obj3 = VehiculeCuRemorca()
#
#
# for obj in [objVehicule, obj, obj3]:
#     for cls2 in [Vehicule, VehiculeDeTractare, VehiculeCuRemorca]:
#         print(isinstance(obj, cls2), end='\t')
#     print()
#
# class SampleClass:
#     def __init__(self, val):
#         self.val = val
#
#
# obj1 = SampleClass(0)
# obj2 = SampleClass(2)
# obj3 = obj1
# obj3.val += 1
# # F F T 1 2 1
# print(obj1 is obj2)
# print(obj2 is obj3)
# print(obj3 is obj1)
# print(obj1.val, obj2.val, obj3.val)
# # is - inseamna daca pointeaza la aceeasi zona de memorie
# # == - compara valoarea propriu-zisa
# str1 = "Maria are mere "
# str2 = "Maria are mere galbene"
# str1 += "galbene"
# print(str1 == str2, str1 is str2)
#
#
# class Super:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"My name is {self.name}"
#
#
# class Sub(Super):
#     def __init__(self, name):
#         super(Super).__init__(name)
#         # Super.__init__(self, name)
#
#
# obj = Sub("Alexandra")
# print(obj)

# class Super:
#     a = 1
#
# class Sub(Super):
#     b = 2
#     a = 2
#
# obj = Sub()
# print(obj.b)
# print(obj.a)

# class Super:
#     def __init__(self):
#         self.supVar = 11
#
#
# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar = 12
#
# obj = Sub()
# print(obj.subVar)
# print(obj.supVar)

# class Level1:
#     varia1 = 100
#
#     def __init__(self):
#         self.var1 = 101
#
#     def fun1(self):
#         return 102
#
#
# class Level2(Level1):
#     varia2 = 200
#
#     def __init__(self):
#         super().__init__()
#         # self.var2 = 201
#         self.var1 = 201
#
#     def fun2(self):
#         return 202
#
#     def fun1(self):
#         return 444
#
#
# class Level3(Level2):
#     varia3 = 300
#
#     def __init__(self):
#         super().__init__()
#         self.var3 = 301
#
#     def fun3(self):
#         return 302
#
#
# obj = Level3()
# print(obj.varia1, obj.var1, obj.fun1())
# # print(obj.varia2, obj.var2, obj.fun2())
# print(obj.varia2, obj.fun2())
# print(obj.varia3, obj.var3, obj.fun3())
#
#
# class Left:
#     var = "L"
#     varLeft = "LL"
#
#     def fun(self):
#         return "Left"
#
#
# class Right:
#     var = "R"
#     varRight = "RR"
#
#     def fun(self):
#         return "Right"
#
#
# class Sub(Left, Right):
#     pass
#
#
# obj = Sub()
# print(obj.var, obj.varLeft, obj.varRight, obj.fun())
# # Mostenirea si Cautarea se vor face Left-to-Right
# # Principiul de utilizare al variabilelor este "cautarea" lor
#

# class Calculator:
#     def __init__(self, *vars):
#         self.vars = vars
#
#     def suma(self, *lista):
#         _sum = 0
#         for elem in lista:
#             _sum += elem
#         return _sum
#
#     def diferenta(self, *lista):
#         _dif = 0
#         for elem in lista:
#             _dif -= elem
#         return _dif
#
#     def inmultire(self, *lista):
#         _inm = 1
#         for elem in lista:
#             _inm *= elem
#         return _inm
#
#     def impartire(self, *lista):
#         pass
#
#     def __str__(self):
#         _str = f"{self.suma(vars)}\n{self.diferenta(vars)}\n{self.inmultire(vars)}\n{self.impartire(vars)}\n"
#
#
# calculator = Calculator()
# print(calculator)