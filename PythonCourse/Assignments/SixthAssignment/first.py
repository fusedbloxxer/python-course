import re
import math


def medie(ls: list):
    suma = 0
    count = 0
    for element in ls:
        suma += element
        count += 1
    return 0 if count == 0 else suma / count


class Catalog:
    def __init__(self, nume: str, prenume: str):
        self.prenume = prenume
        self.nume = nume
        self._materii = {}
        self._absente = 0

    def adauga_absenta(self):
        self._absente += 1

    def sterge_absente(self, numar: int, scutire_medicala: bool):
        if scutire_medicala:
            self._absente = 0 if self._absente < numar else self._absente - numar

    def __str__(self):
        return f"Numar absente prezente in catalog: {self._absente}"


class Extensie1(Catalog):
    __format_nota = re.compile("^([1-9](\\.[0-9]+)?|10)$")

    def __init__(self, nume: str, prenume: str):
        super().__init__(nume, prenume)

    def adauga_materie(self, materie: str, note: list):
        self._materii[materie] = [math.ceil(float(nota)) for nota in note if Extensie1.__este_nota(nota)]

    def materii(self):
        materii = ""
        for materie in self._materii:
            materii += f"{materie} "
        return materii

    def medii(self):
        note_materii = ""
        for materie_note in self._materii.items():
            note_materii += f"La {materie_note[0]} are media {round(medie(materie_note[1]), 2): .2f}.\n"
        return note_materii

    @staticmethod
    def __este_nota(nota: object):
        if not (isinstance(nota, int) or isinstance(nota, float)):
            if not (isinstance(nota, str) and Extensie1.__format_nota.match(str(nota))):
                return False
        return True if 1 <= math.ceil(float(nota)) <= 10 else False


student1 = Extensie1("Ion", "Roata")
for i in range(3):
    student1.adauga_absenta()
student1.sterge_absente(2, True)

student2 = Extensie1("George", "Cerc")
for i in range(4):
    student2.adauga_absenta()
student2.sterge_absente(2, True)

print("{}\n{}\n".format(student1, student2))

student1.adauga_materie("Python", ["4.5", "8.3", "haha", "amuzant"])
student1.adauga_materie("Romana", ["Gresit", 7, "Salut", "Oops"])

student2.adauga_materie("Python", [-100, 8, 3, "5"])
student2.adauga_materie("Matematica", [5, 8, 10])

print(student1.materii())
print(student1.medii())

print(student2.materii())
print(student2.medii())
