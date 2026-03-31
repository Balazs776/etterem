import random
import raktar_torles_rendeles
import beolvas

def rendelesek():
    class Rendeles:
        def __init__(self, asztal_szama, felszolgalo, vendeg):
            self.asztal_szama = asztal_szama
            self.felszolgalo = felszolgalo
            self.vendeg = vendeg
            self.etelek = []
            self.osszeg = 0
            self.folyamat = "foly"

        def etel_hozzaadas(self, etel_neve, ar):
            """
            Osszeg novelese a rendelt item araval es az item tarolasa emellet a raktar csokkentese.
            """
            self.etelek.append(etel_neve)
            self.osszeg += ar
            raktar_torles_rendeles.rendelesTorles(etel_neve)
            print(f"{etel_neve} hozzáadva az {self.asztal_szama}. asztalhoz.")

        def fizetes(self):
            """
            Vasarlo fizetesenek a fuggvenye.
            """
            if self.folyamat == "fiz":
                fajl = open("vasarlasok.csv", "a", encoding="utf-8")
                print(f"A(z) {self.asztal_szama}. asztal által {self.osszeg} Ft lett kifizetve", end=" ")
                print(*self.etelek, end=",")
                print(f" után.")
                # Azonos rendelt etelek megszamlalasa.
                termekek = []
                darabszamok = []
                i = 0
                while i < len(self.etelek):
                    t = self.etelek[i]
                    talalt = False
                    
                    j = 0
                    while j < len(termekek):
                        if termekek[j] == t:
                            darabszamok[j] = darabszamok[j] + 1
                            talalt = True
                            break 
                        j += 1
                    
                    if talalt == False:
                        termekek.append(t)
                        darabszamok.append(1)

                    i += 1
                self.etelek = []
                k = 0
                while k < len(termekek):
                    if darabszamok[k] == 1:
                        darab = ""
                        self.etelek.append(str(darab) + str(termekek[k]))
                    else:
                        darab = darabszamok[k]
                        self.etelek.append(str(darab) + " " + str(termekek[k]))
                    k += 1
                i = 1
                etelek = self.etelek[0]
                while i < len(self.etelek):
                    etelek += "," + self.etelek[i]
                    i += 1
                
                kiiras = f"{self.vendeg};{self.felszolgalo};{self.osszeg};{etelek}\n"
                fajl.write(kiiras)
    
    szolgalok = ["Marcsi", "Lajos", "Viki", "Özséb", "Dániel"]
    szolgalo = random.randint(0, 4)
    i = 0 
    udvozlo = input("Köszöntöm önt a Magyar Ízek Háza étteremben. Mi a keresztneve? ")
    asztal_szam = int(input("Kérem válasszon egy asztalt!"))

    asztalok = []
    asztalok.append(asztal_szam)


    vendegek = []
    print("Itt is a menünk.")
    print("-------------------------------")
    menu = beolvas.menu_beolvasasa()
    while i < len(menu):
        print(f"{i + 1} {menu[i].etel}")
        i += 1
    print("-------------------------------")

