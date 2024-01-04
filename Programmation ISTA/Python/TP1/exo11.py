Gender =input("Veuillez saisir votre genre:")
if Gender == "H" or Gender == "F" or Gender == "h" or Gender == "f":
    Age =int(input("Veuillez saisir votre âge:"))
    if Gender == "H" or Gender=="h":
        if Age >= 20:
            print("Vous êtes obligé de payer l'impôt")
        else:
            print("Vous êtes dispensez")
    elif Gender == "F" or Gender=="f":
        if Age >= 18 and Age <= 35:
            print("Vous êtes obligé de payer l'impôt")
        else:
            print("Vous êtes dispensez")
else:
        print("erreur du genre ")



