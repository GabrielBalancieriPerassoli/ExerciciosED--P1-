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

vetor = CriarLista(5)
n = -1
vetor, n = InserirElem(vetor, n, 5, 0, 7)
vetor, n = InserirElem(vetor, n, 2, 1, 7) 
vetor, n = InserirElem(vetor, n, 8, 2, 7) 
vetor, n = InserirElem(vetor, n, 1, 3, 7)  
vetor, n = InserirElem(vetor, n, 10, 4, 7) 
print(vetor)

def Busca(vetor, valor, n):
    i = 0

    while (i <= n):

        if vetor[i] == valor:
            return True
        
        i = i + 1

    return False

valor = 8

print(Busca(vetor, valor, n))