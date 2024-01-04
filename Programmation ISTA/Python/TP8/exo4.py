d = {"Aladin": [12, 15 , 17] , "Nathalie" : [15, 13, 16] , "Robert": [13, 15 , 11] }
m=0
for i in d.keys():
    s=0
    for a in d[i]:
        s=s+a
    m=s/3
    d[i].append(m)
print(d)


