import datetime as dt
class Chauffeur:
    
    #constructeur 
    def __init__(self,CIN,Nom,Prenom):
        self.__cin=CIN
        self.__nom=Nom
        self.__prenom=Prenom

    #getters
    def GetCIN(self):
        return self.__cin
    def GetNom(self):
        return self.__nom
    def GetPrenom(self):
        return self.__prenom
    
    #__str__
    def __str__(self):
        return f"CIN:{self.GetCIN()}\tNom:{self.GetNom()}\tPrenom:{self.GetPrenom()}"
    
class Bus:

    #contructeur
    def __init__(self,Imm,mrq,typ):
        self.__immatriculation=Imm
        self.__marque=mrq
        self.__type=typ

    #Getters Accesseurs:
    def GetImm(self):
        return self.__immatriculation
    def getMrq(self):
        return self.__marque
    def GetType(self):
        return self.__type
    
    #__str__()
    def __str__(self):
        return f"Immatriculation:{self.GetImm()}\tMarque:{self.getMrq()}\tType:{self.GetType()}"
    
class Voyage:
    __cpt=0
    __prix=70
    #constructeur
    def __init__(self,VilleD,VilleA,nbrvyg=int(),prix=float(),Ch=None,Bs=None):
        Voyage.__cpt+=1
        self.NumVoy=Voyage.__cpt
        if isinstance(Ch,Chauffeur):
            self.Vchauffeur=Ch
        
        if isinstance(Bs,Bus):
            self.Vbus=Bs

        self.DD=dt.datetime.today() #date de départ
        self.VD=VilleD #VD= Ville de Départ
        self.VA=VilleA #VA= Ville d'Arrivée
        self.NbrVygs=nbrvyg
        self.prix=Voyage.__prix

    def __str__(self):
        return f"Le Numero du voyage:{self.NumVoy}\nLa date du voyage:{self.DD}\nLe nom:{self.Vchauffeur.GetNom()}\nLe prénom:{self.Vchauffeur.GetPrenom()}\nL'immatriculation du bus:{self.Vbus.GetImm()}\nLa marque:{self.Vbus.getMrq()}\nVille de départ:{self.VD}\nVille d'arrivée:{self.VA}\nRecette du voyage:{float((self.NbrVygs)*(Voyage.__prix))}"


#===========================Programme =========================#
# ch1=Chauffeur(input("Entrez CIN: "),input("Entrez nom: "),input("Entez prenom: "))
ch1=Chauffeur("fj25868","derdaki","mohammed")
# B1=Bus(input("Entrez immatriculation: "),input("Entrez marque: "),input("Entrez type: "))
B1=Bus("MR100120","Mercedes-benz","G-class")
# v1=Voyage(input("villeD: "),input("villeA: "),int(input("nbr: ")),float(input("prix: ")),ch1,B1)
v1=Voyage("oujda","rabat",70,115,ch1,B1)
print(v1)