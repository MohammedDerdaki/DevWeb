l1=[]
l2=[]
l3=[]

for i in range(10):
    x=int(input(f"saisir le nombre {i+1}"))
    l1.append(x)

l2.append(l1[0])

for i in range(1,len(l1)) :
    if l1[i]!=l1[i-1] :
        l2.append(l1[i])
    else:
        l3.append(i)

print(l2)
print("les positions :")
print(l3)
