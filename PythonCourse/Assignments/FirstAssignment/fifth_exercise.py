from functions import to_float

while True:

    number = input("""1 – Afisare lista de cumparaturi 
2 – Adaugare element 
3 – Stergere element 
4 – Stergere lista de cumparaturi 
5 - Cautare in lista de cumparaturi
$""")

    if (number := to_float(number)) is None:
        print("Nu ati introdus un numar!")
        continue
    elif not number.is_integer():
        print("Numarul nu este intreg!")
        continue
    elif (number := int(number)) == 1:
        print("Afisare lista de cumparaturi")
    elif number == 2:
        print("Adaugare element")
    elif number == 3:
        print("Stergere element")
    elif number == 4:
        print("Stergere lista de cumparaturi")
    elif number == 5:
        print("Cautare in lista de cumparaturi")
    else:
        print("Alegerea nu exista. Reincercati")

# Ar fi util sa comparam cu stringuri
# PRO:  nu mai e nevoie de casturi
# CON:  inputul nu este la fel de flexibil (1.0, 1., etc.)

# Se pot face comparatii de tipul valore <= variabila <= valoare.
# Selectie cod + shift tab ca sa dau codul la stanga
# Daca tipul cu care comparam este boolean atunci putem scrie cu is/not is vs ==/!=