TXT=input("Entrez un ligne de text: ")
print(TXT)
L=(len(TXT))
j=0
for i in TXT:
    if 'e'==i:
        j=j+1
print("le nombre de 'e' contenus dans le texte : ",j)        
print("la phrase que on'a : ", TXT)
print("la phrase à l'inverse: ")
for i in range(L-1,-1,-1):
    print(TXT[i], end="")
    
print()
#Tranches:
for i in range(len(TXT)-1,-1,-1):
    print(TXT[len(TXT):-(len(TXT)+1):-1])
