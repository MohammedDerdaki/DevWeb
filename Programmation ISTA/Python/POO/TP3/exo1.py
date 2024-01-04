class Stagiaire:
    #Attribut de class
    cpt=0

    #constructeur
    def __init__(self):
        Stagiaire.cpt+=1

    #desconstructeur

    def __del__(self):
        Stagiaire.cpt-=1

    
    #method de class
    @classmethod
    def GetNBInstances(cls):
        return "Le nombre d'instances crée est :"+str(Stagiaire.cpt)
    
    def Afficher(self):
        print(f"Le Nom: {self.Nom}\nNumero d'inscription {self.NumInscri}\nLes notes sont: {(self.Notes[0], self.Notes[1], self.Notes[2])} ")
        
    def  CalculMoyenne(self):
        Moy=0
        for i in range(len(self.Notes)):
            Moy+=self.Notes[i]
        Moy=Moy/3
        self.Moy=Moy
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

    def CalculMoyenne1(self,x,y,z):
        print(f"La moyenne de {self.Nom} est {(x+y+z)/3}")

stg1=Stagiaire()
#definit de stg1
stg1.Nom="Salmi"
stg1.Prenom="Karim"
stg1.NumInscri=1000
stg1.Notes=[14.5,12,13.5]

stg2=Stagiaire()
#definit de stg1
stg2.Nom="Salmi"
stg2.Prenom="Karim"
stg2.NumInscri=1000
stg2.Notes=[14.5,12,13.5]

# stg3=Stagiaire()
# #definit de stg1
# stg3.Nom="Salmi"
# stg3.Prenom="Karim"
# stg3.NumInscri=1000
# stg3.Notes=[14.5,12,13.5]

print(Stagiaire.GetNBInstances())