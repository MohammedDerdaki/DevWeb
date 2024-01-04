class Stagiaire:
 

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

    def CalculMoyenne2(self,x,y,z):
        print(f"La moyenne de {self.Nom} est {(x+y+z)/3}")

    # def CalculMoyenne3(self,x=self.Notes[0],y=self.Notes[1],z=self.Notes[2]):
    #     print(f"La moyenne de {self.Nom} est {(x+y+z)/3}")



stg1=Stagiaire()

#definit de stg1
stg1.Nom="Salmi"
stg1.Prenom="Karim"
stg1.NumInscri=1000
stg1.Notes=[14.5,12,13.5]



#definit de stg2
# nom=input("entrez un nom: ")
# numInscrit=input("entrez N° inscrit: ")
# LNotes=[]
# for i in range(3):
#     note=float(input(f"entrez la note {i+1}"))
#     LNotes.append(note)

# stg2=Stagiaire()
# stg2.Nom=nom
# stg2.NumInscri=numInscrit
# stg2.Notes=LNotes

# print(f"Le Nom: {stg1.Nom}\nNumero d'inscription {stg1.NumInscri}\n")
# print(f"Le Nom: {stg2.Nom}\nNumero d'inscription {stg2.NumInscri}\n")

# stg1.Afficher()
# # stg2.Afficher()

# stg1.CalculMoyenne()
# stg1.Mention()

stg1.Infos()
print(stg1.CalculMoyenne())

# stg2.CalculMoyenne()
print(stg1.Mention())
stg1.CalculMoyenne3()