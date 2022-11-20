#Fonction randrange nécessaire pour générer un nombre aléatoire.
from random import randrange

#Un titre pour faire joli.
print("\n\n\t\t\t\t\033[1;34;49m=== LE JEU DU NOMBRE MYSTERE ===\n\n")


#Demande si le joueur souhaite bel et bien jouer
play = input("\t\t\033[1;37;49m Etes-vous pret à jouer ?\n\t")

#Lorsque oui est tappé, le while commence. Boucle permettant de relancer une partie
while play == "oui" or play == "o" or play == "Oui" or play == "O":
    
    #On initie la variable essaie à 0.
    nombreEssaie = 0
    #On initie la variable nombrePropose à 0.
    nombrePropose = 0
    #On génère le nombre mystère.
    nombreMystere = randrange(1, 100)

    
    #Boucle qui continuera tant que l'utilisateur n'aura pas trouvé le nombre.
    while nombrePropose != nombreMystere:

    
        #On ajoute 1 à chaque fois que la boucle recommence.
        nombreEssaie = nombreEssaie + 1

        #En cas d'erreur de saisie:
        while True:
            try:
                #L'utilisateur propose son nombre.
                nombrePropose = int(input("\n\t\t\033[1;30;49m Quel est le nombre ?\n\033[0;37;49m\t"))
                break
            except ValueError:
                print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer\n")
            
            
            
        #Si le nombre est trop petit ou proche de la reponse...
        if nombrePropose + 5 == nombreMystere or nombrePropose + 4 == nombreMystere or nombrePropose + 3 == nombreMystere or nombrePropose + 2 == nombreMystere or nombrePropose + 1 == nombreMystere:
            print("\033[1;31;49m Trop petit mais tu chauffes !!\n\n")
        elif nombrePropose < nombreMystere:
            print("\033[0;31;49m C'est trop petit !\n\n")

        #Si le nombre est trop grand ou proche de la reponse...
        if nombrePropose - 5 == nombreMystere or nombrePropose - 4 == nombreMystere or nombrePropose - 3 == nombreMystere or nombrePropose - 2 == nombreMystere or nombrePropose - 1 == nombreMystere:
            print("\033[1;31;49m Trop grand mais tu chauffes !!\n\n")
        elif nombrePropose > nombreMystere:
            print("\033[0;31;49m C'est trop grand !\n\n")


        #Si le joueur a trouvé le nombre...
        if nombrePropose == nombreMystere:
            print("\033[1;32;49m Félicitations, vous avez trouvé le nombre mystère en ",nombreEssaie," coups !!!\n\n\n")


        #Termine la partie si nombreEssaie atteint 7
        if nombreEssaie >= 7 and nombrePropose != nombreMystere :
            print("\t\t\033[1;35;49m Mince... Tu as depassé le nombre d'essai possible")
            break

    #Re-demande si le joueur souhaite continuer
    play = input("\t\t\t\033[1;34;49m Souhaitez-vous refaire une partie ?? \n\t\033[0;37;49m  ")
