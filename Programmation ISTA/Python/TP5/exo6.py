A=[0,1,2,3,4,5,6,7,8,9,1]
VAL=int(input("Entrez un nombre: "))
if VAL in A:
    POS=0
    for i in A:
        POS+=1
        if VAL==i:
            print(f"la valeur {VAL} est dans la liste, et son positon {POS}")
                 
else:
    print(f"cette  valeur {VAL} n'existe pas dans cette liste. position est -1")




