from os import system

print("\n\n\t\t\t\t\033[1;34;49m=== Projet - Crepe's Store ===\033[0;37;49m\n\n")

# Declare variables
panier=[]
list_crepe =[{"nom":"Crepe Bonanza",
                "prix":25.99,
                "type":"Salée"},
             
             {"nom":"Crepe Confiture de Pomme",
                "prix":3.99,
                "type":"Sucrée"},
             
             {"nom":"Crepe Jambon & Fromage",
                "prix":16.99,
                "type":"Salée"},
             
             {"nom":"Crepe Salade Cesar",
                "prix":48.99,
                "type":"Salée"}]
 
 
list_crepeType = ["Salée", "Sucrée","Végétarienne"]

list_ingreSalty = [{"nom":"Jambon",
                    "prix":5.99},
                   
                  {"nom":"Poulet",
                    "prix":5.99},

                  {"nom":"Fromage",
                   "prix":1.99}]

list_ingreSweet = [{"nom":"Confiture de Fraises",
                    "prix":9.99},
                  
                  {"nom":"Confiture de Pommes",
                    "prix":6.99},
                    
                  {"nom":"Sucre",
                    "prix": 3.99}]

list_ingreVege = [{"nom" :"Tomates",
                    "prix": 6.99},
                    
                    {"nom":"Oignons",
                    "prix": 4.99},
                    
                    {"nom": "Brocoli",
                    "prix":3.99}]



# Functions                       
def showList_alpha(): # Show crepes by alphabeticalby. checking every character (len) in the list. then uses tri_selection function and prints variables in order.
    
    print ("\n\n\t\033[1;34;49m La liste de crêpes par ordre alphabétique (croissant): ")

    nm = 1
    for i in range (len(list_crepe)):
        tri_selectionUp(list_crepe,"nom")
        print ("\t\t\033[0;33;49m", nm,". \033[0;37;49m",list_crepe[i]["nom"],list_crepe[i]["prix"])
        nm += 1
        
    while True:
        try:

            choice = int(input("\n\t\033[0;33;49m 1.\033[0;37;49m Crepe Bonanza  (\033[1;35;49mTapez 1\033[0;37;49m)"
                            "\n\t\033[0;33;49m 2.\033[0;37;49m Crepe Confiture de Pomme  (\033[1;35;49mTapez 2\033[0;37;49m)"
                            "\n\t\033[0;33;49m 3.\033[0;37;49m Crepe Jambon & Fromage  (\033[1;35;49mTapez 3\033[0;37;49m) "
                            "\n\t\033[0;33;49m 4.\033[0;37;49m Crepe Salade Cesar  (\033[1;35;49mTapez 4\033[0;37;49m) "
                            "\n\t\033[0;33;49m 5.\033[0;37;49m Personaliser votre crepe  (\033[1;35;49mTapez 5\033[0;37;49m)"
                            "\n\n\t\033[0;37;49m Achats terminés : (\033[1;35;49mTapez 6\033[0;37;49m) \033[1;35;49m\t\t\t"))
            
            if choice == 1 :    # add "Crepe Bonanza" to panier
                system("cls")
                print("\t \033[0;37;49m Crepe ajoutée :\t\033[1;35;49m",list_crepe[0]["nom"],"\033[0;37;49m pour \033[0;33;49m",list_crepe[0]["prix"])
                panier.append(list_crepe[0])
                panier_func()

            elif choice == 2 :  # add "Crepe Confiture de Pomme" to panier
                system("cls")
                print("\t \033[0;37;49m Crepe ajoutée :\t\033[1;35;49m",list_crepe[1]["nom"],"\033[0;37;49m pour \033[0;33;49m",list_crepe[1]["prix"])
                panier.append(list_crepe[1])
                panier_func()

                
            elif choice == 3 :  # add "Crepe Jambon & Fromage" to panier
                system("cls")
                print("\t \033[0;37;49m Crepe ajoutée :\t\033[1;35;49m",list_crepe[2]["nom"],"\033[0;37;49m pour \033[0;33;49m",list_crepe[2]["prix"])
                panier.append(list_crepe[2])
                panier_func()


            elif choice == 4 :  # add "Crepe Salade Cesar" to panier
                system("cls")
                print("\t \033[0;37;49m Crepe ajoutée :\t\033[1;35;49m",list_crepe[3]["nom"],"\033[0;37;49m pour \033[0;33;49m",list_crepe[3]["prix"])
                panier.append(list_crepe[3])
                panier_func()

            
            elif choice == 5: # Crepe Personnalized
                system("cls")
                persoCrepe()
                panier_func()

            elif choice == 6:   # Close Menu
                system("cls")
                print ("\n\n\t\t\t\033[1;31;49m Achats terminés\n\n")
                break
            
            else : # If the input is a INT but a wrong one
                system("cls")
                print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")



        except ValueError: # If the input isn't a INT
            system("cls")
            print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")

    print ("\n\n")



