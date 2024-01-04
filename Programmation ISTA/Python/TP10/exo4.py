def supprimerCaractere(c):
    global ch
    NewCh=""
    C=(c.upper())
    for i in ch:
        if (i!=c) and (i!=C):

            NewCh=NewCh+i
    return NewCh

ch=input("Entrez une phrase: ")
c=input("Entrez un caractere: ")
print(supprimerCaractere(c))