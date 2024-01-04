Moy = 0
i=0
c=0
for i in range(1,4):
    Note=float(input(f"saisir la note {i}"))
    if Note>=0 and Note<=20:
        Moy=Moy+Note
    else:
        c=c+1

Moy=Moy/(i-c)
if Moy<10:
    x="ajourner"
elif Moy<14:
    x="assez bien"
elif Moy<16:
    x="bien"
else:
    x="trés bien"
print(f"La moyen est: {Moy}, et votre mention est : {x}")