def raktar_beolvasasa():
    class raktar():
        def __init__(self, termek, darab):
            self.termek = termek
            self.darab = darab
    raktaronlevodolgok = []
    bemenet_files = open("raktar.csv", "W", encoding = "utf-8")
    be = bemenet_files.strip().split(" ")
    while be != "":
        splitelt = be.split(";")
        splitelt[2] = float(splitelt[2])
        raktaronlevodolgok.append(raktar(splitelt[0], splitelt[0]))
        be = bemenet_files.readline().strip()
    return raktaronlevodolgok