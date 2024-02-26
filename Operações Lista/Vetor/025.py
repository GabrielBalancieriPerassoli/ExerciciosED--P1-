def CriarLista(TAM):
    vetor = [None] * TAM 
    return vetor

vetor = CriarLista(7)

def NumElementos(vetor):
    n = len(vetor) - 1
    return n + 1

print(NumElementos(vetor))