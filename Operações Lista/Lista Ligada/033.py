
def NumElementoLig(P):

    if P == None:
        return "Lista Vazia"

    R = P
    cont = 1

    while (R != None):
        R = R.prox
        cont = cont + 1

    return cont
