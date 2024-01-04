CH1=input("Entrez un text: ")
CH2=input("Entrez un text: ")
CH3=""
x=len(CH1)//2
y=len(CH2)//2
for i in range(x+1):
    CH3=CH3+CH1[i]
for j in range(y+1):
    CH3=CH3+CH2[j]
print(CH3)