L=[]
Som=0
Moy=0
Nbr=int(input("entrez le nombre de list:"))
for i in range(Nbr):
    Note=float(input(f"entrez la note {i+1}:"))
    L.append(Note)
    Som=Som+Note
    Moy=Som/Nbr

print(L)
print(Moy)
# L=[]
# Som=0
# Moy=0
# Nbr=int(input("entrez le nombre de list:"))
# for i in range(Nbr):
#     Note=float(input(f"entrez la note {i+1}:"))
#     L.append(Note)
# for i in range(len(L)):
#     Som=Som+L[i]
# Moy=Som/len(L)
# for i in L:
#     print(i)
# print(f" le moyen  est :{Moy}")