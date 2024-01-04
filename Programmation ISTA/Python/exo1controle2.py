ch=input("Saisir une chaine")
ch=ch.lower()
v="aeiuoy"
l=[]
c=0
#methode 1
# for i in range(len(ch)):
#     if ch[i] in v :
#         c+=1
#         l.append(i)

#methode 
# for i in range(len(ch)):
#     for j in range(len(v)):
#         if ch[i]==v[j]:
#             c+=1
#             l.append(i)

#methode 3

for i in range(len(ch)):
    if ch[i]=='a' or ch[i]=="e" or ch[i]=="i" or ch[i]=="o" or ch[i]=="u" or ch[i]=='y' :
        c+=1
        l.append(i)


print("le nombre de voyelle " ,c)
print("les positiosn sont : ")
for a in l :
    print(a)    



