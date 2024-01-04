N = int(input("Veuillez saisir un nombre:"))
X =True
for i in range(2,N):
    if (N%i==0):
        print("ce n'est pas nombre premier")
        X=False
        break
if X==True:
    print("nombre premier")
