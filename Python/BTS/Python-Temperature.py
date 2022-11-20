print("\t\t\t\t=== Temperature - Etat de l'eau : ===\n\n")


temperature=int(input("Saisir une temperature:\t"))
if temperature <= 0:
    print ("C'est de la glace")
elif temperature >0 and temperature <100:
    print ("C'est de l'eau liquide")
elif temperature >=100:
    print ("C'est de la vapeur")
