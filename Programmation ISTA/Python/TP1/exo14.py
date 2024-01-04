An =int(input("Veuillez saisir l'année:"))
if (An%4==0 and An%100!=0) or An%400==0:
    print("année bissextile")
else:
    print("année non bissextile") 