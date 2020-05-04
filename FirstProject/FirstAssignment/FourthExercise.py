# Fourth Exercise
from FirstAssignment.Functions import to_float

while (number := to_float(input("Introduceti un numar: "))) is None:
    print("Nu ati introdus un numar!")

if number > 0:
    print("Numarul {0} este {1} ca 10.".format(number, "mai mic" if number < 10 else "mai mare"))
elif number == 0:
    print("Numarul este zero.")
else:
    print(f"Valoarea absoluta este {number * -1}.")