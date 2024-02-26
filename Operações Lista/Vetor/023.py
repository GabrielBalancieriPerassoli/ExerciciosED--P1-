def CriarLista(TAM):
    vetor = [None] * TAM 
    return vetor

def SeparaLista(vetor, n, posicao):
    
    v2 = CriarLista(posicao)
    v3 = CriarLista(n - posicao)

    for i in range(posicao):
        v2[i] = vetor[i]

    for j in range(posicao, n):
        v3[j - posicao] = vetor[j]

    return v2, v3      

vetor = [1, 2, 3, 4, 5, 6, 7]
n = len(vetor)
posicao = 2
v2, v3 = SeparaLista(vetor, n, posicao)
print("Lista 2:", v2)
print("Lista 3:", v3)