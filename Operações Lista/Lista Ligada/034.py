
def busca(P, x):
    if P == None:
        return "Lista Vazia"
    
    Q = P 

    while Q != None and Q.info != x:
        Q = Q.prox 

    return Q