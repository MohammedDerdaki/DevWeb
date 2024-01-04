L=[-12,10,100,0,-20,12.5,-1.9]

for i in range(len(L)):
    for j in range((i+1),len(L)):
        if L[i]>L[j]:
            x=L[i]
            L[i]=L[j]
            L[j]=x



for i in range(len(L)):
    mini=L[i]
    p=i
    for j in range((i+1),len(L)):
        if mini>L[j]:
            mini=L[j]
            p=j
    x=L[i]
    L[i]=mini
    L[p]=x
            


print(L)
VAL=int(input("entrez un nombre: "))
# L.append(VAL)
# for i in range(len(L)):
#     for j in range((i+1),len(L)):
#         if L[i]>L[j]:
#             x=L[i]
#             L[i]=L[j]
#             L[j]=x
# print(L)

Trouve=False
for i in range(len(L)):
    if L[i]>VAL:
        L.insert(i,VAL)
        break
if (Trouve==False):
    L.append(VAL)
print(L)