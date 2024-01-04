M=[[-5,15,12,0,48],[-45,12,100,-1.5,33],[154,20,4,3,5]]
LPos=[]
LNeg=[]

Som=0
NbrPos=0
SomPos=0
NbrNeg=0
SomNeg=0

for i in range(len(M)):
    for j in M[i]:
        Som=Som+j
        if j>=0:
            NbrPos+=1
            SomPos+=j
            LPos.append(j)
        else:
            NbrNeg+=1
            SomNeg+=j
            LNeg.append(j)
print(f"La somme des valeurs de la liste est :{Som}")
print(f"Le nombre des éléments positifs est :{NbrPos} .")
print(f"les valeurs positifs sont: {LPos}")
print(f"La somme des éléments positifs sont: {SomPos}")
print(f"et La somme des éléments négatifs sont: {SomNeg}")
print(f"Les valeurs negatifs sont: {LNeg}")
