import random

print("\n\n\t\t\t\t\033[1;34;49m=== Exercice 7 - Phrases aléatoires ===\033[0;37;49m\n\n")


sujet=["Il","Ines","William","Le dictateur","Alice","Sage","Victor"]
verbe=["mange","slay","arrache","frappe","détruit","a","ecoute"]
complement=["son pantalon","son chien","son cerveau","la flemme","des chips","des crepes","à l'exterieur"]

suj_comp=(random.randint(1,2))


if suj_comp == 1:     #Sujet Verbe Complement

    print ("\t\t\t\t\033[1;35;49m",(random.choice(sujet)) +" "+ "\033[1;33;49m",(random.choice(verbe))+" "+"\033[1;36;49m",(random.choice(complement)) +"\033[1;37;49m .")

else :                  #Sujet Verbe Sujet
    print ("\t\t\t\t\033[1;35;49m",(random.choice(sujet)) +" "+ "\033[1;33;49m",(random.choice(verbe))+" "+"\033[1;36;49m",(random.choice(sujet)) +"\033[1;37;49m !")

