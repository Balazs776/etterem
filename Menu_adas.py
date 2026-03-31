def hozzadas():
    """
    A felhasznalo altal megadott itemek es alapanyagai hozzaadasa a menuhoz, recepthez es raktarhoz.
    """
    import beolvas
    recept_fajl = open("recept.csv", "a", encoding="utf-8")
    menu_fajl = open("menu.csv", "a", encoding="utf-8")
    raktar_fajl = open("raktar.csv", "a", encoding="utf-8")
    hozzaadas_szama = int(input("Hány itemet szeretne hozzáadni a menühoz: "))
    i = 0
    j = 0
    k = 0
    while i < hozzaadas_szama:
        # Menühöz hozzáadás.
        item_fajta = input("A hozzáadandó item ital vagy étel? ")
        item_fajta.lower()
        if item_fajta == "ital":
            menuitem = input(f"Adja meg a(z) {i + 1}. hozzáadandó item nevét: ")
            menuar = input(f"Adja meg a(z) {i + 1} item árát: ")
            menu_fajl.write(f"\n{menuitem};{menuar}")
        elif item_fajta == "étel":
            menuitem = input(f"Adja meg a(z) {i + 1}. hozzáadandó item nevét: ")
            menuar = input(f"Adja meg a(z) {i + 1} item árát: ")
            menu_fajl.write(f"\n{menuitem};{menuar}")

            # Recepthez hozzáadás.
            alapanyagok_szama = int(input("Adja meg a hozzáadandő menü item alapanyagának a számát: "))
            while j < alapanyagok_szama:
                alapanyag_neve = input(f"Adja meg az {j + 1} alapanyag nevét: ")
                alapanyag_mennyisége = int(input(f"Mennyi mennyiség kell a(z) {alapanyag_neve} alapanyagból: "))
                recept_fajl.write(f"\n{menuitem};{alapanyag_neve};{alapanyag_mennyisége}")
                j += 1
                # Megnezzuk, hogy már raktárban van-e az alapanyag.
                while k < len(beolvas.raktar_beolvasasa()):
                    kelle = True
                    if beolvas.raktar_beolvasasa()[k].termek == alapanyag_neve:
                        kelle = False
                    k += 1
                # Ha nem akkor hozzáadom a raktárhoz.
                if kelle:
                    raktari_mennyiseg = int(input(f"Adja meg a(z) {alapanyag_neve} raktárba kerülő mennyiségét: "))
                    raktar_fajl.write(f"\n{alapanyag_neve};{raktari_mennyiseg}")
        i += 1