a=int(input("Entrez un nombre: "))
b=int(input("Entrez un nombre: "))
pgcd=0
x=a
y=b
while a!=0 and b!=0:
    if a>b:
        a=a-b
    else:
        b=b-a
if a==0:
    pgcd=b
elif b==0:
    pgcd=a
print(f"Le PGCD de {x} et {y} est : {pgcd}")