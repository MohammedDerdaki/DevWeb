# i=0
suite=[]
suite.append(1)
suite.append(1)
for i in range(2,6):
    suite.append(suite[i-1]+suite[i-2])

for i in range(6):
    print(suite[i])