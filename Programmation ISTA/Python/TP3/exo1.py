N=int(input("Veuillez saisir un nombre:"))
SomD=0
SomM=1
for i in range(1,N+1):
    SomD=SomD+(1/i)
    SomM=SomM*(1/i)
print("La somme est:",round(SomD,4))
print("La produit est:",round(SomM,4))
