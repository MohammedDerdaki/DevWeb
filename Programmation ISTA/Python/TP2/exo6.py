NomOld=""
NomNew=input("Veuillez saisir le Nom de premeier athléte:")
i=1
while(NomNew!=NomOld):
    NomOld=NomNew
    NomNew=input(f"veuillez saisir le nom de athelete {i}")
    i=i+1
print(i-1)