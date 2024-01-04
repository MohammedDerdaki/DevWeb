TXT=input("Entez un text: ")
X=input	("Entez un caractere: ")
L=[]
TXT1=""
for i in TXT:
    if i!=X:
        L.append(i)
TXT1=TXT1.join(L)
print(TXT1)