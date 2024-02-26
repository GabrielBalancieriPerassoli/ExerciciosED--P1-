def RemoveElem(vetor, n, i):
    if i < 0 or i >= n:
        return "Problema de Índice"
    elif n != 0:
        for j in range(i, n):
            vetor[j] = vetor[j + 1]
        del vetor[n]

    n = n - 1
    return vetor, n

vetor = [8, 2, 5, 1, 10, 15, 3]
n = 6
vetor, n = RemoveElem(vetor, n, 2)
print("Lista após remoção:", vetor)
