import random
print("\t\t\t\t=== Jeu Du Dé : ===\n\n")
print ("   Le dé se lance 6 fois :")
somme=0

for i in range (6):

    dé=random.randint(6,6)
    i = i+1
    print ("N.",i,"\t\tVous obtenez",dé)
    somme=somme + dé 


print("\n\nLa somme des chiffres obtenus est:\t",somme)

#somme=somme+10
if somme%2== 0:
    print ("Le nombre de points obtenu est paire ! Vous gagnez 1 point. :) \n")
else:
    print ("Le nombre de points obtenu est impaire ! Vous perdez 2 points. :) \n")