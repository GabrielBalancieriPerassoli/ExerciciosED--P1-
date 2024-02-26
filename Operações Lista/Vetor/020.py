def CriarLista(TAM):
    vetor = [None] * TAM 
    return vetor

def InserirElem(vetor, n, valor, i, TAM):
    if i < 0 or i > TAM:
        return "Problema de Índice"
    elif n < TAM:
        for j in range(n, i, -1):
            vetor[j + 1] = vetor[j]
    
    vetor[i] = valor 
    n = n + 1

    return vetor, n

vetor = CriarLista(7)
n = -1
vetor, n = InserirElem(vetor, n, 5, 2, 7)
vetor, n = InserirElem(vetor, n, 2, 1, 7) 
vetor, n = InserirElem(vetor, n, 8, 0, 7) 
vetor, n = InserirElem(vetor, n, 1, 3, 7)  
vetor, n = InserirElem(vetor, n, 10, 4, 7) 
vetor, n = InserirElem(vetor, n, 15, 5, 7)  
vetor, n = InserirElem(vetor, n, 3, 6, 7)
print(vetor)
print(n)