def showList_price(): # Show crepes by price (Cheapest to Most Expensive.) by checking every character (len) in the list. then uses tri_selection function and prints variables in order.
    
    print ("\n\n\t\033[1;34;49m La liste de crêpes par prix (croissant) : ")

    nm = 1        
    for i in range (len(list_crepe)):
        tri_selectionDown(list_crepe,"prix")
        print ("\t\t\033[0;33;49m", nm,". \033[0;37;49m",list_crepe[i]["nom"],list_crepe[i]["prix"])
        nm += 1

    while True:
        try:
            choice = int(input("\n\t\033[0;33;49m 1.\033[0;37;49m Crepe Salade Cesar  (\033[1;35;49mTapez 1\033[0;37;49m)"
                            "\n\t\033[0;33;49m 2.\033[0;37;49m Crepe Bonanza  (\033[1;35;49mTapez 2\033[0;37;49m)"
                            "\n\t\033[0;33;49m 3.\033[0;37;49m Crepe Jambon & Fromage  (\033[1;35;49mTapez 3\033[0;37;49m) "
                            "\n\t\033[0;33;49m 4.\033[0;37;49m Crepe Confiture de Pomme  (\033[1;35;49mTapez 4\033[0;37;49m) "
                            "\n\t\033[0;33;49m 5.\033[0;37;49m Personaliser votre crepe  (\033[1;35;49mTapez 5\033[0;37;49m)"
                            "\n\n\t\033[0;37;49m Achats terminés : (\033[1;35;49mTapez 6\033[0;37;49m) \033[1;35;49m\t\t\t"))

            if choice == 1 :    # add Crepe Bonanza to panier
                system("cls")

                panier.append(list_crepe[0])
                panier_func()
                print(panier)

            elif choice == 2 :  # add Crepe Bonanza to panier
                system("cls")
                panier.append(list_crepe[1])
                panier_func()
                print(panier)

            elif choice == 3 :  # add Crepe Bonanza to panier
                system("cls")
                panier.append(list_crepe[2])
                panier_func()
                print(panier)

            elif choice == 4 :  # add Crepe Bonanza to panier
                system("cls")
                panier.append(list_crepe[3])
                panier_func()
                print(panier)

            elif choice == 5: # Crepe Personnalized
                system("cls")
                persoCrepe()
                panier_func()

            elif choice == 6:   # Close Menu
                system("cls")
                print ("\n\n\t\t\t\033[1;31;49m Achats terminés\n\n")
                break

            else : # If the input is a INT but a wrong one
                system("cls")
                print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")

        except ValueError: # If the input isn't a INT
            system("cls")
            print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")

    print ("\n\n")




def showList_expen(): # Show crepes most expensive by checking every character (len) in the list. then uses tri_selection function and prints variables in order.
    tri_selectionDown(list_crepe,"prix")
    
    print ("\n\n\t\033[1;34;49m Crêpe la plus chère : ")
      

    print ("\t\t\033[0;33;49m",list_crepe[0]["nom"],list_crepe[0]["prix"],list_crepe[0]["type"])
    print ("\n\n")

def showList_cheap(): # Show the cheapest Crepes by checking every character (len) in the list. then uses tri_selection function and prints variables in order.
    tri_selectionUp(list_crepe,"prix")
    
    print ("\n\n\t\033[1;34;49m Crêpe la moins chère : ")
      

    print ("\t\t\033[0;33;49m",list_crepe[0]["nom"],list_crepe[0]["prix"],list_crepe[0]["type"])
    print ("\n\n")


def tri_selectionUp(tab,arg): #all tri_selection functions are similar. Only difference is that each one sorts in a different manner.
    for i in range (len(tab)):
       
      # Find min by checking the variables i and j, i+1 exists to compare each caractere in the variable and comparing it with j. if i is bigger than j; then j becomes the new min (the smallest variable)
        min = i
        for j in range (i+1, len(tab)):
           if tab[min][arg] > tab[j][arg]:
               min = j
        
        #Exchange between tab[i] and tab[min]. tmp exists to stock the variables to exchange them temporarly.      
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab

