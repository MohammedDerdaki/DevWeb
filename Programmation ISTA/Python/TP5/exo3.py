L=[]
Nbr=int(input("Entrez le nombre de saisi:"))
for i in range(Nbr):
    note=int(input(f"Entrez la nombre {i+1}: "))
    L.append(note)
Mini=L[0]
Maxi=L[0]
for j in L:
    if j<Mini:
        Mini=j
    if j>Maxi:
        Maxi=j
print(f"la minimale: {Mini} et Le maximale: {Maxi}")