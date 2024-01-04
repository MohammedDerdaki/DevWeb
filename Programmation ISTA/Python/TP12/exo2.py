MesStagiaires=[{"N° d'inscrit": 1, 'Nom': 'derdaki', 'Prenom': 'mohammed', 'Moyenne': 20.0},
{"N° d'inscrit": 2, 'Nom': 'madmad', 'Prenom': 'mohammed', 'Moyenne': 20.0},
{"N° d'inscrit": 3, 'Nom': 'el asri', 'Prenom': 'youssef', 'Moyenne': 20.0},
{"N° d'inscrit": 4, 'Nom': 'Youssefi', 'Prenom': 'Ibrahim', 'Moyenne': 20.0},
{"N° d'inscrit": 5, 'Nom': 'hamid ', 'Prenom': 'bousekou', 'Moyenne': 20.0}]

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

def ChercherNum(N):
    for i in range(len(MesStagiaires)):
        if N==MesStagiaires[i]["N° d'inscrit"]:            
            return print(MesStagiaires[i])
        else: return print("« Ce stagiaire est ne se trouve pas dans la liste »")

def ChercherNP(n,p):
    j=0
    while j!=1:
        
        for i in range(len(MesStagiaires)):
            if n==MesStagiaires[i]["Nom"] and p==MesStagiaires[i]["Prenom"]:
                print(f"\n** Voila les information de stagiaire {n} {p}: de N° d'inscrit ", MesStagiaires[i]["N° d'inscrit"]," **")
                print(MesStagiaires[i])
                j=1
        if j!=1:
                print(f"\n **Erreur** \n « Ce stagiaire est ne se trouve pas dans la liste »")
                break
        break
def Supprimer(N):
    j=0
    while j!=1:
        if MesStagiaires==[]:
                print("List est vide")
                break
        else:
            for i in range(len(MesStagiaires)):
                if N==MesStagiaires[i]["N° d'inscrit"]:
                    print("Les informations de stagiaire:\n", MesStagiaires[i]["Nom"], MesStagiaires[i]["Prenom"], "a été supprimer ")
                    del MesStagiaires[i]
                    j=1
                    break
                else:
                    print("Le N° d'inscrit uncorrect: « Ce stagiaire est ne se trouve pas dans la liste")

def Modifier(N):
    j=0
    while j!=1:
        for i in range(len(MesStagiaires)):
            if N==MesStagiaires[i]["N° d'inscrit"]:
                     
                opt=int(input("choose numero pour modifier :\n 1-N° d'inscrit \n 2-Nom\n 3-Prenom\n 4-Moyennne\n 5-Quitté \n==>  "))

                match opt:
                        case 1: 
                                MesStagiaires[i]["N° d'inscrit"]=int(input("Entrez N° d'inscrit: ")) 
                                break
                        case 2: 
                                MesStagiaires[i]["Nom"]=input("Entrez nom: ")
                                break
                        case 3: 
                                MesStagiaires[i]["Prenom"]=input("Entrez prenom: ")
                        case 4: 
                                NbrNote=int(input("Pour calculez la moyenne, veuillez saisir nombre des notes: "))
                                moy=0
                                for i in range(NbrNote):
                                    note=float(input(f"Entrez la note {i+1}: "))
                                    moy+=note
                                    moy=moy/NbrNote
                                MesStagiaires[i]["Moyenne"]=moy
                        case _: j=1
            else:
                print(f"\n **Erreur** \n « Ce stagiaire est ne se trouve pas dans la liste »")
                j=1
                break
choix=1
while choix>=1 and choix<=6:
    choix=int(input(f"\n ------------------------------------ \n ** Veuillez choisir un nombre: ** \n 1- Pour Ajouter un stagiaire \n 2- Pour Afficher la liste \n 3- Chercher par Num \n 4- Chercher par Nom&Prenom \n 5- Pour supprimer un stagiaire \n 6- Pour modifier les informations \n 7- Pour exit le programme \n ==>"))
    option=1
    match (choix):
        case 1: 
                while option==1 or option==2:
                    match option:
                        case 1: AjouterStagiaire()
                        case 2:break
                    option=int(input(f"\n ------------------------------------ \n Veuillez choisir : \n 1- Pour Ajouter autre Stagiaire \n 2- Pour retourner a menu \n ==>"))
        case 2: AfficherListe()    
        case 3: 
                N=int(input("Entrez N° d'inscrit de stagiaire: "))
                ChercherNum(N)
        case 4: 
                n=input("entrez nom de stagiaire: ")
                p=input("entrez prenom de stagiaire: ")
                ChercherNP(n,p)
        case 5: 
                N=int(input("Entrez N° d'inscrit de stagiaire: "))
                Supprimer(N)
        case 6: 
                N=int(input("Entrez N° d'inscrit de stagiaire: "))
                Modifier(N)
        case 7: exit()