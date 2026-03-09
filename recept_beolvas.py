def recept_beolvasasa():
    class Recept():
        def __init__(self, etel, alapanyag, mennyiseg):
            self.etel = etel
            self.alapanyag = alapanyag
            self.mennyiseg = mennyiseg
    receptek = []
    bemenet_files = open("recept.csv", "r", encoding="utf-8")
    be = bemenet_files.readline().strip()
    while be != "":
        splitelt = be.split(";")
        splitelt[2] = float(splitelt[2])
        receptek.append(Recept(splitelt[0], splitelt[1], splitelt[2]))
        be = bemenet_files.readline().strip()
    return receptek