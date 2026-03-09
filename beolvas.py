def recept_beolvasasa():
    class Recept():
        def __init__(self, etel, alapanyag, mennyiseg):
            self.etel = etel
            self.alapanyag = alapanyag
            self.mennyiseg = mennyiseg
    receptek = []
    bemenet_files1 = open("recept.csv", "r", encoding="utf-8")
    be = bemenet_files1.readline().strip()
    while be != "":
        splitelt = be.split(";")
        splitelt[2] = float(splitelt[2])
        receptek.append(Recept(splitelt[0], splitelt[1], splitelt[2]))
        be = bemenet_files1.readline().strip()
    return receptek

def menu_beolvasasa():
    class menuk():
        def __init__(self, etel, ar):
            self.etel = etel
            self.ar = ar
    menuitemek = []
    bemenet_files2 = open("menu.csv", "r", encoding="utf-8")
    be = bemenet_files2.readline().strip()
    while be != "":
        splitelt = be.split(";")
        splitelt[1] = float(splitelt[1])
        menuitemek.append(menuk(splitelt[0], splitelt[1]))
        be = bemenet_files2.readline().strip()
    return menuitemek

def raktar_beolvasasa():
    class raktar():
        def __init__(self, termek, darab):
            self.termek = termek
            self.darab = darab
    raktaronlevodolgok = []
    bemenet_files3 = open("raktar.csv", "w", encoding = "utf-8")
    be = bemenet_files3.readline().strip()
    while be != "":
        splitelt = be.split(";")
        splitelt[2] = float(splitelt[2])
        raktaronlevodolgok.append(raktar(splitelt[0], splitelt[0]))
        be = bemenet_files3.readline().strip()
    return raktaronlevodolgok