TXT=input("Entrez un text: ")
c=""
TXT1=""
for i in TXT:
    if i!=c:
        TXT1=TXT1+i
    c=i    
print(TXT1)