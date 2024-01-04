class Stagiaire:
    #Attribut de class
    cpt=0

    #constructeur
    def __init__(self,stgInscri=str(),stgNom=str(),stgPrenom=str(),stgNt1=int(),stgNt2=int()):
        Stagiaire.cpt+=1
        
        self.__NumInscri=stgInscri
        self.__Nom=stgNom
        self.__Prenom=stgPrenom
        self.__note1=stgNt1
        self.__note2=stgNt2
    #desconstructeur

    def __del__(self):
        Stagiaire.cpt-=1

    # Getters ===========>
    def GetNumInscri(self):
        return self.__NumInscri
    def GetNom(self):
        return self.__Nom
    def GetPrenom(self):
        return self.__Prenom
    def GetNote1(self):
        return self.__note1
    def GetNote2(self):
        return self.__note2
    # Setters ===========>
    def SetNumInscri(self,M):
        self.__NumInscri=M
    def SetNom(self,M):
        self.__Nom=M
    def SetPrenom(self,M):
        self.__Prenom=M
    def SetNote1(self,M):
        self.__note1=M
    def SetNote2(self,M):
        self.__note2=M

    #method de class
    @classmethod
    def GetNBInstances(cls):
        return "Le nombre d'instances crée est :"+str(Stagiaire.cpt)
    
    def Afficher(self):
        print(f"Le Nom: {self.Nom}\nNumero d'inscription {self.NumInscri}\nLes notes sont: {(self.GetNote1, self.GetNote2)}\n\t")
        
    def  CalculMoyenne(self):
        Moy=0
        Moy=(self.GetNote1()+self.GetNote2())/2
        return round(Moy,2)
    
    def Mention(self):
        Moy=self.CalculMoyenne()
        if Moy<10: x="redoubler"
        elif Moy>=10 and Moy<12: x="passable"
        elif Moy>=12 and Moy<14: x="assez bien"
        else: x="bien"
        return x

    def Infos(self):
        print("*"*10,"stagiaire",Stagiaire.cpt,"*"*10,f"\nLe Numero d'inscription: {self.GetNumInscri()}\nNom: {self.GetNom()}\nPrenom: {self.GetPrenom()}\nsa moyenne: {self.CalculMoyenne()}\nsa mention: {self.Mention()}\n\t")

    

stg1=Stagiaire(100,"derdaki","mohammed",20,20)
stg1.Infos()
# #definit de stg1
# stg1.Nom="Salmi"
# stg1.Prenom="Karim"
# stg1.NumInscri=1000
# stg1.Notes=[14.5,12,13.5]
stg1.SetNumInscri(input("Num d'inscrit: "))
stg1.SetNom(input("Nom: "))
stg1.SetPrenom(input("Prenom: "))
stg1.SetNote1(int(input("note1: ")))
stg1.SetNote2(int(input("note2: ")))
stg1.Infos()

stg2=Stagiaire(input("Entrez Num d'inscrit: "),input("Nom: "),input("Prenom: "),int(input("Note1: ")),int(input("Note2: ")))

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

