class Stagiaire:
    def Afficher(self):
        print(f"Le Nom: {self.Nom}\nNumero d'inscription {self.NumInscri}\n")
stg1=Stagiaire()

#definit de stg1
stg1.Nom="Salmi Karim"
stg1.NumInscri=1000
stg1.Notes=[14.5,12,13.5]




nom=input("entrez un nom: ")
numInscrit=input("entrez N° inscrit: ")
LNotes=[]
nbrNotes=int(input("entrez les nombres des notes: "))
for i in range(nbrNotes):
    note=float(input(f"entrez la note {i+1}"))
    LNotes.append(note)

stg2=Stagiaire()
stg2.Nom=nom
stg2.NumInscri=numInscrit
stg2.Notes=LNotes

# print(f"Le Nom: {stg1.Nom}\nNumero d'inscription {stg1.NumInscri}\n")
# print(f"Le Nom: {stg2.Nom}\nNumero d'inscription {stg2.NumInscri}\n")

stg1.Afficher()
stg2.Afficher()
