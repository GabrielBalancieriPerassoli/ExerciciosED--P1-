
def SepararListaLig(P, i):

    if (P == None):
        return "Lista Ligada Vazia"

    if i > 0:
        R = P
        cont = 1
        while (R.prox != None) and (cont < i):
            R = R.prox
            cont = cont + 1

        P2 = R.prox
        R.prox = None