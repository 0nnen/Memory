from math import *

#Déclaration des valeurs:
Jour=int(input("Choississez le nombre de jour(s) :      "))
Heure=int(input("Choississez le nombre d'heure(s) :    "))
Minute=int(input("Choississez le nombre de minute(s) :      "))
Seconde=int(input("Choississez le nombre de seconde(s) :      "))

#Conversion des valeurs:
Conv_Jour=Jour*86400
Conv_Heure=Heure*3600
Conv_Minute=Minute*60

Conv_Totale=Conv_Jour+Conv_Heure+Seconde


#Affichage du total:
print("Cela donne donc ", Conv_Totale ," secondes.")