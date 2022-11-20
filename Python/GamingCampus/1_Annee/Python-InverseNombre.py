#Un titre pour faire joli.
print("\n\n\t\t\t\t\033[1;34;49m=== Exercice 3 - Inverse ===\033[0;37;49m\n\n")

def inverse(num):
    
    # En cas d'erreur :
    try:    
        Inv = 1/num
        print("\t\t\t\033[0;37;49m L'inverse de \033[1;35;49m",num,"\033[0;37;49m est \033[1;35;49m",Inv,"\033[0;37;49m")
        
    # Faire :
    except:
        print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n\033[1;37;49m")
        while True:
            num = int(input("\n\t\033[0;37;49m Entrez un nombre pour obtenir son inverse: \033[1;35;49m "))
            print ("\t\t\t",inverse(num),"\033[1;37;49m")
            

# Demande la saisie d'un nombre
num = int(input("\n\t\033[0;37;49m Entrez un nombre pour obtenir son inverse: \033[1;35;49m "))

# Fonction inverse
print (inverse(num))