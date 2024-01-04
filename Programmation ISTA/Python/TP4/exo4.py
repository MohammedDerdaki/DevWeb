L=[]
plsGrd=0
P=0
for i in range(5):
    Nbr=float(input(f"Entrez le nombre numéro {i+1}"))
    L.append(Nbr)
plsGrd=L[0]
for i in range(len(L)):
    if L[i]>plsGrd:
        plsGrd=L[i]
        P=i+1
print(f"le plus grand de ces nombres est: {plsGrd} et sa position est {P}")