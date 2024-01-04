L=[]
Som=0
sup=0
for i in range(12):
    Note=float(input(f"Entrez le nombre {i+1}: "))
    L.append(Note)
    Som=Som+Note
Moy=Som/12
for i in L:
    L[0]=sup
    if i>sup:
        sup=i
print(f"le moyen est {Moy} et la superieur est {sup}")