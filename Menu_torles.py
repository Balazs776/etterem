def torles():
    """
    A felhasznalo altal megadott item torlese a menubol es receptbol.
    """
    import beolvas
    import os
    be = input("Adja meg melyik ételt vagy italt szeretné levenni a menüről: ")

    # Menu fajlbol torles.
    inputs = open("menu.csv", "r", encoding="utf-8")
    output = open("temp.csv", "w", encoding="utf-8")
    sor = inputs.readline().strip()
    while sor != "":
        splitelt = sor.split(";")
        if splitelt[0] != be:
            output.write(sor)
            output.write("\n")
        sor = inputs.readline().strip()
    output.close()
    inputs.close()
    os.replace("temp.csv", "menu.csv")

    # Recept fajlbol torles.
    inputs = open("recept.csv", "r", encoding="utf-8")
    output = open("temp.csv", "w", encoding="utf-8")
    sor = inputs.readline().strip()
    while sor != "":
        splitelt = sor.split(";")
        if splitelt[0] != be:
            output.write(sor)
            output.write("\n")
        sor = inputs.readline().strip()
    output.close()
    inputs.close()
    os.replace("temp.csv", "recept.csv")