def tri_selectionDown(tab,arg):
    for i in range (len(tab)):
       
      # Find min by checking the variables i and j, i+1 exists to compare each caractere in the variable and comparing it with j. if i is bigger than j; then j becomes the new min (the smallest variable)
        min = i
        for j in range (i+1, len(tab)):
           if tab[min][arg] < tab[j][arg]:
               min = j
        
        #Exchange between tab[i] and tab[min]. tmp exists to stock the variables to exchange them temporarly.      
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab


def tri_bubble(tab,arg): #Doesnt used but work.
    n = len(tab)
    # Browse in the list
    for i in range(n):
         for j in range(0, n-i-1):
             
            # Transfer is the next element is higher
            if tab[j][arg] > tab[j+1][arg] :
                tab[j], tab[j+1][arg] = tab[j+1][arg], tab[j][arg]
    return tab



def persoCrepe(): #allows user to choose different ingredients from the list inside the type they chose.

    crepeIngredients = []
    crepeType = ""
    crepePrice = 0.0
    while crepeType != "Salée" and crepeType != "Sucrée" and crepeType != "Végé":
        crepeType = input("\t\t\033[0;37;49m Voulez vous une crepe \033[1;35;49mSalée\033[0;37;49m, \033[1;35;49mSucrée\033[0;37;49m ou \033[1;35;49mVégé\033[0;37;49m?: (\033[1;35;49mcancel\033[0;37;49m)\t\t\033[1;35;49m")  
        if crepeType == "cancel": return

    # As long as smthElse is true, repeat the crepeType loop. If any of the variables the user inputs are not equal to the ones declared in the loop, repeat the loop. if yeet = non then break loop.
    smthElse = True 
    
    # ------ Ingredients Choice : ------
    if crepeType == "Salée":
        while smthElse:
            ingr = ""
            while ingr != "Jambon" and ingr != "Poulet" and ingr != "Fromage":
                ingr = input("\n\t\t\033[0;37;49m Ingrédients: \033[1;35;49mJambon\033[0;37;49m, \033[1;35;49mPoulet\033[0;37;49m, \033[1;35;49mFromage\033[0;37;49m: (\033[1;35;49mcancel\033[0;37;49m)\t\t\033[1;35;49m") 
                if ingr == "cancel": return
            crepeIngredients.append(ingr)
            yeet = ""
            while yeet != "Oui" and  yeet != "Non":
                yeet = input("\t\033[0;37;49m Voulez-vous un/des autre(s) ingrédients (\033[1;35;49mOui/Non\033[0;37;49m)\t\t\033[1;35;49m")
            smthElse = True if yeet == "Oui" else False 
            
    elif crepeType == "Sucrée":
        while smthElse:
            ingr = ""
            while ingr != "Confiture de Fraises" and ingr != "Confiture de Pommes" and ingr != "Sucre":
                ingr = input("\n\t\t\033[0;37;49m Ingrédients: \033[1;35;49mConfiture de Fraises\033[0;37;49m, \033[1;35;49mConfiture de Pommes\033[0;37;49m, \033[1;35;49mSucre\033[0;37;49m: (\033[1;35;49mcancel\033[0;37;49m)\t\t\033[1;35;49m")
                if ingr == "cancel": return
            crepeIngredients.append(ingr)
            yeet = ""
            while yeet != "Oui" and  yeet != "Non":
                yeet = input("\t\033[0;37;49m Voulez-vous un/des autre(s) ingrédients (\033[1;35;49mOui/Non\033[0;37;49m)\t\t\033[1;35;49m")
            smthElse = True if yeet == "Oui" else False 
            
    if crepeType == "Végé":
        while smthElse:
            ingr = ""
            while ingr != "Tomates" and ingr != "Oignons" and ingr != "Brocoli":
                ingr = input("\n\t\t\033[0;37;49m Ingrédients: \033[1;35;49mTomates\033[0;37;49m, \033[1;35;49mOignons\033[0;37;49m, \033[1;35;49mBrocoli\033[0;37;49m: (\033[1;35;49mcancel\033[0;37;49m)\t\t\033[1;35;49m")
                if ingr == "cancel": return
            crepeIngredients.append(ingr)
            yeet = ""
            while yeet != "Oui" and  yeet != "Non":
                yeet = input("\t\033[0;37;49m Voulez-vous un/des autre(s) ingrédients (\033[1;35;49mOui/Non\033[0;37;49m)\t\t\033[1;35;49m")
            smthElse = True if yeet == "Oui" else False 
            
    crepeIngredients = list(set(crepeIngredients)) #declares function as a list then utilises set( ) function to disable any duplicates inputed by user 
    
    # ------ Calcul : ------
    if crepeType == "Salée":
        for i in range(len(crepeIngredients)):
            if crepeIngredients[i] == "Jambon":
                crepePrice += list_ingreSalty[0]["prix"]
            elif crepeIngredients[i] == "Poulet":
                crepePrice += list_ingreSalty[1]["prix"]
            else:
                crepePrice += list_ingreSalty[2]["prix"]
                
    if crepeType == "Sucrée":
        for i in range(len(crepeIngredients)):
            if crepeIngredients[i] == "Confiture de Fraises":
                crepePrice += list_ingreSweet[0]["prix"]
            elif crepeIngredients[i] == "Confiture de Pommes":
                crepePrice += list_ingreSweet[1]["prix"]
            else:
                crepePrice += list_ingreSweet[2]["prix"]
                
    if crepeType == "Végé":
        for i in range(len(crepeIngredients)):
            if crepeIngredients[i] == "Tomates":
                crepePrice += list_ingreVege[0]["prix"]
            elif crepeIngredients[i] == "Oignons":
                crepePrice += list_ingreVege[1]["prix"]
            else:
                crepePrice += list_ingreVege[2]["prix"]


    CrepeNamePerso = input("\t\033[0;37;49mEntrez le nom de votre crêpe: \t\033[1;35;49m")

    # Show the crepe informations 
    ingredientsPerso = ", ".join(crepeIngredients)
    print("\n\t\t\033[0;37;49mLa crêpe\033[1;35;49m", CrepeNamePerso,"\033[0;37;49mcontenant\033[1;36;49m", ingredientsPerso, "\033[0;37;49mcoûtant\033[1;33;49m", crepePrice, "€ \033[0;37;49ma été ajoutée au panier.\n")

    # Create and Add the crepe to list_crepe and panier
    newCrepe = {'nom':str("Crepe " + CrepeNamePerso),
                 'prix':float(crepePrice),
                 'ingr':ingredientsPerso}
    
    list_crepe.append(newCrepe)
    panier.append(newCrepe)
    panier_func()
    

