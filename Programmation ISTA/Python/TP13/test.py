File=open("./TP13/notes2.txt","r")
L=File.readlines()
for i in L:
    T=i.split(" ")
    print(T)