print("\t\t\t\t=== Prix Concert : ===\n\n")


place=int(input("Combien de place voulez vous ?\n   "))
etudiant=str(input("Etes vous etudiant: y / n\n     "))
juin=str(input("Souhaitez vous commander pour le mois de Juin:  y / n\n     "))

#Si Y pour le mois de Juin alors le prix d'une place passe à 16€
if juin=="y":
    prix=place*16
else:
    prix=place*20

#Si plus de 3 places sont commandés, réduction de 10%
if place >=3:
    prix=prix*0.9

#Si Y pour etudiant, réduction de 25%
if etudiant=="y":
    prix = prix*0.75
    print ("Vous devez payer ",prix," pour un tarif etudiant")
else:
    print("Vous devez payer ",prix," pour un tarif basique")

