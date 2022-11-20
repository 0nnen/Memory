age=int(input("Entrez votre age:    "))
obtention=int(input("Entrez l'année d'obtention du permis:    "))

if age < 25 and obtention <=2 :
    print (" Tarif ROUGE")

if age <= 25 and obtention < 2 :
    print (" Tarif VERT")

else:
    print (" Tarif ORANGE")