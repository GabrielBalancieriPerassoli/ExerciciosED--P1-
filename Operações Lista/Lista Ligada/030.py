
def InserirElemento(P, x, i):
    Q = 0
    # novo(Q)
    Q.info = x 

    if (P != None):
        if (i == 1):
            Q.prox = P 
            P = Q

        cont = 1
        R = P 
        
        while (R != None) and (cont < i):
            R = R.prox
            cont = cont + 1

        if (R == None):
            return "Posição Inválida"
        
        Q.prox = P.prox
        P.prox = Q 
