listch=['B','o','n','j','o','u','r']

ch="Bonjour"  #string
a=len(ch)
print("la longueur ",a)


# les indice commence 0 jusqu' len(ch) -1 
# print(ch[0])
# print(ch[6])
# print(ch[len(ch)-1])

# les indice negatifs

# print(ch[-1])

# print(ch[-len(ch)])  # ch[-7]

# à retenir : ch[0]=ch[-len(ch)]
#             ch[len(ch)-1]= ch[-1]

# ch1=ch[2:5]  
# print(ch1)


# ch1=ch[5:2:-1]  
# print(ch1)

#la concaténation
# ch2=ch+"   "+"les amis"
# print(ch2)

# A=ch.lower()
# print(A)

# print(ch[2].upper())
# c=ch[2].upper()
# print(c)

# c=ch[2].upper()
# print(c)

# ch[2]="F" # affectation d'un caractère=modification d'un caratère
# print(ch)   # ipossible
# listch[2]="F"
# print(listch)

# b= ch.isupper()

# b= ch[0].isupper()
# print(b)

chh="les amis"
# f=chh.capitalize()
# print(f)
# f=chh[0].upper() + chh[1:]
# print(f)

# ch=ch.replace('on','Fi')
# print(ch)

# x=ch.find('n',3,5)
# print(x)

if 'n' in ch:
    print("existe")
else :
    print('n existe pas')
# a='n'

# if a in listch :
#     print("existe")

# a=ch.count('o')
# print(a)
# l=list(ch)
# print(l)
# ch="Bonjour/mes/amis/ "
# t=ch.split("/")
# print(t)

g='-'.join(listch)
print(g)