Min =int(input("Saisir une borne minimal:"))
Max =int(input("Saisir une borne maximale:"))
X =int(input("saisir un nombre entre ces deux bornes:"))
while (X<Min or X>Max):
    X =int(input("Erreur,saisir à nouveau:"))
print("vous êtes reussi")