File=open("./TP13/notes1.txt","r")
nbrStg=File.readlines()
File.close()
File=open("./TP13/notes1.txt","r")

for i in range(len(nbrStg)):
    if i==0:
        print(File.readline())
    elif i==(len(nbrStg)-1):
        print(f"Moyenne  de classe : {File.readline()}")
    else:
        print(f"Moyenne du stagiaire {i} : {File.readline()}")
