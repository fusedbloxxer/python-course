from FirstAssignment.Functions import is_num_seq

while True:
    if (number := input("Introduceti un an: ")).isdigit():
        number = int(number)
    elif '.' in number or not is_num_seq(number):
        print("Nu este un an!")
        continue
    else:
        if '+' in number:
            number = int(number.split('+')[1])
        elif '-' in number:
            number = -1 * int(number.split('-')[1])
        else:
            number = int(number)
    break

print("Anul {0} este {1}.".format(number, "bisect" if ((number % 4 == 0 and number % 100 != 0) or number % 400 == 0) else "normal"))