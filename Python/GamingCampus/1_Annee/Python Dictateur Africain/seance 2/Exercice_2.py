import random
import operator
print("\n\t\t\t\t=== Exercice 2: ===\n\n")


def randomCalc():
    
    #Declaration des operateurs
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '//':operator.truediv}
    A = random.randint(1,100)
    B = random.randint(1,10)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(A,B)
    print('Calcul\t {} {} {}?\n'.format(A, op, B))

    return answer


i = 0
while i < 5:
    print (randomCalc())
    choose = int(input("Entrez le resultat :\t"))
    i = +1
    
# Vérification du résultat
    if choose == randomCalc():
        points = + 1
        print ("Bravo\n\n")
    else:
        print("Faux !\n\n")


print("\n\n\t\tVous avez donc ",points)