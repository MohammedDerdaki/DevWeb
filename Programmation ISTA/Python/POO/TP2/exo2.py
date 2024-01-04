class Salarie:
    def __init__(self,matricule=None,nom=None,prenom=None,salaire=None,TauxCS=None):
        self.matricule=matricule
        self.nom=nom
        self.prenom=prenom
        self.salaire=salaire
        self.TauxCS=TauxCS #TCS= Taux Charges Sociales

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
        print("l'objet a été nettoyé")

    def __str__(self):
        #  return ("Matricule:"+str(self.matricule)+"Nom:"+str(self.nom)+"Prenom"+str(self.prenom)+"Salaire:"+str(self.salaire)+"Taux de Charge Sociale:"+str(self.TauxCS))
    
        return f" str method: \nMatricule : {self.matricule}\nNom: {self.nom}\nPrenom: {self.prenom}\nSalaire: {self.salaire}\nTaux de charge sociale: {self.TauxCS}"
    
    
S1=Salarie(matricule=101,nom="derdaki",prenom="mohammed",salaire=10000,TauxCS=0.3)
# S1.tostring()
print("\n***",S1.CalculerSalaireNet(10000,0.25),"\t***\n")

S2=Salarie()
S2.copier(S1)
# S2.tostring()
print(S1)



