
def LocalizaElem(P, i):

    if (P == None) or (i <= 0):
        return "Valor Inválido ou Nil"
    
    cont = 1
    atual = P 

    while (atual != None) and (cont < i):
        atual = atual.prox
        cont = cont + 1

    if atual != None:
        return "Inválido"
    else:
        devolve = print("Posição", cont, "Elemento" + atual.info)
        return devolve    