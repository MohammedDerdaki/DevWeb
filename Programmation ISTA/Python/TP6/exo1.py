L_class=[]
Notes=0
MoyCls=0
SomCls=0
for i in range(25):
    j=0
    SomElv=0
    MoyElv=0
    Notes=0
    while Notes!=-1:
        Notes=int(input(f"Entrez la note {j+1} de l'élève {i+1}:"))
        if Notes!=-1:
            SomElv=SomElv+Notes
            j+=1
    MoyElv=SomElv/(j)
    L_class.append(MoyElv)
    SomCls=SomCls+MoyElv
    MoyCls=SomCls/25

for i in range(len(L_class)):
        print(f"la moyen des notes de l'élève {i+1}: {L_class[i]}")
print(f"la moyen de class est {MoyCls}")

