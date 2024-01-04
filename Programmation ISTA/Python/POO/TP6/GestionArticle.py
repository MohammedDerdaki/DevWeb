class Article:
    __TTVA=20
    __cpt=0
    def __init__(self,nom,prix):
        Article.__cpt+=1
        self.__nom=nom
        self.__reference=Article.__cpt
        self.__prix=prix
        # self.__TTVA=TTVA
    #Getters
    def GetNom(self):
        return self.__nom
    def GetReference(self):
        return self.__reference
    def GetPrix(self):
        return self.__prix
    # def GetTTVA(self):
    #     self.__TTVA
    
    # #setters
    # def SetNom(self,m):
    #     self.__nom=m
    # def Setreference(self,m):
    #     self.__reference=m
    # def SetPrix(self,m):
    #     self.__prix=m
    # def SetTTVA(self,m):
    #     self.__TTVA=m
    
    #Calcul TTC  
    def CalculerPrixTTC(self):
        TTC=(self.GetPrix()+(self.GetPrix()*(Article.__TTVA*100)))
        return TTC
    #Afficher method
    def Afficher(self):
        print(f"Reference:{self.GetReference()}\nNom:{self.GetNom()}\nPrix:{self.CalculerPrixTTC()}")
    
    #__str__
    def __str__(self):
        return (f"Reference:{self.GetReference()}\nNom:{self.GetNom()}\nPrix:{self.CalculerPrixTTC()}\nTTVA:{Article.__TTVA}")
    
produit=Article(input("Entrez Nom: "),int(input("Entrez Prix: ")))
produit.Afficher()
print(produit)