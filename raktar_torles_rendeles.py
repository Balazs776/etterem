import os
def rendelesTorles(torlendo):
    """
    Ez a függvény a rendelés során egy rendelt étel alapanyagát törli a raktárból.
    Parameters:
        torlendo - str -> rendelt étel.
    """
    # Beolvassuk a raktarat egy listaba.
    raktar_lista = []
    inputs = open("raktar.csv", "r", encoding="utf-8")
    sor = inputs.readline().strip()
    while sor != "":
        adat = sor.split(";")
        adat[1] = float(adat[1])
        raktar_lista.append(adat) 
        sor = inputs.readline().strip()
    inputs.close()

    # Beolvassuk a recepteket es ha egyezik a levonandoval akkor levonjuk a mennyiseget.
    bemenet = open("recept.csv", "r", encoding="utf-8")
    sorok = bemenet.readline().strip()
    while sorok != "":
        recept = sorok.split(";")
        recept_nev = recept[0]
        alapanyag = recept[1]
        mennyiseg = float(recept[2])
        i = 0
        if recept_nev == torlendo:
            while i < len(raktar_lista):
                if raktar_lista[i][0] == alapanyag:
                    raktar_lista[i][1] -= mennyiseg
                i += 1
        sorok = bemenet.readline().strip()
    bemenet.close()

    # Beleirjuk a listat a temp fajlba, majd kicsereljuk a raktar.csv-re.
    output = open("temp.csv", "w", encoding="utf-8")
    i = 0
    while i < len(raktar_lista):
        kiirando = f"{raktar_lista[i][0]};{round(raktar_lista[i][1])}\n"
        output.write(kiirando)
        i += 1
    output.close()
    os.replace("temp.csv", "raktar.csv")
