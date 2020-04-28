# Second Exercise
from Functions import to_float

while True:
    if (number := to_float(input("Introduceti un numar: "))) is None:
        print("Nu ati introdus un numar!")
        continue
    elif not number.is_integer():
        print("Nu ati introdus un numar intreg!")
        continue
    else:
        number = int(number)
        break

print("Numarul {0} este {1}.".format(number, "par" if number % 2 == 0 else "impar"))
