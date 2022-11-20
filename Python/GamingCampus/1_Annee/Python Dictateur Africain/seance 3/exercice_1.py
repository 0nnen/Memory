#Un titre pour faire joli.
print("\n\n\t\t\t\t\033[1;34;49m=== Exercice 1 - Lenght ===\033[0;37;49m\n\n")

string= "J'aime le python" #Chaine de caracteres
letter= "m" #Lettre à trouver

#Longueur de string
print ("\033[0;37;49m Longueur de string:\t\t\033[1;35;49m",(len((string))))

#Position de letter dans string
print ("\033[0;37;49m Position de letter dans string:\033[1;35;49m",(string.index(letter)))

#Position du numero de caractere
print ("\033[0;37;49m Position de la 5e lettre:\t\033[1;35;49m",(string[5]))
print ("\033[0;37;49m Position de la 8e lettre:\t\033[1;35;49m",(string[8]))

#Affichage de string avec et sans MAJ
print ("\033[0;37;49m String sans modification:\t\033[1;35;49m",(string))
print ("\033[0;37;49m String en MAJ:\t\t\t\033[1;35;49m",(string.upper()),"\033[0;37;49m")