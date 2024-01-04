L=[]
def change(x,y):
    x=y-x
    y=y-x
    x=x+y
    L.append(x)
    L.append(y)


def paires(x,y):
    
    if x>y:
        change(x,y)
    else:
        L.append(x)
        L.append(y)
        
    for i in range(L[0],L[1]):
        if (i%2==0) and x!=i:
            print(i, end=" ")

a=int(input("entrez premier nombre: "))
b=int(input("entrez deuxieme nombre: "))
paires(a,b)