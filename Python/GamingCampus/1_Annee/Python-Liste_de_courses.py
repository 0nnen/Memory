from os import system

print("\n\n\t\t\t\t\033[1;34;49m=== Exercice 8 - Liste de courses ===\033[0;37;49m\n\n")

liste_courses = ["Pain","Patate","Riz","Raisin","Pomme"]


def add_element():    # Pour ajouter un element à la liste
    global liste_courses
    
    while True:
        try:
            add = input ("\n\t\t\033[1;37;49m Entrez le nom du nouvel element:\t(cancel pour annuler) \t\033[1;35;49m")
            
            
            if add == "cancel" or add == "Cancel" :
                print("\t\t\t\033[1;31;49m Operation annulée\n\n")
                break

            else:
                liste_courses.append(add)
                liste_courses = [i.title() for i in liste_courses]    #Premier caractere de chaque element en MAJ
                liste_courses.sort()
                print("\t\t\t\t\t\033[1;32;49m Ajout réussi !!\n\n")
                
                
                # Verifie qu'il n'y ait pas de doublon
                for course in liste_courses:
                    if liste_courses.count(course) > 1:
                        liste_courses.remove(course)
                
                # Affiche les elements de liste_courses
                for ele in liste_courses:
                    print("\t\t\033[0;33;49m",ele)

                break

        except ValueError:
            print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")
  
def rem_element():    # Pour supprimer un element de la liste
    while True:
        try:
            rem = input ("\n\t\t\033[1;37;49m Entrez le nom de l'element à supprimer:\t(cancel pour annuler) \t\033[1;35;49m")

            if rem == ("cancel") or rem == ("Cancel"):
                print("\t\t\t\033[1;31;49m Operation annulée\n\n")
                break
            
            else:
                rem = rem.title()
                liste_courses.remove(rem)
                liste_courses.sort()       
                print("\t\t\t\t\t\033[1;32;49m Suppression réussie !!\n\n")
                
                # Affiche les elements de liste_courses
                for ele in liste_courses:
                    print("\t\t\033[0;33;49m",ele)
                break

        
        except ValueError:
            print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")
            for ele in liste_courses:
                print("\t\t\033[0;33;49m",ele)

def clear_list():    # Pour vider la liste
        while True:
            try:
                clear = int(input("\n\t\033[0;37;49m Etes-vous sur de vouloir supprimer entierement la liste ? \033[1;35;49m (Tapez 1) \t\t\033[0;37;49m Annuler \033[1;35;49m (Tapez 2) \n\t\t\t\t\t"))
                        
                if clear == 1 : # Supprimer la liste
                    liste_courses.clear()   # Supprime tous les éléments de liste_courses
                    print("\t\t\t\t\t\033[1;32;49m Suppression totale réussie !!\n\n")
                    break

                else : # Annule l'opération
                    print("\t\t\t\t\t\033[1;31;49m Suppression totale annulée !!\n\n")
                    break
        
            except ValueError:
                print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")

def show_list():
    for ele in liste_courses:
        print("\t\t\033[0;33;49m",ele)
    print("\n\n")


#En cas d'erreur de saisie:
while True:
    try:
        liste_courses.sort()
        choice = int(input("\n\t\033[0;37;49m Ajouter un élément \033[1;35;49m (Tapez 1) \t\t\033[0;37;49m Retirer un élément \033[1;35;49m (Tapez 2)\033[0;37;49m \n\t\033[0;37;49m Afficher les éléments \033[1;35;49m (Tapez 3)\t\033[0;37;49m Vider la liste \033[1;35;49m (Tapez 4)\n\n\t\033[0;37;49m Terminer la liste \033[1;35;49m (Tapez 5) \t\t\t"))
        
        if choice == 1 :    # Ajouter un élément
            add_element()
            
        elif choice == 2 :  # Retirer un élément
            rem_element()
            
        elif choice == 3 :  # Afficher les éléments
            show_list()

        elif choice == 4 :  # Vider la liste
            clear_list()
        
        elif choice == 5:   # Fin des courses
            print("\t\t\t\033[1;31;49m Liste de Courses terminée\n\n")
            system("pause")
            print("\033[0;37;49m")
            break
        
        else :
            print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")


    except ValueError:
        print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")
