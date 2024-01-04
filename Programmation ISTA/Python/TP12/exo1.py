
MesStagiaires=[]
def AjouterStagiaire():
    Stag={"N° d'inscrit":int(),"Nom":"", "Prenom":"","Moyenne":float()}
    moyenne=0
    j=0
    while j!=1:
        NumInscrit=0
        if MesStagiaires==[]:
            NumInscrit=int(input("Veuillez saisir Numero d'inscription de stagiaire: "))
            Stag["N° d'inscrit"]=NumInscrit
            j=1
        else:
           k=0
           while k!=1: 
                NumInscrit=int(input("Veuillez saisir Numero d'inscription de stagiaire: "))
                for i in range(len(MesStagiaires)):
                    
                        if (NumInscrit==MesStagiaires[i]["N° d'inscrit"]):
                            print(f"le Numero d'inscrit {NumInscrit} déjà reservé")
                        else:
                            Stag["N° d'inscrit"]=NumInscrit
                            j=1
                            k=1

    Nom=input("Veuillez saisir Nom de stagiaire: ")
    Stag["Nom"]=Nom
    Prenom=input("Veuillez saisir Prenom de stagiaire: ")
    Stag["Prenom"]=Prenom
    NbrNote=int(input("Pour calculez la moyenne, veuillez saisir nombre des notes: "))
    for i in range(NbrNote):
        note=float(input(f"Entrez la note {i+1}: "))
        moyenne+=note
    moyenne=moyenne/NbrNote
    Stag["Moyenne"]=moyenne
    MesStagiaires.append(Stag)

    return Stag
    

def AfficherListe():
    print("** La list des stagiaires : **")
    for i in range(len(MesStagiaires)):
        print(f"Stagiaire {i+1} : {MesStagiaires[i]}")
    return

def ChercherNum():
    Num=int(input("Veuillez saisir le numero de stagiaire: "))
    for i in range(len(MesStagiaires)):
        if Num==MesStagiaires[i]["N° d'inscrit"]:
            print(MesStagiaires[i])
            return
    
def ChercherNP():
    j=0
    while j!=1:
        Nom=input("Veuillez saisir le Nom de stagiaire: ")
        Prenom=input("Veuillez saisir le Prenom de stagiaire: ")
        for i in range(len(MesStagiaires)):
            if Nom==MesStagiaires[i]["Nom"] and Prenom==MesStagiaires[i]["Prenom"]:
                print(f"\n** Voila les information de stagiaire {Nom} {Prenom}: de N° d'inscrit ", MesStagiaires[i]["N° d'inscrit"]," **")
                print(MesStagiaires[i])
                j=1
            else:
                print(f"\n **Erreur**")
def Supprimer():
    j=0
    while j!=1:
        Num=int(input("Veuillez saisir le numero de stagiaire: "))
        if MesStagiaires==[]:
                print("List est vide")
                break
        else:
            for i in range(len(MesStagiaires)):
                if Num==MesStagiaires[i]["N° d'inscrit"]:
                    print("Les informations de stagiaire:\n", MesStagiaires[i]["Nom"], MesStagiaires[i]["Prenom"], "a été supprimer ")
                    del MesStagiaires[i]
                    j=1
                else:
                    print("Le N° d'inscrit uncorrect:")
    return
choix=1
while choix>=1 and choix<=6:
    choix=int(input(f"\n ------------------------------------ \n ** Veuillez choisir un nombre: ** \n 1- Pour Ajouter un stagiaire \n 2- Pour Afficher la liste \n 3- Chercher par Num \n 4- Chercher par Nom&Prenom \n 5- Pour supprimer un stagiaire \n 6- Pour exit le programme \n ==>"))
    option=1
    match (choix):
        case 1: 
                while option==1 or option==2:
                    match option:
                        case 1: AjouterStagiaire()
                        case 2:break
                    option=int(input(f"\n ------------------------------------ \n Veuillez choisir : \n 1- Pour Ajouter autre Stagiaire \n 2- Pour retourner a menu \n ==>"))
        case 2: AfficherListe()    
        case 3: ChercherNum()
        case 4: ChercherNP()
        case 5: Supprimer()
        case 6: exit()