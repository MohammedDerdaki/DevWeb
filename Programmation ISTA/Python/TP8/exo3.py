etudiants = {"etudiant_1" : 13 , "etudiant_2" : 17 , "etudiant_3" : 9 , "etudiant_4" : 15 ,"etudiant_5" :
8 , "etudiant_6" : 14 , "etudiant_7" : 16 , "etudiant_8" : 12 , "etudiant_9" : 13 , "etudiant_10" : 15 ,
"etudiant_11" : 14 , "etudiant_12" : 9 , "etudiant_13" : 10 , "etudiant_14" : 12 , "etudiant_15" : 13 ,
"etudiant_16" : 7 , "etudiant_17" : 12 , "etudiant_18" : 15 , "etudiant_19" : 9 , "etudiant_20" : 17}
etudiantAdmis={}
etudiantNonAdmis={}
for a,b in etudiants.items():
    if b<10:
        etudiantNonAdmis[a]=b
    else:
        etudiantAdmis[a]=b
print("les etudiant admis:")
for i in etudiantAdmis.items():
    print(i)
print("les etudiant non admis:")
for i in etudiantNonAdmis.items():
    print(i)