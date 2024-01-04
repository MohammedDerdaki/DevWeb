class Stagiaire:

    def Afficher(self):
        print(f"Le Prenom: {self.Prenom}\nLe Nom: {self.Nom}\nNumero d'inscription: {self.NumInscri}\nLes notes sont: {self.Note1, self.Note2, self.Note3} ")
        

#     def __init__(self):
#         self.Notes1=0
#         self.Notes2=0
#         self.Notes3=0
    
    # def __init__(self,Prenom,Nom,NumInscri):
    #     self.Prenom=Prenom
    #     self.Nom=Nom
    #     self.NumInscri=NumInscri
    #     self.Note1=int()
    #     self.Note2=int()
    #     self.Note3=int()
        
    # def __init__(self,Prenom,Nom,NumInscri,Notes1,Notes2,Notes3):
    #     self.Prenom=Prenom
    #     self.Nom=Nom
    #     self.NumInscri=NumInscri
    #     self.Note1=Notes1
    #     self.Note2=Notes2
    #     self.Note3=Notes3
# stg1=Stagiaire(1,"derdaki","mohammed") #method1
# print(f"{stg1.Notes1}\n{stg1.Notes2}\n{stg1.Notes3}")

    def __init__(self,Prenom=str(),Nom=str(),NumInscri=int(),Notes1=int(),Notes2=int(),Notes3=int()):
        self.Prenom=Prenom
        self.Nom=Nom
        self.NumInscri=NumInscri
        self.Note1=Notes1
        self.Note2=Notes2
        self.Note3=Notes3
# stg1=Stagiaire(input("Entrez prenom:"),input("Entrez nom:"),int(input("Entrez Num:")),int(input("Entrez Note1:")), int(input("entrez note2:")), int(input("entrez note3: ")))
stg1=Stagiaire()
stg1.Afficher()