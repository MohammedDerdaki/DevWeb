N = int(input("Veuillez saisir un nombre:"))
c=0
for i in range (1,N+1):
    if N%i==0:
        c+=1
if c==2:
    print("nombre premier")
else:
    print("ce n'est pas nombre premier")