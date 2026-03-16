def torles():
    import beolvas
    import os
    be = input("Adja meg melyik ételt vagy italt szeretné levenni a menüről: ")
    inputs = open("menu.csv", "r", encoding="utf-8")
    output = open("temp.csv", "w", encoding="utf-8")
    sor = inputs.readline().strip()
    while sor != "":
        splitelt = sor.split(";")
        if splitelt[0] != be:
            output.write(sor)
            output.write("\n")
        sor = inputs.readline().strip()
    os.replace("temp.csv", "menu.csv")