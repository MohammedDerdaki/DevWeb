File=open("./TP13/personne.txt", "a")
personne={"CIN":str(), "Nom":str(), "Prenom":str()}
def Saisir():
    global personne
    personne["CIN"]=input("Veuillez saisir votre CIN: ")
    personne["Nom"]=input("Veuillez saisir votre Nom: ")
    personne["Prenom"]=input("Veuillez saisir votre Prenom: ")

File.close()   

def Enregistrer():
    global personne
    File=open("./TP13/personne.txt", "a")
    Saisir()
    File.write(f"{personne['CIN']}\t{personne['Nom']}\t{personne['Prenom']}\n")
    File.close()

def  Lister():
    File=open("./TP13/personne.txt", "r")
    print(File.read())
    File.close()

def Chercher(cin):
    File=open("./TP13/personne.txt", "r")
    L=File.readlines()
    for x in L:
        T=x.split("\t")
        if T[0]==cin:
            print(f"CIN: {T[0]}\nNom: {T[1]}\nPrenom: {T[2]}")
    File.close()

def Supprimer(cin): #continue
    File=open("./TP13/personne.txt", "r")
    listePersonne=File.readlines()
    File.close()
    for i in range(len(listePersonne)):
        T=listePersonne[i].split("\t")
            # supprimer
        if cin==T[0]:
            print(f"CIN: {T[0]}\nNom: {T[1]}\nPrenom: {T[2]}\n==> est bien supprimer")
            print(i)
            print(listePersonne)
            del listePersonne[i]
            
        else:
            print("CIN n'exsiste pas")
            

    File.close()

def Modifier(cin): #continue
    return

# Le menu pour l'utilisateur 
j=0
while j!=1:
    option=int(input("Choose:\n 1 pour Enregistrer\n 2 pour lister\n 3 pour chercher\n 4 pour supprimer\n 5 pour modifier\n 6 pour sortir\n==>"))
    match option:
        case 1: Enregistrer()
        case 2: Lister()
        case 3: 
            cin=input("Veuillez entrez le CIN: ")
            Chercher(cin)
        case 4: 
            cin=input("Veuillez saisir le CIN: ")
            Supprimer(cin)
        case 5:
            cin=input("Veuillez saisir le CIN: ")
            Modifier(cin)
        case _: exit()
