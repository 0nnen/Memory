import random
import operator 

# Def choississant les nombres et l'operateur random en affichant le calcul
def randomCalc():
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '%':operator.truediv}
    A = random.randint(1,100)
    B = random.randint(1,100)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(A,B)
    
    print('\t\t\033[1;30;49m Calcul :\t \033[0;34;49m{} \033[1;31;49m{} \033[0;34;49m{}\n'.format(A, op, B))
    return answer

# Nombre de calcul reussi(s)
points = 0

#Un titre pour faire joli.
print("\n\n\t\t\t\t\033[1;34;49m === LE JEU DU CALCUL MENTAL ===\n\n")

# Permet de n'afficher au maximum que 5 calculs
for i in range(5):
    
        #En cas d'erreur de saisie:
    while True:
        try:
            answer = randomCalc()
            player = float(input("\033[1;37;49m La réponse est : \033[1;35;49m"))
            break
        
        except ValueError:
            print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n")

    #Ajoute ou non un point si la reponse est correct
    if player == answer:
        points += 1
        print("\t\033[0;32;49m Bonne réponse ! \n")
    elif player != answer:
        print("\t\033[0;31;49m Mauvaise réponse ! La réponse était", answer,"\n")
        
# Affiche le score avec un message adapté
print("\t\t\033[1;37;49m Votre score est de", points, "/ 5")
if points == 5 :
    print("\t\033[1;32;49m Félicitations ! Tout est correct !\033[0;37;49m\n")
if points == 4 :
    print("\t\033[1;33;49m Bravo tu y etais presque\033[0;37;49m\n")
if points <= 3 :
    print("\t\033[1;31;49m Tu feras mieux la prochaine fois !\033[0;37;49m\n")


