mydict = {"device": "laptop" , "constructeur": "acer" , "ram": "8G" , "processeur": "Intel core i5", 
"stockage": "500"}
mydict["stockage"]="750 G"

for i in mydict.keys():
    print(i)
for i in mydict.values():
    print(i)
for i in mydict.items():
    print(i)
print(mydict["ram"])
mydict["Système d'exploitation"]="Windows 10"
print(mydict)