from ListaLigada import No

def SomaListaLigada(P):
    if P == None:
        return 0
    else:
        return P.info + SomaListaLigada(P.prox)
    
print(SomaListaLigada(1,2,3,4,5,6))
    


