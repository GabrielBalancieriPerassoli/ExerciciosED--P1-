
def CopiaElem(P):

    Q = 0

    if P == None:
        return "Lista Vázia"
    
    R = P
    P2 = None
    P2_aux = None

    while (R != None):

        # novo(Q)
        Q.info = P.info

        if (P2 == None):
            P2 = Q
            P2_aux = Q
        else:
            P2_aux.prox = Q
            P2 = Q 

        R = R.prox 

    Q.prox = None 

    return P2 
  
