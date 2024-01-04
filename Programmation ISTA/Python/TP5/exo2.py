L_Nbr=[]
TPOS=[]
TNEG=[]
for i in range(5):
    Nbr=int(input(f"Entrez le nombre {i+1}: "))
    L_Nbr.append(Nbr)
for j in L_Nbr:
    if j>=0:
        TPOS.append(j)
    else:
        TNEG.append(j)
print(L_Nbr)
print(TNEG)
print(TPOS)