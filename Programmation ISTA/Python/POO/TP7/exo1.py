import datetime as dt

class Stagiaire:
    #Attribut de class
    cpt=0
    #constructeur
    def __init__(self,stgInscri=int(),stgNom=str(),stgPrenom=str(),DTN=tuple(),stgNt1=int(),stgNt2=int(),stgNt3=int()):
        Stagiaire.cpt+=1
        
        self.__NumInscri=stgInscri
        self.__Nom=stgNom
        self.__Prenom=stgPrenom
        self.__DTNaissance=DTN
        self.__note1=stgNt1
        self.__note2=stgNt2
        self.__note3=stgNt3
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
    def GetDTNaissance(self):
        return self.__DTNaissance
    def GetNote1(self):
        return self.__note1
    def GetNote2(self):
        return self.__note2
    def GetNote3(self):
        return self.__note3
    # Setters ===========>
    def SetNumInscri(self,M_num):
        j=1
        while j!=0:
            if M_num>=0:
                self.__NumInscri=M_num
                j=0
            else:
                M_num=int(input("Erreur,Entrez une valeur positive: "))
    def SetNom(self,M):
        self.__Nom=M
    def SetPrenom(self,M):
        self.__Prenom=M
    def SetDTNaissance(self,m):
        self.__DTNaissance=m
    def SetNote1(self,M):
        j=1
        while j!=0:
            if M>=0:
                self.__note1=M
                j=0
            else:
                M=int(input("Erreur,Entrez une valeur positive: "))    
    def SetNote2(self,M):
        j=1
        while j!=0:
            if M>=0:
                self.__note2=M
                j=0
            else:
                M=int(input("Erreur,Entrez une valeur positive: ")) 
    def SetNote3(self,M):
        j=1
        while j!=0:
            if M>=0:
                self.__note3=M
                j=0
            else:
                M=int(input("Erreur,Entrez une valeur positive: ")) 

    #method de class
    @classmethod
    def GetNBInstances(cls):
        return "Le nombre d'instances crée est :"+str(Stagiaire.cpt)
    #Property
    NumeroInscription=property(GetNumInscri,SetNumInscri)
    Nom=property(GetNom,SetNom)
    Prenom=property(GetPrenom,SetPrenom)
    Note1=property(GetNote1,SetNote1)
    Note2=property(GetNote2,SetNote2)
    Note3=property(GetNote3,SetNote3)
   
    def  CalculMoyenne(self):
        Moy=0
        Moy=(self.Note1+self.Note2+self.Note3)/3
        return round(Moy,2)
    
    def Mention(self):
        Moy=self.CalculMoyenne()
        if Moy<10: x="redoubler"
        elif Moy>=10 and Moy<12: x="passable"
        elif Moy>=12 and Moy<14: x="assez bien"
        else: x="bien"
        return x

    def Infos(self):
        print("*"*10,"stagiaire",Stagiaire.cpt,"*"*10,f"\nLe Numero d'inscription: {self.NumeroInscription}\nNom: {self.Nom}\nPrenom: {self.Prenom}\nDate de Naissance:{self.GetDTNaissance()[0]}/{self.GetDTNaissance()[1]}/{self.GetDTNaissance()[2]}\nsa moyenne: {self.CalculMoyenne()}\nsa mention: {self.Mention()}\n","*"*30)
    
    def Age(self):
        age=(dt.date.today().year)-self.GetDTNaissance()[0]  
        return age
    

# stg=Stagiaire(int(input("Entrez le numero d'inscription: ")),input("Entre votre Nom: "),input("Entre votre Prenom: "),int(input("Entrez la note1: ")),int(input("Entrez la note2: ")),int(input("Entrez la note3: ")))
stg=Stagiaire(100,'dd','pp',(1998,6,8),20,20,20)
# stg.NumeroInscription=int(input("Entrez le numero d'inscription: "))
# print(stg.NumeroInscription)
# stg.Nom=input("Entre votre Nom: ")
# print(stg.Nom)
# stg.Prenom=input("Entre votre prenom: ")
# print(stg.Prenom)
# stg.Note1=int(input("Entrez la note1: "))
# print(stg.Note1)
# stg.Note2=int(input("Entrez la note2: "))
# print(stg.Note2)
# stg.Note3=int(input("Entrez la note3: "))
# print(stg.Note3)


stg.Infos()
print(stg.Age())