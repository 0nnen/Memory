from os import system
#Un titre pour faire joli.
print("\n\n\t\t\t\t\033[1;34;49m=== Exercice 5 - Manipulation de chaîne de caractère ===\033[0;37;49m\n\n")

sentence = (input("\n\t\t\033[0;37;49m Entrez une phrase à inverser: \033[1;35;49m "))

# Phrase originale
print ("\n\t\033[0;37;49m La phrase originale :\t\033[1;35;49m", str(sentence))
# Phrase inversée
print ("\t\033[0;37;49m La phrase inversée :\t\033[1;35;49m", str(sentence[::-1]),"\n")



res = (" ne contient pas de")
# Verifie si il y a des Majuscules
for ele in sentence:

    if ele.isupper():
        sum(map(str.islower, ele))
        res = (" contient ")
        break

#Compte le nombre de MAJ dans sentence
numUP = sum(1 for c in sentence if c.isupper())

 
#On crée une liste de la phrase avec les mots séparés
listSentence = sentence.split()
 
#On affiche le mot le plus petit et le plus grand
print("\t\033[0;37;49m Le mot le plus petit est: \033[1;35;49m" + min(listSentence, key=len))
print("\t\033[0;37;49m Le mot le plus grand est: \033[1;35;49m" + max(listSentence, key=len))


# Affiche le resultat
print ("\n\t\t\033[0;37;49m La phrase \033[1;35;49m",res,sum(1 for c in sentence if c.isupper()),"\033[1;37;49m Majuscule(s) \033[0;37;49m\n\n")



# Marque une pause dans le code
system("pause")



#On demande de rentrer une autre phrase
sentence2=input("\n\t\t\033[0;37;49m Entrez une nouvelle phrase à inverser: \033[1;35;49m ")

#Phrase inversée
print ("\t\033[0;37;49m La phrase inversée :\t\033[1;35;49m", str(sentence2[::-1]),"\n")


wordsSentence = []
for i in range(len(listSentence)):
    if listSentence[i].lower() in sentence2.lower().split():
        wordsSentence.append(listSentence[i].lower())
        
print("\033[0;37;49m Les mots communs sont: \033[1;35;49m" + "\033[0;37;49m , \033[1;35;49m".join(wordsSentence),".\n")
