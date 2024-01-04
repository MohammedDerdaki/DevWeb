MF =int(input("Veuillez saisir votre monatant de la facture:"))
if MF>= 2200:
    MF -=(MF*0.06)
elif MF>= 1200 and MF<2200:
    MF -=(MF*0.03)
print(f"Votre facture est :{MF}")