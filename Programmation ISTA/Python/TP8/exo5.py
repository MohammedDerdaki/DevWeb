stagiaire={}
stagiaire["Nom"]=input("Entrez un nom: ")
stagiaire["Prenom"]=input("Entez le prenom: ")
S=0
stagiaire["Notes"]=[]
for i in range(3):
    Nbr=float(input(f"Entrez la note {i+1}: "))
    stagiaire["Notes"].append(Nbr)
    S+=Nbr
stagiaire["Moyenne"]=(S/3)
print(stagiaire)