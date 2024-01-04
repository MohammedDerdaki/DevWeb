N=int(input("Veuillez saisir un nombre:"))
X=1
Y=1
U=0
if N>2:
    for i in range(3,N+1):
        U=X+Y
        Y=X
        X=U
    
print(U)