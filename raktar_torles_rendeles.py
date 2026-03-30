import os
def rendelesTorles(torlendo):
    """
    Ez a függvény a rendelés során egy rendelt étel alapanyagát törli a raktárból.
     Parameters:
        torlendo - str -> rendelt étel.
    """

    bemenet = open("recept.csv", "r", encoding="utf-8")
    output = open("temp.csv", "w", encoding="utf-8")
    sorok = bemenet.readline().strip()
    while sorok != "":
        inputs = open("raktar.csv", "r", encoding="utf-8")
        sor = inputs.readline().strip()
        recept = sorok.split(";")
        recept[2] = float(recept[2])
        while sor != "":
            raktar = sor.split(";")
            raktar[1] = float(raktar[1])
            if recept[0] == torlendo:  
                if raktar[0] == recept[1]:
                    raktar[1] = raktar[1] - recept[2]
                    output.write(f"{raktar[0]};{raktar[1]}\n")
            sor = inputs.readline().strip()
        sorok = bemenet.readline().strip()
    inputs.close()
    bemenet.close()

    bemenet = open("recept.csv", "r", encoding="utf-8")
    inputs = open("raktar.csv", "r", encoding="utf-8")
    sorok1 = bemenet.readline().strip()
    sor1 = inputs.readline().strip()
    recept = sorok1.split(";")
    recept[2] = float(recept[2])
    while sor1 != "":
        raktar = sor1.split(";")
        raktar[1] = float(raktar[1])
        if recept[0] != torlendo:
            print(f"{raktar[0]};{raktar[1]}\n")
            output.write(f"{raktar[0]};{raktar[1]}\n")
        sor1 = inputs.readline().strip()

    bemenet.close()
    output.close()
    inputs.close()
    os.replace("temp.csv", "raktar.csv")
rendelesTorles("Tyúkhúsleves")