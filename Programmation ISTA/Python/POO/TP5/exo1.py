class CompteBancaire:


    def __init__(self,NumCpt,Nom,Solde=float()):
        self.__numeroCompte=NumCpt
        self.__nom=Nom
        self.__solde=Solde
    
    #Getters
    def GetNumCpt(self):
        return self.__numeroCompte
    def GetNum(self):
        return self.__nom
    def GetSolde(self):
        return self.__solde
    
    #Setters
    def SetNumCpt(self,M):
        self.GetNumCpt=M
    def SetNom(self,M):
        self.GetNum=M
    def SetSolde(self,M):
        self.GetSolde=M


    def Virement(self,Vir):
        # Vir=int(input("Votre virment: ")) #utilisez on match
        if self.GetSolde>=0:
            self.__solde+=Vir
        else:
            self.SetSolde+=Vir
            self.Agios()

        
    def Agios(self):
        self.SetSolde-=(self.SetSolde*0.05)    
        

    def Retrait(self,Rtr):
        # Rtr=int(input("Votre Retrait: ")) # utiliez on match
        if Rtr>self.GetSolde:
            print("Erreur!!, Votre solde actuel est inférieur au montant à retirer")
            
        
        self.SetSolde-=Rtr
    
    def Afficher(self):
        char=22
        print(f'+ {"-"*39} +')
        print("|        RELEVE DE COMPTE BANCAIRE        |") #29Char
        print(f'+ {"-"*39} +')
        print("|            AGENCE OFPPT DD              |") #29Char
        print(f'+ {"-"*39} +')
        
        print(f"| Numero de Compte |{NmCptX}|")

        print(f"| Nom {' '*13}|{NomX}|")
        print(f"| Solde {' '*11}|{SoldeX}|")
        print(f'+ {"-"*39} +')
