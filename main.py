import Menu_adas
import beolvas
import Menu_torles
import Fizetes
import random

class Rendelesek:
            """
            A rendelesekhez egy osztaly ami tartalmazza a rendeles adatait.
            """
            def __init__(self, asztal_szama, felszolgalo, vendeg):
                self.asztal_szama = asztal_szama
                self.felszolgalo = felszolgalo
                self.vendeg = vendeg
                self.etelek = []
                self.osszeg = 0
                self.folyamat = "foly"

i = 0
vendegek = []
asztalok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while i < 1:
    print("Üdvözlöm a Magyar Ízek Háza étteremben.")
    bemenet = input("Ön vásárló vagy üzletvezető? ")
    if bemenet == "üzletvezető" or bemenet == "Üzletvezető":
        be1 = input("Adja meg az adminisztrációs felhasználónevet: ")
        be2 = input("Adja meg az adminisztrációs jelszót: ")

        if be1 == "maih" and be2 == "Admin":
            admin = True
            while admin:
                print("\n--- ÜZLETVEZETŐI MENÜ ---")
                print("1. Asztalok számának bővítése")
                print("2. Új étel/ital hozzáadása a menühöz")
                print("3. Tétel törlése a menüről")
                print("4. Kilépés az adminisztrációból")
                admin_valaszt = input("Válasszon opciót: ")
                if admin_valaszt == "1":
                    be1 = int(input("Hány asztallal szeretné bővíteni? "))
                    o = len(asztalok)
                    j = o
                    while j <  o + be1 + 1:
                        asztalok.append(j)
                        j += 1
                elif admin_valaszt == "2":
                    Menu_adas.hozzadas()
                elif admin_valaszt == "3":
                    Menu_torles.torles()
                elif admin_valaszt == "4":
                    admin = False
        
    if bemenet == "vásárló" or bemenet == "Vásárló":

        print("\n--- VÁSÁRLÓI MENÜ ---")
        print("1. Új vendég érkezése (asztalfoglalás)")
        print("2. Rendelés hozzáadása meglévő asztalhoz")
        print("3. Vissza a főmenübe")
        valaszt = input("Válasszon opciót: ")
        
        szolgalok = ["Marcsi", "Lajos", "Viki", "Özséb", "Dániel"]
        if valaszt == "1":
            udvozlo = input("Köszöntöm önt a Magyar Ízek Háza étteremben. Mi a keresztneve? ")
            asztal_szam = int(input(f"Kérem válasszon egy asztalt! (1 tól {len(asztalok)} ig)"))
            d = 0 
            
            # Eldöntés tétele
            vane = False
            while d < len(vendegek):
                if vendegek[d].asztal_szama == asztal_szam:
                    vane = True
                d += 1
            if vane == False:
                vendegek.append(Rendelesek(asztal_szam, szolgalok[random.randint(0, 4)], udvozlo))

            print("Itt is a menünk.")
            print("-" * 10)
            menu = beolvas.menu_beolvasasa()
            k = 0
            while k < len(menu):
                print(f"{k + 1} {menu[k].etel}")
                k += 1
            print("-" * 10)

        if valaszt == "2":
            # Kiválasztás tétele
            keresett = int(input("Melyik asztalhoz rögzítsünk rendelést? "))
            aktualis = " "
            h = 0
            while h < len(vendegek):
                if vendegek[h].asztal_szama == keresett:
                    aktualis = vendegek[h]
                    break
                h += 1
            if aktualis == " ":
                print("Ezen az asztalon még nem ül senki!")
            if aktualis != " ":
                print(f"Rendelés felvétele a(z) {aktualis.asztal_szama}. asztalhoz.")
                
                rendel = True
                while rendel:
                    print("1. Étel/Ital/Desszert rendelése")
                    print("2. Rendelés befejezése")
                    print("3. Fizetés")
                    valasztas = input("Válasszon: ")
                    
                    if valasztas == "1":
                        rendelt = input("Folyadék/Étel/Desszert neve: ")
                        l = 0
                        ar = 0
                        # Keresés tétele
                        # Összegzés tétele
                        while l < len(menu):
                            if menu[l].etel == rendelt:
                                ar = menu[l].ar
                            l += 1
                        aktualis.etelek.append(rendelt)
                        aktualis.osszeg += ar
                        print(f"> {rendelt} hozzáadva.\n")
                    elif valasztas == "2":
                        rendel = False
                    elif valasztas == "3":
                        print("-" * 10)
                        print(f"Vevő: {aktualis.vendeg}")
                        print(f"Felszolgáló: {aktualis.felszolgalo}")
                        print(f"Fizetendő: {aktualis.osszeg} Ft")
                        print("-" * 10)
                        folyamat = "fiz"
                        Fizetes.fizetese(folyamat, aktualis.etelek, keresett, aktualis.osszeg, aktualis.vendeg, aktualis.felszolgalo)
                        vendegek.pop(d)
                        rendel = False
        elif valaszt == "3":
            break
        i = 0
