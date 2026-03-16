import Menu_adas
import beolvas
import Menu_torles
import rendeles

asztalok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
be = input("Szeretné bővíteni az asztalok számát? ")
if be == "Igen" or be == "igen":
    be1 = int(input("Hány asztallal szeretné bővíteni? "))
    i = len(asztalok)
    j = i
    while j <  i + be1 + 1:
        asztalok.append(j)
        j += 1
