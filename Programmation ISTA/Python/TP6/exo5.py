A=[]
Lg=int(input("Entrez la nombre des lignes: "))
Cl=int(input("Entrez le nombre des colonnes: "))
for i in range(Lg):
    Ligne=[]
    for j in range(Cl):
        nbr=int(input(f"Entrez la valeur de ligne {i+1} et colonne {j+1}: "))
        Ligne.append(nbr)
        print(Ligne)
    A.append(Ligne)
print(A)
B=[]
for i in range(Cl):
    Ligne=[]
    for j in range(Lg):
        Ligne.append(A[j][i])
    B.append(Ligne)
print(B)