L1=[]
L2=[]
Nbr1=int(input("Entrez le nombre de liste 1:"))
Nbr2=int(input("Entrez le nombre de liste 2:"))
som=0
for i in range(Nbr1):
    N=int(input(f"Entrez le nombre {i+1} de liste 1: "))
    L1.append(N)

for j in range(Nbr2):
    N=int(input(f"Entrez le nombre {j+1} de liste 2: "))
    L2.append(N)

# for i in L1:
#     for j in L2:
#         print(f"{i}*{j}", end="+")
#         som=som+i*j
# print("=",som)

for i in range(len(L1)):
    for j in range(len(L2)):
        if(i==len(L1)-1  and j==len(L2)-1):
            print(f"{L1[i]}*{L2[j]}", end=" ")
        else :
             print(f"{L1[i]}*{L2[j]}", end="+")
        som=som+L1[i]*L2[j]
print("=",som)

