# def factoriel(nbr):
#     x=nbr
#     for i in range(1,nbr):
#         x=x*i
#     return x
# nbr=int(input("Entrez un nombre pour calculez la factoriel: "))
# print(factoriel(nbr))
nbr=int(input("Entrez un nombre pour calculez la factoriel: "))


def factoriel():
    global nbr
    x=nbr
    for i in range(1,nbr):
        x=x*i
    nbr=x
    print(nbr)

factoriel()




