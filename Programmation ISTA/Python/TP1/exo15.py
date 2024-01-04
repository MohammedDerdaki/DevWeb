Salaire =int(input("Veuillez saisir votre salaire:"))
ChA =int(input("Veuillez saisir le chiffre d'affaire:"))
if ChA > 10000:
    print(f"Votre Salaire Net est :{Salaire+(ChA*0.2)}")
elif ChA >=5000 and ChA <=10000:
    print(f"Votre Salaire Net est :{Salaire+(ChA*0.1)}")
else:
    print(f"Votre Salaire Net est:{Salaire}")