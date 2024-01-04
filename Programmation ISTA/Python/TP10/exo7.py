L=[]
def calcul(L):
    som=0
    for i in L:
        som+=i
    return print(f"La somme des valeurs de liste est: {som}")
nbr=int(input("Entez le nombre des valeurs pour votre liste: "))
for j in range(nbr):
    val=float(input(f"Entrez la valeur {j+1}: "))
    L.append(val)
calcul(L)