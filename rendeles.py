import random
def rendeles():
    szolgalok = ["Marcsi", "Lajos", "Viki", "Özséb", "Dániel"]
    szolgalo = random.randint(0, 4)
    udvozlo = input("Köszöntöm önt a Magyar Ízek Háza étteremben. Mi a keresztneve? ")
    asztal = int(input("Kérem válasszon egy asztalt! "))
    ugyfel = []
    itemek = []
    árak = []
    osszeg = 0
    ugyfel.append(udvozlo)
    ugyfel.append(szolgalok[szolgalo])
    ugyfel.append(asztal)
    bemenet = input(f"Üdvözlöm önöket én {szolgalok[szolgalo]} vagyok, a pincéretek. Mit adhatok ön(ök)nek")
    fajl = open("menu.csv", "r", encoding="utf-8")
    be = fajl.readline().strip()
    while be != "":
        splitelt = be.split(";")
        itemek.append(splitelt[0])
        árak.append(float(splitelt[1]))
        be = fajl.readline().strip()
    i = 0
    while i < len(itemek):
        if itemek[i] == bemenet:
            osszeg += árak[i]
            ugyfel.append(itemek[i])
        i += 1
    ugyfel.append(osszeg)
    return ugyfel
print(rendeles())
