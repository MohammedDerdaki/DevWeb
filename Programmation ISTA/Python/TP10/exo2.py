def OccurCara(c):
    global Ch
    j=0
    for i in Ch:
        if c==i:
            j+=1
    return j
Ch=input("Entrez une phrase: ")
c=input("Entrez le caractere cherecher: ")
print(f"Le nombre de fois se trouve le caractere {c} dans la phrase est : {OccurCara(c)}")