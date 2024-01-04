T =int(input("Veuillez saisir la température de l'eau:"))
if T <= 0 or T >= 100:
    if T <= 0:
        print("Etat de l'eau Solid")
    else:
        print("Etat de l'eau Gaz")
else:
    print("Etat de l'eau Liquid")