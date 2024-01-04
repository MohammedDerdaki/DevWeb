MesParticipants=[{"N°": 1, 'birthday': 1998, "score":100, "pays":"Maroc"},{"N°": 2, 'birthday': 1999, "score":100, "pays":"Maroc"},{"N°": 3, 'birthday': 2004, "score":100, "pays":"Maroc"}]
def Ajouter():
    Participant={"N°": int(), "birthday":int(), "score": int(), "pays":""}
    Participant["N°"]=int(input("Entrez N°: "))
    Participant["birthday"]=int(input("Entrez l'anne de naissance: ", {}))
    Participant["score"]=int(input("Entrez score: "))
    Participant["pays"]=input("Entrez pays: ")
    MesParticipants.append(Participant)
    return Participant

def Afficher():
    if MesParticipants==[]:
        print("liste vide")
    else:
        for i in range(len(MesParticipants)):
            print("** La list des stagiaires : **")
            print(MesParticipants[i]["N°"])
            print(2023-MesParticipants[i]["birthday"])
            print(MesParticipants[i]["score"])
            print(MesParticipants[i]["pays"])

def Chercher(n):
    for i in range(len(MesParticipants)):
        if n==MesParticipants[i]["N°"]:
            return MesParticipants[i]
    
def supprimer():
    for i in range(0,len(MesParticipants),-1):
        if (MesParticipants[i]["birthday"]-2023)>25:
            del MesParticipants[i]
    return print("les participant ayant un âge supérieur à 25 ans ont supprimé.")
j=0
while j!=1:
    choix=int(input("\nchoisissez parmi:\n 1 pour Ajouter\n 2 pour Afficher\n 3 pour chercher\n 4 pour supprimer les participant ayant un âge supérieur à 25 ans \n 6 pour quitter\n ==>"))
    match choix:
        case 1: Ajouter()
        case 2: Afficher()
        case 3:
            n=int(input("Entrez le N°: "))
            Chercher(n)
        case 4: supprimer()
        case 6: exit()