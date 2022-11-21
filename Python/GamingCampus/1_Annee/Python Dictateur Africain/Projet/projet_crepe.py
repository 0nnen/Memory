from os import system

print("\n\n\t\t\t\t\033[1;34;49m=== Projet - Crepe's Store ===\033[0;37;49m\n\n")


# Declare variables
list_crepe = [["Crepe Bonanza",25.99,"Sucrée"],["Crepe Confiture de Pomme",3.99,"Sucrée"],["Crepe Jambon & Fromage",16.99,"Salée"],["Crepe Salade Cesar ",48.99,"Salée"],["Crepe Personalisée",0,""]]
 
list_crepeType = ["Salé", "Sucré","Végetarien"]
list_ingreSalty = []
list_ingreSweet = []
list_ingreVege = []

personalizedCrepe = [""]



# Functions
def showList_alpha(): # Show crepes by alphabetical
    
    print ("\n\n\t\033[1;34;49m La liste de crêpes par ordre alphabétique (croissant): ")

    
    nm = 1
    for i in range (len(list_crepe)):
        tri_selection(list_crepe)
        print ("\t\t\t\t\t\t\033[0;33;49m", nm,". ",list_crepe[i][0],list_crepe[i][1],list_crepe[i][2])
        nm += 1


    print ("\n\n")
    
    
    
def showList_price(): # Show crepes by price (Cheapest to Most Expensive.) 
    
    print ("\n\n\t\033[1;34;49m La liste de crêpes par prix croissant : ")
    tri_selection(list_crepe)
        

    for ele in list_crepe[0][1]:
        print("\t\t\t\t\t\t\033[0;33;49m",ele)
    print ("\n\n")




def showList_expen(): # Show crepes most expensive 
    
    # tri_selection(list_tmp)
    # for ele in list_tmp:
    #     print("\t\t\t\t\t\t\033[0;33;49m",ele)
    print ("\n\n")



def showList_cheap(): # Show the cheapest Crepes 
    print()



def tri_selection(tab):
    for i in range (len(tab)):
       
      # Find min by checking the variables i and j, i+1 exists to compare each caractere in the variable and comparing it with j. if i is bigger than j; then j becomes the new min (the smallest variable)
        min = i
        for j in range (i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
        
        #Exchange between tab[i] and tab[min]. tmp exists to stock the variables to exchange them temporarly.      
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
        
    return tab



while True:
    try:
        choice = int(input("\n\t\033[0;37;49m Afficher la liste de crêpes par ordre alphabétique \033[1;35;49m (Tapez 1) \n\t\033[0;37;49m Afficher la liste de crêpes par prix croissant \033[1;35;49m (Tapez 2)\033[0;37;49m \n\t\033[0;37;49m Afficher la crêpe la plus chère \033[1;35;49m (Tapez 3) \n\t\033[0;37;49m Afficher la crêpe la moins chère \033[1;35;49m (Tapez 4)\n\n\t\033[0;37;49m Terminer la liste \033[1;35;49m (Tapez 5) \t\t\t"))
        
        if choice == 1 :    # Show crepes by alphabetical
            showList_alpha()
            
        elif choice == 2 :  # Show crepes by price (Cheapest to Most Expensive.)
            showList_price()
            
        elif choice == 3 :  # Show crepes most expensive
            showList_expen()

        elif choice == 4 :  # Show the cheapest Crepes
            showList_cheap()
        
        elif choice == 5:   # Close Menu
            print("\t\t\t\033[1;31;49m Achats terminés\n\n")
            system("pause")
            print("\033[0;37;49m")
            break
        
        else :
            print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")


    except ValueError:
        print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")


    