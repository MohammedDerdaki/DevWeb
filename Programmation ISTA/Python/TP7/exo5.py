CH=input("Entrez un text: ")
x=""
#method1
x=CH[(len(CH))::-1]
print(x)
#method2
# for i in range(len(CH)-1,-1,-1):
#     x=x+CH[i]
if CH==x:
    print(f"{CH} est palindrome")
else:
    print(f"{CH} n'est pas palindrome")