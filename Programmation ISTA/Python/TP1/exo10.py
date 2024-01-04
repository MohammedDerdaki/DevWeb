hr =int(input("Veuillez saisir l'heure:"))
mn =int(input("Veuillez saisir minute:"))
mn +=1
if mn ==60:
    if hr==23:
        hr = 0
        mn = 0
    else:
        hr += 1
        mn = 0
print(f"Dans un minute, il sera {hr} heure(s) et {mn} minute(s)")