import random
print("\t\t\t\t=== Chevaux: ===\n\n")

Dé=random.randint(1,6)
n=0


print ("Le numéro du dé est : ",Dé, "\n Alors, ")
while Dé < 6:

    n = n + 1
print("Le cheval sort au bout de",n," lancés !\n\n")
