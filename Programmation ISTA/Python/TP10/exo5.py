def  NBCasse(ch):
    j=0
    k=0
    for i in range(len(ch)):
        if (ch[i].isupper()==True):
            k+=1
        else:
            j+=1
    return print(f"le nombre de lettre mini est {j} et le nombre de lettres maj est {k}")
ch=input("Entrez une phrase: ")
NBCasse(ch)
