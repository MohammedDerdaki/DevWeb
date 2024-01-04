X=int(input("Veuillez saisir le nombre base:"))
N=int(input("Veuillez saisir l'exposant:"))
Y=X
# if N==0:
#     X=1
# else:
#     if N>0:
#         for i in range(1,N):
#             X=X*Y
#     elif N<0:
#         for i in range(N+1,0):
#             X=X*Y
#         X=1/X
if N==0:
    X=1
else:
    if (N<0):
        N=N*(-1)
        Y=1/X
        X=1/X
    for i in range(1,N):
        X=X*Y
print("le resultat:", X)