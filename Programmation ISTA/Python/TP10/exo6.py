L=[0,2,3,0,0]
K=[0,0,0,0,0]
def nulle(L):
    j=0
    k=""
    for i in L:
        if i!=0:
            j+=1
        k=f"Le nombre de valeur non nul dans la liste est {j}"
    if j==0:
        k="La liste est nulle"
    return k
print(nulle(L))