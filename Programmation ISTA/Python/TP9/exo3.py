def Max(a,b):
    if a>b:
        x=a
    else:
        x=b
    return x

a1=int(input("Entrez un nombre: "))
a2=int(input("Entrez un nombre: "))
a3=int(input("Entrez un nombre: "))
a4=int(input("Entrez un nombre: "))
print("La valeur maximum est: ",Max(Max(a1,a2),Max(a3,a4)))