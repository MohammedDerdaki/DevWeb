def sommeN(n):
    L=[]    
    y=0
    for i in range(1,n):
        y=y+(i**2)
    return y
n=int(input("entrez la nombre :"))
print(sommeN(n))