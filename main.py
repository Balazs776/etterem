import Menu_adas
import beolvas
import Menu_torles
import rendeles
i = 0
while i < 1:
    asztalok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Üdvözlöm a Magyar Ízek Háza étteremben.")
    bemenet = input("Ön vásárló vagy üzletvezető? ")
    if bemenet == "üzletvezető" or bemenet == "Üzletvezető":
        be2 = input("Adja meg az adminisztrációs felhasználónevet: ")
        be1 = input("Adja meg az adminisztrációs jelszót: ")
        if be1 == "maih" and be2 == "Admin":
            be = input("Szeretné bővíteni az asztalok számát? ")
            if be == "Igen" or be == "igen":
                be1 = int(input("Hány asztallal szeretné bővíteni? "))
                i = len(asztalok)
                j = i
                while j <  i + be1 + 1:
                    asztalok.append(j)
                    j += 1
        be2 = input("Szeretne hozzáadni a menühöz? ")
        if be2 == "igen" or be2 == "Igen":
            Menu_adas.hozzadas()
        be3 = input("Szeretne levenni a menüről itemet? ")
        if be3 == "Igen" or be3 == "igen":
            Menu_torles.torles()
        print("Nincs több beállítási lehetőség.\n")
        print("Üdvözlöm a Magyar Ízek Háza étteremben.")
        
    if bemenet == "vásárló" or bemenet == "Vásárló":
        rendeles.rendelesek()
