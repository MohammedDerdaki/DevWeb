M=[[-5,15,12,0,48],[-45,12,100,-1.5,33],[154,20,4,3,5],[15,13,-5,14,0],[-1,12,-12,-13,-50]]
som=0
for i in range(len(M)):
    som+=M[(len(M)-1)-i][i]
print(som) 