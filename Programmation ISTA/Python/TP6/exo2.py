L=[-12,10,100,0,-20,12.5,-1.9]
liste=[]
for j in range(len(L)):
    N=L[0]
    for i in L:
        if N>i:
            N=i
    liste.append(N)
    L.remove(N)
print(liste)
nbr=int(input("entrez un nombre: "))
liste.append(nbr)
for j in range(len(liste)):
    N=liste[0]
    for i in liste:
        if N>i:
            N=i
    L.append(N)
    liste.remove(N)
print(L)