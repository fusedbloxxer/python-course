from Functions import is_num_seq

inputName = input("Introduceti numele: ")

inputText = input("Introduceti un sir de caractere sau de numere: ")

inputType = "numere" if is_num_seq(inputText, " ,") else "caractere"

print(f"Sirul de {inputType} a fost gasit de {inputName}.")

# Atentie la separatori!
# * Daca consideram separatorul ca fiind vid atunci 12345 se va comporta asemanator cu isdigit (+/- .)