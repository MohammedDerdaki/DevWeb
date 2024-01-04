D={'nom':'Dupuis','prenom':'Jacque','age':30}
D['prenom']="Jacques"
print(D)
for i in D.keys():
    print(i)
for i in D.values():
    print(i)
for i in D.items():
    print(i)

print(f"{D['prenom']} {D['nom']} a {D['age']} ans")