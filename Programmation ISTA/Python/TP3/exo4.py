N = int(input("Veuillez saisir un nombre:"))
Som=0
for i in range(1,N):
    if N%i==0:
        Som=Som+i
if Som==N:
    print(f"Le nombre {N} est parfait")
else:
    print(f"Le nombre {N} n'est pas parfait")