def panier_func():
    total = 0.0
    oui = open('Panier.txt', 'w',encoding='UTF-8')
    oui.write('~ PANIER ~'.center(67))
    oui.write('\n\n')
    oui.write ('--------------------------------------------\n\n'.center(70))
    oui.write('\n')
    
    for i in panier:
        total = total + i['prix']
        
        oui.write (str(i['nom']).center(50))
        oui.write (' - ')
        oui.write (str(i['prix']))
        oui.write ('€\n')
    
    total = round(total, 2) # Take two numbers after the comma
    oui.write('\n')
    oui.write ('==============================================\n\n'.center(70))
    oui.write ('Total :'.ljust(20))
    oui.write(str(total).rjust(26))


while True:
    try:
        choice = int(input("\n\t\033[0;37;49m Afficher la liste de crêpes par ordre alphabétique  (\033[1;35;49mTapez 1\033[0;37;49m)"
                           " \n\t\033[0;37;49m Afficher la liste de crêpes par prix croissant  (\033[1;35;49mTapez 2\033[0;37;49m)"
                           " \n\t\033[0;37;49m Afficher la crêpe la plus chère  (\033[1;35;49mTapez 3\033[0;37;49m) "
                           "\n\t\033[0;37;49m Afficher la crêpe la moins chère  (\033[1;35;49mTapez 4\033[0;37;49m) "
                           "\n\t\033[0;37;49m Personaliser votre crepe  (\033[1;35;49mTapez 5\033[0;37;49m)"
                           "\n\n\t\033[0;37;49m Achats terminés :  (\033[1;35;49mTapez 6\033[0;37;49m) \033[1;35;49m\t\t\t"))
        
        if choice == 1 :    # Show crepes by alphabetical
            system("cls")
            showList_alpha()
            
        elif choice == 2 :  # Show crepes by price (Cheapest to Most Expensive.)
            system("cls")
            showList_price()
            
        elif choice == 3 :  # Show crepes most expensive
            system("cls")
            showList_expen()

        elif choice == 4 :  # Show the cheapest Crepes
            system("cls")
            showList_cheap()
        
        elif choice == 5:
            system("cls")
            persoCrepe()

        elif choice == 6:   # Close Menu
            system("cls")
            print ("\n\n\t\t\t\033[1;31;49m Achats terminés\n\n")
            system("pause")
            print ("\033[0;37;49m")#Reset the color
            break
        
        else : # If the input is a INT but a wrong one
            system("cls")
            print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")



    except ValueError: # If the input isn't a INT
        system("cls")
        print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n")
