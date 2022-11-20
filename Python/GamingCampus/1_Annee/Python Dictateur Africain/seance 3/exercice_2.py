#Un titre pour faire joli.
print("\n\n\t\t\t\t\033[1;34;49m=== Exercice 2 - Array ===\033[0;37;49m\n\n")


#Declare prenoms en tant que tableau et l'affiche
prenoms=["jean","Paul","pierre","Lydie","Ruth","Esther"]
print (prenoms)

#Insere marie à la 1 position et l'affiche prenoms
prenoms.insert(1,"marie")
print(prenoms)

#Supprime Esther, le replace au debut et affiche prenoms
prenoms.remove("Esther")
prenoms.insert(0,"Esther")
print(prenoms)

#Ajoute jaques à la fin de prenoms et l'affiche
prenoms.append("jaques")
print(prenoms)

#Premier caractere de chaque ligne en MAJ
prenoms = [i.title() for i in prenoms]

#Tri par ordre alphabetique
prenoms.sort()
print('Tableau :\n')
print(prenoms)
