L_stag=[]
nbrStg=int(input("Entrez les nombres des stagiaires: "))
for i in range(nbrStg):
    L_stag.append(f"Stagiaire{i+1}")
    L_stag[i]={}
    L_stag[i]["Nom"]=input("Entrez le nom de stagiaire: ")
    L_stag[i]["Prenom"]=input("Entrez le prenom de stagiaire: ")
    S=0
    L_stag[i]["Note"]=[]
    nbrNote=int(input("Entez le nombre des notes: "))
    for j in range(nbrNote):
        Note=float(input(f"Entrez la note {j+1}: "))
        S+=Note
        L_stag[i]["Note"].append(nbrNote)
    L_stag[i]["Moyenne"]=(S/nbrNote)
print(L_stag)