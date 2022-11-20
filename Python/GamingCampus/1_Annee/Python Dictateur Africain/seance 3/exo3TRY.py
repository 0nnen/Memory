def inverse(num):

    while True:
        num = (input("\n\t\033[0;37;49m Entrez un nombre pour obtenir son inverse: \033[1;35;49m "))
        print ("\t\t\t",inverse(num),"\033[1;37;49m")
        res = 1 / num
        break
    
    try:
        num = 0
    except:
        print("\t\t\t\033[1;31;49m Saisie Invalide, veuillez réessayer :\n\n\033[1;37;49m")
        while True:
            num = (input("\n\t\033[0;37;49m Entrez un nombre pour obtenir son inverse: \033[1;35;49m "))
            print ("\t\t\t",inverse(num),"\033[1;37;49m")

    return res




print (inverse(10))
