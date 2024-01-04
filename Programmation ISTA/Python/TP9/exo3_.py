L=[-45,12,100,-1.5,33]
def Max():
    L.sort()
    x=L[len(L)-1]
    return x

# nbr=int(input("Entrez la nombre des valeurs: "))
# #remplir la liste L:
# for j in range(nbr):
#         z=int(input(f"Entrez la valeur {j+1}: "))
#         L.append(z)
# if nbr%2!=0:
#     nbr_=int(input("Entrez une autre valeur : "))
#     L.append(nbr_)
# for i in range(0,len(L),2):
#      d=Max(L)
 

print(Max())