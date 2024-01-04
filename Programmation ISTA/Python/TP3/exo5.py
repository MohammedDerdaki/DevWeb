
for j in range(2,501):
    Som=0
    for i in range(1,j):
        if j%i==0:
            Som=Som+i     
    if Som==j:
            print(f"Le nombre {Som} est parfait")
            
