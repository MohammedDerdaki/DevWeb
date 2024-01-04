# x=int(input("saisir nombre line:"))
# y=int(input("saisir nombre de colum:"))
# i=0
# while (i<y+1):
#     print("*"*x)
#     i+=1

# n=int(input("Saisir nombre des lines:"))
# for i in range(1,n):
#     print((i)*"*","    ",(n-i)*"*")

# for j in range(1,x+1):
#     for i in range(1,y+1):
#         print("*", end="")
#     print()
n=int(input("line:"))
for j in range(1,n+1):
    for i in range(1,j):
        print("*", end=" ")
    print("")

for k in range(n,0,-1):
    for l in range(1,k):
        print("*", end="")
    print("")