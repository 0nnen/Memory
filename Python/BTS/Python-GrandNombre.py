print("\t\t\t\t=== Le Plus Grand Nombre : ===\n\n")


n1=int(input("Saisir le premier nombre:   "))
n2=int(input("Saisir le second nombre:   "))
n3=int(input("Saisir le troisieme nombre:   "))

if n1 > n2 and n1 > n3:
    print ("Le nombre choisi est ", n1)
if n2 > n1 and n2 > n3:
    print ("Le nombre choisi est ", n2)
else:
    print ("Le nombre choisi est ", n3)