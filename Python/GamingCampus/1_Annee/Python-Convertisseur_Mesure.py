#Un titre pour faire joli.
print("\n\n\t\t\t\t\033[1;34;49m=== LE JEU DU NOMBRE MYSTERE ===\n\n")

#On demande le nombre 
convert = input("\t\t\t\033[1;30;49m Voulez-vous convertir une valeur ? \n\t\t\t\t\033[1;37;49m")

# Lorsque oui est tappé, le while commence
while convert == "oui" or convert == "o" or convert == "Oui" or convert == "O":
    
    #En cas d'erreur de saisie:
    while True:
        try:
            #Nous avons le choix d'un sens ou dans l'autre
            choice = int(input("\n\t\033[0;37;49m Pouces vers cm \033[1;35;49m (Tapez 1) \t\033[0;37;49m Cm vers pouces \033[1;35;49m (Tapez 2)\033[0;37;49m \n"))
            break
        
        except ValueError:
            print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")
    
    #Pouces to Cm
    if choice == 1 :
        #En cas d'erreur de saisie:
        while True:
            try:
                value_PtoCm = float(input("\033[1;37;49m\n\t\tNombre en pouces :\n"))
                value_PtoCm = value_PtoCm*2.54
                print("\033[1;32;49m\t",value_PtoCm, "centimetres")
                break
            
            except ValueError:
                print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n")
        

    #Cm to Pouces
    elif choice == 2 :
                #En cas d'erreur de saisie:
        while True:
            try:
                valeur_CmtoP = float(input("\033[1;37;49m\n\t\tNombre en centimetres :\n"))
                valeur_CmtoP = valeur_CmtoP*0.394
                print("\033[1;32;49m\t",valeur_CmtoP, "pouces")
                break
            
            except ValueError:
                print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n")

        
    else:
        print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer\n\n")
        choice = int(input("\n\t\033[0;37;49m Pouces vers cm \033[1;35;49m (Tapez 1) \t\033[0;37;49m Cm vers pouces \033[1;35;49m (Tapez 2)\033[0;37;49m \n"))

    
    convert = input("\t\t\t\033[1;30;49m Voulez-vous convertir une autre valeur ? \n\t\t\t\t\033[1;37;49m")