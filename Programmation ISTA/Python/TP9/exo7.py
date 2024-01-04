def change(x,y):
    x=y-x
    y=y-x
    x=x+y
    print(x,y)

x=int(input("entrez un nombre: "))
y=int(input("entrez un nombre: "))
change(x,y)