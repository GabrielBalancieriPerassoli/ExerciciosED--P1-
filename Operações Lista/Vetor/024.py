def CriarLista(TAM):
    vetor = [None] * TAM 
    return vetor

def CopiaElem(vetor, n):

    v2 = CriarLista(n)

    for i in range(n):
        v2[i] = vetor[i]

    return v2

vetor = [1,2,3,4,5]
n = len(vetor)
print(CopiaElem(vetor, n))