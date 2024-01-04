ch=input("Entrez un text:   ")
j=0
ch2=""

for i in ch:
    ch1=ch.upper()
    
    x=0
    if i==ch1[j]:
        x=i.lower()
        ch2=ch2+x
    else:
        x=i.upper()
        ch2=ch2+x
    j+=1
print(ch2)
