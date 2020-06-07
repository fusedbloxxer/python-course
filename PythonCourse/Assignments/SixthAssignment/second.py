def pozitiv(numar: int):
    return numar if numar >= 0 else 0


class Prajitura:
    __prajituri = []

    def __init__(self, nume: str, pret: int, gramaj: int):
        self.__nume = nume
        self.__pret = pozitiv(pret)
        self.__gramaj = pozitiv(gramaj)
        Prajitura.__prajituri.append(self)

    @staticmethod
    def __afisare_prajituri():
        string = ""
        for prajitura in Prajitura.__prajituri:
            string += f"{prajitura}\n"
        return string

    @staticmethod
    def sortare_gramaj(crescator: bool = True):
        Prajitura.__prajituri.sort(key=lambda o: o.__gramaj, reverse=not crescator)
        return Prajitura.__afisare_prajituri()

    @staticmethod
    def sortare_pret(crescator: bool = True):
        Prajitura.__prajituri.sort(key=lambda o: o.__pret, reverse=not crescator)
        return Prajitura.__afisare_prajituri()

    def __str__(self):
        return f"Gramaj: {self.__gramaj}, Nume: {self.__nume}, Pret: {self.__pret}"


class Tort(Prajitura):
    def __init__(self, nume: str, pret: int, gramaj: int, etajat: bool = False, glazura: str = "ciocolata"):
        super().__init__(nume, pret, gramaj)
        self.setare_preferinte(etajat, glazura)

    def setare_preferinte(self, etajat: bool = False, glazura: str = "ciocolata"):
        self.__etajat = etajat
        self.__glazura = glazura

    def citire_preferinte(self):
        preferinte = f"Tortul {'nu ' if self.__etajat else ''}este etajat si "
        preferinte += "nu are glazura." if len(self.__glazura) == 0 else f"are glazura de {self.__glazura}."
        return preferinte


class Fursec(Prajitura):
    def __init__(self, nume: str, pret: int, gramaj: int):
        super().__init__(nume, pret, gramaj)


tort1 = Tort("Deluxe", 80, 250)
tort2 = Tort("Fantastic", 120, 400, False, "fructe")
tort3 = Tort("Extravaganza", 300, 550, glazura="vanilie")

fursec1 = Fursec("Yummy Yum", 10, 25)
fursec2 = Fursec("Creamy", 15, 39)
fursec3 = Fursec("Oreo", 20, 12)

print(Prajitura.sortare_gramaj())
print(Prajitura.sortare_pret())

tort1.setare_preferinte(True, "cacao")
print(tort1.citire_preferinte())
tort2.setare_preferinte(False, "caramel")
print(tort2.citire_preferinte())
tort3.setare_preferinte(True, "")
print(tort3.citire_preferinte())
