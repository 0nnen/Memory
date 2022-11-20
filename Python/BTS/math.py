from math import *
from random import *
from time import *

#Avec un nombre entier choisi nous meme:
n=int(input('Choisir un nombre entier n:    '))

r=n-4
r=r*n
r=r+4
print ('Le resultat est :   ', r)

#Avec un nombre entier compris entre 0 et 5 choisi aléatoirement:
ran=randint(0,5)
print('Le nombre choisi est:    ', ran)
time.sleep(2)

r1=ran-4
print (ran,' - 4')
time.sleep(1)
r1=r1*ran
print (r1,' x ', ran)
time.sleep(1)
r1=r1+4
print (r1,' + 4')
time.sleep(1)
print ('Le resultat est :   ', r1)