import random

print("\n\t\t\t\t=== Exercice 2: ===\n\n")

# Déclaration des randint
numAle1 = random.randint(0,100)
numAle2 = random.randint(0,100)

# Déclaration des résultats des calculs
res_add = numAle1 + numAle2
res_sou = numAle1 - numAle2
res_div = numAle1 // numAle2
res_mul = numAle1 * numAle2

i = 1

# Affichage du calcul - Addition
print ("\t Calcul: ",numAle1,"+",numAle2)
print ("Essai", i)
choose = int(input("Entrez le resultat :\t"))

# Vérification du résultat - Addition
if choose == res_add :
    print("\t\t Bravo, le resultat est correct ! \n Vous avez eu le resultat en",i, "essai(s)")
else :
    while i < 5:
        i= i+1
        
        print ("\nEssai", i)
        choose = int(input("Entrez le resultat :\t"))
        if choose == res_add :
            print("\n\t\t Bravo, le resultat est correct ! \n\t Vous avez eu le resultat en",i, "essai(s)")

        if i ==5:
            print("\t\t Vous etes mauvais !")
