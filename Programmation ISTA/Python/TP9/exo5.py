def Premier(n):
    j=0
    for i in range(1,n+1):
        if n%i==0:
            j+=1
    if j==2:
        return print("nombre premier")
    else:
        return print("nombre n'est pas premier")
n=int(input("entrez un nombre: "))
Premier(n)