def OrdenaListaLig(P):
    
    if P == None:
        return "Lista Vazia"
    
    trocou = True # Flag começa com TRUE

    while trocou:

        trocou = False # Flag muda para FALSE
        R = P # R aponta para P

        while (R.prox != None):

            Q = R.prox # Faz Q apontar para o prox de R

            if R.info > Q.info: # Se o info de R for maior que o info de Q, faz a troca de valores
                # Troca os valores dos nós
                temp = R.info
                R.info = Q.info
                Q.info = temp
                trocou = True

            R = R.prox # R aponta pro proximo

    return P
