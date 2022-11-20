def moyenne (valeurs , effectifs) :
    # print ("calcule la moyenne pondérée d’une série ,affectée de coefficients")
    produits=[]
    for i in range ( len ( valeurs ) ) :
        produits . append  ( valeurs [ i ] ∗ effectifs [ i ] )
        m=sum ( produits ) / sum (effectifs)
        return m
