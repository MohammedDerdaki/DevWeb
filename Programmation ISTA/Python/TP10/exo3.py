def compteMots(phrase):
    word=0
    for i in range(len(phrase)-1):
        if (phrase[0]!=" ") and (i==0):
            word+=1
            print(word,phrase[i])
            
        elif (phrase[i]==" ") and ((phrase[i+1]!=" " )):
            word+=1
            print(word,phrase[i+1])
    return print("nombre:",word)

phrase=input("Entrez une phrase: ")
compteMots(phrase)