Ch=input("Entrez un text: ")
newCh=""

#method1:
for i in Ch:
    if 'e'!=i:
        newCh=newCh+i
print(newCh)
#method2
L=[]
newCh=""
for i in Ch:
    if 'e'!=i:
        L.append(i)
newCh=newCh.join(L)
print(newCh)