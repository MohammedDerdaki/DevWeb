class Stagiaire:
    #Attribut de class
    cpt=0
    # stgNom=str()
    # stgPrenom=str()
    # stgInscri=int()
    # stgNt1=int()
    # stgNt2=int()
    #constructeur
    def __init__(self,stgNom=input("Entrez Nom:"),stgPrenom=input("Entrez Prenom:"),stgInscri=input("Entrez Num d'inscrit:"),stgNt1=int(input("Entrez note1:")),stgNt2=int(input("Entrez note2:"))):
        Stagiaire.cpt+=1
        
        self.Nom=stgNom
        self.Prenom=stgPrenom
        self.NumInscri=stgInscri
        self.note1=stgNt1
        self.note2=stgNt2
    #desconstructeur

    def __del__(self):
        Stagiaire.cpt-=1

    
    #method de class
    @classmethod
    def GetNBInstances(cls):
        return "Le nombre d'instances crée est :"+str(Stagiaire.cpt)
    
    def Afficher(self):
        print(f"Le Nom: {self.Nom}\nNumero d'inscription {self.NumInscri}\nLes notes sont: {(self.Notes[0], self.Notes[1])} ")
        
    def  CalculMoyenne(self):
        Moy=0
        Moy=(self.note1+self.note2)/2
        return round(Moy,2)
    
    def Mention(self):
        Moy=self.CalculMoyenne()
        if Moy<10: x="redoubler"
        elif Moy>=10 and Moy<12: x="passable"
        elif Moy>=12 and Moy<14: x="assez bien"
        else: x="bien"
        return x

    def Infos(self):
        print(f"Le Numero d'inscription: {self.NumInscri}\nNom: {self.Nom}\nPrenom: {self.Prenom}\nsa moyenne: {self.CalculMoyenne()}\nsa mention: {self.Mention()}")

    

stg1=Stagiaire()
stg1.Infos()
# #definit de stg1
# stg1.Nom="Salmi"
# stg1.Prenom="Karim"
# stg1.NumInscri=1000
# stg1.Notes=[14.5,12,13.5]


stg2=Stagiaire()
stg2.Infos()

#definit de stg1
# stg2.Nom="Salmi"
# stg2.Prenom="Karim"
# stg2.NumInscri=1000
# stg2.Notes=[14.5,12,13.5]


# dic={}
# GetMatricule=0
# dic=15
# print(type(stg1.GetMatricule))

