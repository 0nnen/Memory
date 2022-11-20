#Un titre pour faire joli.
print("\n\n\t\t\t\t\033[1;34;49m=== Exercice 6 - Pyramide ===\033[0;37;49m\n\n")


def pyramid():
    
    try:    
        L= int(input("\033[1;37;49m Entrez le nombre de lignes: \033[1;35;49m\t"))
        for i in range (L+1) :
            
            #Place la pyamide au milieu en fonction de L
            for j in range (L-i+1) :
                print("\033[3;37;40m  ",end="")
            
            #Affiche $
            for j in range (1,2*i-1+1):
                print("\033[3;37;40m$ ",end="")
                
            print("\033[0;37;40m")
        
    except ValueError:
        print("\t\t\t\033[1;31;49m Saisie Invalide\n\n\033[1;37;49m")



pyramid()
