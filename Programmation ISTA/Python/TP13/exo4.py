File=open("./TP13/personne.txt", "a")

personne={"CIN":str(), "Nom":str(), "Prenom":str()}
def Saisir():
    global personne
    personne["CIN"]=input("Veuillez saisir votre CIN: ")
    personne["Nom"]=input("Veuillez saisir votre Nom: ")
    personne["Prenom"]=input("Veuillez saisir votre Prenom: ")
    
def Enregistrer():
    global personne
    File=open("./TP13/personne.txt", "a")
    Saisir()
    File.write(f"{personne['CIN']}\t{personne['Nom']}\t{personne['Prenom']}")
    File.close()
def  Lister():
    File=open("./TP13/personne.txt", "r")
    print(File.read())
    File.close()

def Chercher(cin):
    File=open("./TP13/personne.txt", "r")
    L=File.readlines(3)
    print(L)
    for x in L:
        T=x.split("\t")
        if T[1]==cin:
            print(f"{T[0]}\t{T[1]}\n{T[2]}")


    
# Le menu pour l'utilisateur 
j=0
while j!=1:
    option=int(input("Choose:\n 1 pour Enregistrer\n 2 pour lister\n 3 pour chercher\n 4 pour sortir\n==>"))
    match option:
        case 1: Enregistrer()
        case 2: Lister()
        case 3: 
            cin=input("Veuillez entrez le CIN: ")
            Chercher(cin)
        case _: exit()
