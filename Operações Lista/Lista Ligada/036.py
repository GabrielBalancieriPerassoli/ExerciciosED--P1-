
def RemoverElem(P, i):

    if P == None:
        return "Lista Vazia"
    
    if (i == 1): # Remoção Inicio
        Q = P
        P = P.prox
        # dispose(Q)
        return P
    else: # Remoção em todo o Resto

        R = P 
        cont = 1

        while (R.prox != None) and (cont < i):
            Q = R
            R = R.prox
            cont = cont + 1
        
        if (R.prox != None):
            Q.prox = R.prox
            # dispose(R)

