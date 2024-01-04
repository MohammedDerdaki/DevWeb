nbr=int(input("Entrez un nombre: "))

#method 1:
# x=1
# for i in range(len(nbr)-1):
#     nbr=int(nbr)
#     if nbr>10:
#         x*=10
# nbr=int(nbr)
# y=((nbr/10)-(nbr//10))
# print(f"Le premier chiffre c'est :{(nbr//x)} et le dernier c'est {y*10}")

#method 2:
x=nbr%10
while (nbr>=10):
    nbr=nbr//10
print(f"le premier chiffre c'est :{nbr} et le dernier c'est : {x}")