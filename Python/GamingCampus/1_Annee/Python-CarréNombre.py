#Un titre pour faire joli.
print("\n\n\t\t\t\t\033[1;34;49m=== Exercice 4 - Carré ===\033[0;37;49m\n\n")

def carre(num):
        # En cas d'erreur :
    try:    
        Car = num*num
        print("\t\t\t\033[0;37;49m Le carré de \033[1;35;49m",num,"\033[0;37;49m est \033[1;35;49m",Car,"\033[0;37;49m")
        
    # Faire :
    except:
        print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n\033[1;37;49m")
        while True:
            num = int(input("\n\t\033[0;37;49m Entrez un nombre pour obtenir son carré: \033[1;35;49m "))
            print ("\t\t\t",carre(num),"\033[1;37;49m")
            

# Demande la saisie d'un nombre
num = int(input("\n\t\033[0;37;49m Entrez un nombre pour obtenir son carré: \033[1;35;49m "))

# Fonction inverse
print (carre(num))
print (carre(5))  # Comme demandé dans l'exercice
print (carre(18)) # Comme demandé dans l'exercice
