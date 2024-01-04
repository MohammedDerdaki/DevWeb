nbrStg=int(input("Veuillez saisir le nombre de stgaiaires: "))
File=open("./TP13/notes1.txt","w")
File.write("** La liste de moyenne des stagiaires **\n")
som=0
note=0
for i in range(nbrStg):
    note=float(input(f"Entrez la moyenne de stagiaire {i+1}: "))
    File.write(f"{str(note)} \n")
    som+=note
File.write(str(round((som/nbrStg),2)))