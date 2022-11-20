# -*- coding: utf-8 -*-
"""
Programme qui demande à l'utilisateur une base de départ (entre 2 et 16 et shadok), un nombre entier écrit dans cette base, une base d'arrivée
et qui affiche le nombre entré dans la base d'arrivée.

"""

def conv_base10(nombre,base):
    """
    Cette fonction prend 2 arguments, une chaine de caractère et un entier qui est sa base et renvoie sa conversion en entier sous base 10.
    """
    res=0
    temp=0
    puissance=0
    inverse=''
    if nombre[-1]=='A':#pour les bases>10
        res+=10
    elif nombre[-1]=='B':
        res+=11
    elif nombre[-1]=='C':
        res+=12
    elif nombre[-1]=='D':
        res+=13
    elif nombre[-1]=='E':
        res+=14
    elif nombre[-1]=='F':
        res+=15
    else:#pour les bases<10
        temp=int(nombre[-1])
        res+=temp
    inverse=nombre[::-1]#inverse la chaine de caractère
    for i in range(1,len(inverse)):
        puissance+=1
        if inverse[i]=='A':#pour les bases>10
            res+=10*base**puissance
        elif inverse[i]=='B':
            res+=11*base**puissance
        elif inverse[i]=='C':
            res+=12*base**puissance
        elif inverse[i]=='D':
            res+=13*base**puissance
        elif inverse[i]=='E':
            res+=14*base**puissance
        elif inverse[i]=='F':
            res+=15*base**puissance
        else:#pour les bases<10
            res+=int(inverse[i])*base**puissance
    return res

assert conv_base10('ABCDEF',16)==11259375
assert conv_base10('A2138C',13)==3772872
assert conv_base10('1000',2)==8
assert conv_base10('1',10)==1


def conv_base_voulue(nombre,base):
    """
    Cette fonction prend en argument 2 entiers : un nombre sous base 10 et une base, et renvoie la conversion du nombre sous la base dans une chaine de carcatères
    """
    res=''
    temp=nombre
    while temp!=0:#tant qu'on ne divise pas 0 on continue
        temp,reste=temp//base,temp%base#division euclidienne et récupération du reste
        if reste==10:
            reste='A'
        elif reste==11:
            reste='B'
        elif reste==12:
            reste='C'
        elif reste==13:
            reste='D'
        elif reste==14:
            reste='E'
        elif reste==15:
            reste='F'
        res=str(reste)+res
    return res

assert conv_base_voulue(15736,10)=='15736'
assert conv_base_voulue(15736,16)=='3D78'
assert conv_base_voulue(2148,2)=='100001100100'


def conv_base_shadok(nombre):
    """
    cette fonction prend en argument un entier en base 10 et renvoie sa conversion en shadok sous forme de chaine de caractères
    """
    res=''
    temp=nombre
    if temp==0:
        return'GA'
    while temp!=0:
        temp,reste=temp//4,temp%4
        if reste==0:
            reste='GA'
        elif reste==1:
            reste='BU'
        elif reste==2:
            reste='ZO'
        elif reste==3:
            reste='MEU'
        res=reste+res
    return res

assert conv_base_shadok(0)=='GA'
assert conv_base_shadok(16)=='BUGAGA'


def conv_shadok_base10(nombre):
    """
    cette fonction prend en argument une chainde en shadok et renvoie sa convertion en entier sous base 10
    """
    res=''
    puissance=0
    conv=0
    inverse=''
    for i in range(len(nombre)):#cette boucle sert à convertir les caractères shadoks en nombre
        if nombre[i:i+3]=='MEU':
            res+='3'
            i+=2
        elif nombre[i:i+2]=='ZO':
            res+='2'
            i+=1
        elif nombre[i:i+2]=='BU':
            res+='1'
            i+=1
        elif nombre[i:i+2]=='GA':
            res+='0'
            i+=1
    conv+=int(res[-1])
    inverse=res[::-1]
    for n in range(1,len(inverse)):
        puissance+=1
        conv+=int(inverse[n])*4**puissance
    return conv

assert conv_shadok_base10("ZOMEUBU")==45
assert conv_shadok_base10("GA")==0

#interface utilisateur
nombre = (input('Veuillez indiquer votre nombre : '))
base_nombre = (input('Veuillez indiquer la base du nombre : '))
base_voulue = (input('Veuillez indiquer la base voulue : '))
nombre_départ = nombre
nombre_arrivée1=0
nombre_arrivée2=''

if base_nombre=='s':
    nombre_arrivée1=conv_shadok_base10(nombre)
else :
    nombre_arrivée1=conv_base10(nombre, int(base_nombre))

if base_voulue=='s':
    nombre_arrivée2=conv_base_shadok(nombre_arrivée1)
else:
    nombre_arrivée2=conv_base_voulue(nombre_arrivée1, int(base_voulue))
    
print(nombre_départ,'en base',base_nombre,'est égal à',nombre_arrivée2,'en base',base_voulue)