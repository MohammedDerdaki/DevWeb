class Salarie:
    cpt=0
    def __init__(self,matricule="",nom=None,prenom=None,salaire=None,TauxCS=None):
        Salarie.cpt+=1
        self.matricule="SAL"+str(Salarie.cpt)
        self.nom=nom
        self.prenom=prenom
        self.salaire=salaire
        self.TauxCS=TauxCS #TCS= Taux Charges Sociales

    @classmethod
    def GETNOMBRE(cls):
        return Salarie.cpt
    def CalculerSalaireNet(self,Salaire,TauxCS):
        Salaire=Salaire-(Salaire*TauxCS)
        return Salaire
    
    # def tostring(self):
    #     print(f"Matricule:{self.matricule}\nNom:{self.nom}\nPrenom:{self.prenom}\nSalaire:{self.salaire}\nTaux de Charge sociale:{self.TauxCS}")

    def copier(self,y):
        self.matricule=y.matricule
        self.nom=y.nom
        self.prenom=y.prenom
        self.salaire=y.salaire
        self.TauxCS=y.TauxCS
    def __del__(self):
        Salarie.cpt-=1

    def __str__(self):
        #  return ("Matricule:"+str(self.matricule)+"Nom:"+str(self.nom)+"Prenom"+str(self.prenom)+"Salaire:"+str(self.salaire)+"Taux de Charge Sociale:"+str(self.TauxCS))
    
        return f"\nMatricule : {self.matricule};\nNom: {self.nom};\nPrenom: {self.prenom};\nSalaire: {self.salaire};\nTaux de charge sociale: {self.TauxCS};"
    
    def equals(self,a):
        if self.matricule==a.matricule:
            return True
        else:
            return False
        
S1=Salarie(matricule=101,nom="derdaki",prenom="mohammed",salaire=10000,TauxCS=0.3)

S2=Salarie(nom="MadMad",prenom="Med",salaire=50000,TauxCS=0.3)

print(S2.matricule)

print(Salarie.GETNOMBRE())

print(S1)

print(S1.equals(S2))