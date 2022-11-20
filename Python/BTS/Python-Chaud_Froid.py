#Fonction randrange nécessaire pour générer un nombre aléatoire.
from random import randrange
from colorama import Fore
from colorama import Style
#On initie la variable nombrePropose à 0.
nombrePropose = 0

#On initie la variable essaie à 0.
nombreEssaie = 0

#Un titre pour faire joli.
print("\t\t\t\t=== LE JEU DU CHAUD OU FROID ===\n\n")
print("33[0;37;40m Normal textn")
#On génère le nombre mystère.
nombreMystere = randrange(1, 100)
 
#Boucle qui continuera tant que l'utilisateur n'aura pas trouvé le nombre.
while nombrePropose != nombreMystere:

    #On ajoute 1 à chaque fois que la boucle recommence.
    nombreEssaie = nombreEssaie + 1

    print("\t\tQuel est le nombre ?")
 
    #L'utilisateur propose son nombre.
    nombrePropose = input()
    nombrePropose = int(nombrePropose)
 


    #Si le nombre est trop petit...
    if nombrePropose < nombreMystere:
        print("C'est trop petit !\n\n")


    #Sinon si le nombre est trop grand...
    elif nombrePropose > nombreMystere:
        print("C'est trop grand !\n")


    #Sinon (sous-entendu : si on a trouvé le nombre)...
    else:
        print("Félicitations, vous avez trouvé le nombre mystère en ",nombreEssaie," coups !!!\n")
 
