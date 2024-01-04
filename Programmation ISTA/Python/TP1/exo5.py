N =int(input("Entrez un nombre :"))
Mod1 = N%3600
Mod2 = Mod1%60
H =(N-Mod1)/3600
M =(Mod1-Mod2)/60 #or M = N%60 
S = Mod2
print(f"équivalent de {N} c'est: {int(H)}h {int(M)}min {int(S)}sec")
