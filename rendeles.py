import random
class Rendeles:
    def __init__(self, asztal_szama, felszolgalo):
        self.asztal_szama = asztal_szama
        self.felszolgalo = felszolgalo
        self.etelek = []
        self.osszeg = 0
        self.lezart = False
 
    def etel_hozzaadas(self, etel_neve, ar):
        self.etelek.append(etel_neve)
        self.osszeg += ar
        print(f"{etel_neve} hozzáadva az {self.asztal_szama}. asztalhoz.")
 
    def fizetes(self):
        self.lezart = True
        print(f"A(z) {self.asztal_szama} asztal által {self.osszeg} Ft lett kifizetve", end=" ")
        print(*self.etelek, end=",")
        print(f" után.")




        
 
 





