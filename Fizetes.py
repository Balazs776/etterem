import raktar_torles_rendeles


def fizetese(folyamat, etelek, asztal_szama, osszeg, vendeg, felszolgalo):
    """
    Vasarlo fizetesenek a fuggvenye.
     Parameters:
         folyamat (str) - tranzakcio allapota.
         etelek (str) - etelek listaja.
         asztal_szama (int) - asztal szama.
         osszeg (int) - fizetendo osszeg.
         vendeg (str) - vendeg neve.
         felszolgalo (str) - felszolgalo neve.
    """
    if folyamat == "fiz":
        fajl = open("vasarlasok.csv", "a", encoding="utf-8")
        szoveg = ""
        i = 0

        while i < len(etelek):
            szoveg += str(etelek[i])
            if i < len(etelek) - 1:
                szoveg += ", "
            i += 1
        print(f"A(z) {asztal_szama}. asztal által {osszeg} Ft lett kifizetve {szoveg} után.")
        # Azonos rendelt etelek megszamlalasa.
        termekek = []
        darabszamok = []
        i = 0
        while i < len(etelek):
            t = etelek[i]
            talalt = False
            # Megszámlálás tétele
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
        etelek = []
        k = 0
        while k < len(termekek):
            if darabszamok[k] == 1:
                darab = ""
                etelek.append(str(darab) + str(termekek[k]))
            else:
                darab = darabszamok[k]
                etelek.append(str(darab) + " " + str(termekek[k]))
            k += 1
        u = 1
        etelek1 = etelek[0]
        while u < len(etelek):
            etelek1 += "," + etelek[u]
            u += 1
        
        kiiras = f"{vendeg};{felszolgalo};{osszeg};{etelek1}\n"
        fajl.write(kiiras)

