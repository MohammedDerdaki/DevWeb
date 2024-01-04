n = int(input("Entrez un nombre:"))
Som=0
Carre=0
SomImp=0
SomPaire=0
for i in range(n,0,-1):
    Som=Som+i
    if i%2!=0:
        SomImp=SomImp+i
    elif i%2==0:
        SomPaire=SomPaire+i
    Carre = Carre + (i*i)
# 2nd method:
#start
# for j in range(n,0,-1):
#     if j%2==0:
#         continue
#     SomImp = SomImp + j
# for k in range(n,0,-1):
#     if k%2!=0:
#         continue
#     SomPaire = SomPaire + k
#End
print(f"La somme des {n} premiers nombres : {Som}")
print(f"et la somme des carrés des {n} est: {Carre},") 
print(f"et la somme des nombre impaires de 1 à {n} est {SomImp},")
print(f"et la somme des nombres paire de 1 à {n} est {SomPaire}")
