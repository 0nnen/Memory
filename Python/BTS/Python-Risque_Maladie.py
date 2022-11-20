print("\t\t\t\t=== TEST IMC ===\n\n")


poids=float(input("Entrez votre poids :\t"))
taille=float(input("Entrez votre taille :\t"))

IMC=poids/taille**2


if IMC<16:
    print("Votre IMC est de ",IMC,"Et vous etes d'une Maigreur extreme.")

elif 16<= IMC and IMC<18.5:
    print("Votre IMC est de ",IMC," Et vous etes Maigre.")

elif 18.5<= IMC and IMC<25:
    print("Votre IMC est de ",IMC,"Et vous etes \"normal\".")

elif 25<= IMC and IMC<30:
    print("Votre IMC est de ",IMC,"Et vous etes Embonpoint.")

elif 30<= IMC:
    print("Votre IMC est de ",IMC,"Et vous etes Obèse.")
 
