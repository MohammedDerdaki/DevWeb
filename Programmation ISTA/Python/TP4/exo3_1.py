L=[]
Som=0
Moy=0
j=0
Nbr=int(input("entrez le nombre de list:"))
for i in range(Nbr):
    Note=float(input(f"entrez la note {i+1}:"))
    L.append(Note)
    if Note>=0 and Note<=20:
        j+=1
    Som=Som+L[i]
Moy=Som/(j)
for i in L:
    if i>=0 and i<=20:
        print(i)
print(f" le moyen  est :{Moy}")