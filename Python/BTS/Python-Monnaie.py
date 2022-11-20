from math import *

print("\t\t\t\t=== Calcul de Monnaie : ===\n\n")

centimes=int(input('Saisir une somme en centimes:   ')) #Demande la valeur




c50= centimes%50
c20= centimes//20
c10= centimes//10
c5= centimes//5
c2= centimes//2
c1= centimes%2  #Valeur égal à 1 ou 0




print (
c1,"piece(s) d'un centimes (1)\n",
c2,"piece(s) de deux centimes(2)\n",
c5,"piece(s) de cinq centimes(5)\n",
c10,"piece(s) de dix centimes(10)\n",
c20,"piece(s) de vingt centimes(20)\n",
c50,"piece(s) de cinquante centimes(50)\n",
)

centimes=int(input('Saisir une somme en centimes:   ')) #Demande la valeur
i50=0
i20=0
i10=0
i5=0
i2=0
i1=0

while centimes!=0:

    if centimes>=50:
        centimes-=50
        i50+=1

    if centimes>=20 and centimes < 50:
        centimes-=20
        i20+=1

    if centimes>=10 and centimes <20:
        centimes-=10
        i10+=1

    if centimes>=5 and centimes <10:
        centimes-=5
        i5+=1

    if centimes>=2 and centimes <5:
        centimes-=2
        i2+=1

    if centimes>=1 and centimes <2:
        centimes-=1
        i1+=1

print (
i1,"pieces d'un centimes(1)\n",
i2,"pieces de deux centimes(2)\n",
i5,"pieces de cinq centimes(5)\n",
i10,"pieces de dix centimes(10)\n",
i20,"pieces de vingt centimes(20)\n",
i50,"pieces de cinquante centimes(50)\n",
)    #Résultat Final