def rendeles():
    ugyfelek = []
    ugyfelek_szemelyek =[]
    ugyfel = input("Üdvözlöm az éttermünkben, kérem adja meg a nevét! ")
    ugyfel1 = int(input("Köszönom. Kérem válasszon egy asztalt! "))
    i = 0
    while i < len(ugyfelek):
        if ugyfelek[i] == ugyfel:
            ugyfel1 = input("A választott asztal már foglalt, kérem válaszon egy másikat! ")
        i += 1
    ugyfelek_szemelyek.append(ugyfel)
    ugyfelek_szemelyek.append(ugyfel1)
    valasztott = input("Üdvözlöm önt / önöket. Mit adhatok? ")
    ugyfelek_szemelyek.append(valasztott)
rendeles()